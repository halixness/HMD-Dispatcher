from typing import Text, List, Any, Dict
from utils.geocoding import Geocoding
from utils.nlu import SlotMappingUtilities

from rasa_sdk.events import EventType, SlotSet
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# References
# [1] https://rasa.com/docs/rasa/forms/#using-a-custom-action-to-ask-for-the-next-slot
# [2] https://rasa.com/docs/rasa/forms/#validating-form-input

# ========================== General info form validation 

TOLERATED_ATTEMPTS = 2

def get_num_attempts(tracker, repetition_utterance):
    repetitions = ["utter_repeat_last_time", repetition_utterance]
    attempts = 0
    for past_event in tracker.events:
        if "metadata" in past_event and "template" in past_event["metadata"]:
            attempts += int(past_event["metadata"]["template"] in repetitions) 
    return attempts

class AskPatientHomeAddr(Action):
    
    def name(self) -> Text:
        return "action_ask_patient_homeaddr"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """
            Formulating how to ask the form field depending on repetitions
        """
        home_addr = tracker.get_slot('patient_homeaddr')
        if home_addr is None:
            attempts = get_num_attempts(tracker, repetition_utterance="utter_invalid_patient_homeaddr")
            # asking for the param depending on the errors
            if not attempts:
                dispatcher.utter_message(response="ask_patient_homeaddr", verb="provide")
            else:
                dispatcher.utter_message(response="ask_patient_homeaddr", verb="repeat")
        return []
    
class SubmitPatientCoordinates(Action):
    
    def name(self) -> Text:
        return "action_submit_patient_coordinates"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:

        home_address = tracker.get_slot('patient_homeaddr')
        phone = tracker.get_slot('patient_phonenmbr')
        helpRequest = {
            "address": home_address,
            "phone": phone
        }
        print(f"[!] New help request at: {helpRequest}")
        return []
    

class SubmitEmergencyForm(Action):
    
    def name(self) -> Text:
        return "action_submit_emergency_form"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        answers = [
            tracker.get_slot('pain_nature'),
            tracker.get_slot('pain_location'),
            tracker.get_slot('pain_duration'),
            tracker.get_slot('pain_severity'),
            tracker.get_slot('pain_relieving'),
            tracker.get_slot('pain_symptoms'),
            tracker.get_slot('pain_history'),
            tracker.get_slot('pain_trauma'),
            tracker.get_slot('pain_allergies'),
            tracker.get_slot('pain_warnings'),
        ]
        print(f"[!] New help request at: {answers}")
        return []
    
    
class MapPainDuration(Action):
    
    def name(self) -> Text:
        return "action_map_pain_duration"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_duration", tracker=tracker)
    
class MapPainSeverity(Action):
    
    def name(self) -> Text:
        return "action_map_pain_severity"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_severity", tracker=tracker)

# ============== Abdominal pain actions ==============

class MapAbdominalPainArea(Action):
    
    def name(self) -> Text:
        return "action_map_abdominal_pain_area"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="abdominal_pain_area", tracker=tracker)
        
class MapAbdominalPainOtherSymptoms(Action):
    
    def name(self) -> Text:
        return "action_map_abdominal_other_symptoms"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="abdominal_other_symptoms", tracker=tracker)
        
# ============== Hypothermia actions ==============

class MapHypothermiaSkincolor(Action):
    
    def name(self) -> Text:
        return "action_map_hypothermia_skin_color"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="hypothermia_skin_color", tracker=tracker)

class MapHypothermiaTreatment(Action):
    
    def name(self) -> Text:
        return "action_map_hypothermia_treatment"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="hypothermia_treatment", tracker=tracker)



class ValidateFormGeneralInfo(FormValidationAction):

    def name(self) -> Text:
        return "validate_form_general_info"

    def validate_patient_homeaddr(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        """ 
            Validate a home address through geocoding API (just if the address exists)
        """
        attempts = get_num_attempts(tracker, repetition_utterance="utter_invalid_patient_homeaddr")
        # geochecking
        address_is_valid = Geocoding.is_address_valid(slot_value)
        if not address_is_valid and attempts < TOLERATED_ATTEMPTS:
            if not attempts:
                dispatcher.utter_message(response="utter_invalid_patient_homeaddr")
            else: 
                dispatcher.utter_message(response="utter_repeat_last_time")
            return {"patient_homeaddr": None}
        else:
            return {"patient_homeaddr": slot_value}

# ========================== General info form validation 
        
class SetPathology(Action):
    
    def name(self) -> Text:
        return "action_set_pathology"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """
            Formulating how to ask the form field depending on repetitions
        """
        intent_pathology = None
        for idx in range(len(tracker.events)-1, 0, -1):
            event = tracker.events[idx]
            if "parse_data" in event and "patient_reports_" in event["parse_data"]["intent"]["name"]:
                intent_pathology = event["parse_data"]["intent"]["name"]
        if intent_pathology:
            return [SlotSet("reported_pathology", intent_pathology)]
        else:
            return []
