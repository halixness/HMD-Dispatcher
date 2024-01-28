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
    

class TogglePainIsReported(Action):
    
    def name(self) -> Text:
        return "action_toggle_is_pain_reported"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Check history for reported pathologies """
        for past_event in tracker.events:
            if "parse_data" in past_event:
                has_detected_entities = len(past_event["parse_data"]["entities"]) > 0
                has_reported_pain = past_event["parse_data"]["intent"]["name"] == "patient_reports_pain"
                if has_reported_pain and has_detected_entities: return [SlotSet("is_pain_reported", True)]
        return [SlotSet("is_pain_reported", False)]            
    
    
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

class MapPainLocation(Action):
    
    def name(self) -> Text:
        return "action_map_pain_location"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_location", tracker=tracker)

class MapPainNature(Action):
    
    def name(self) -> Text:
        return "action_map_pain_nature"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_nature", tracker=tracker)

class MapPainSymptoms(Action):
    
    def name(self) -> Text:
        return "action_map_pain_symptoms"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_symptoms", tracker=tracker)

class MapPainHistory(Action):
    
    def name(self) -> Text:
        return "action_map_pain_history"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_history", tracker=tracker)

class MapPainRelieving(Action):
    
    def name(self) -> Text:
        return "action_map_pain_relieving"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="pain_relieving", tracker=tracker)


# ============== Abdominal pain actions ==============

class MapAbdominalPainArea(Action):
    
    def name(self) -> Text:
        return "action_map_abdominal_pain_area"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="abdominal_pain_area", tracker=tracker)
        
# ============== Respiratory difficulty actions ==============


class MapRespiratoryDiffTriggers(Action):
    
    def name(self) -> Text:
        return "action_map_resp_difficulty_triggers"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="resp_difficulty_triggers", tracker=tracker)

# ============== Fainting actions ==============

class MapFaintingPrior(Action):
    
    def name(self) -> Text:
        return "action_map_fainting_prior"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="fainting_prior", tracker=tracker)

class MapFaintingMedicalConditions(Action):
    
    def name(self) -> Text:
        return "action_map_fainting_medical_conditions"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="fainting_medical_conditions", tracker=tracker)


# ============== Hypothermia actions ==============

class MapHypothermiaSkincolor(Action):
    
    def name(self) -> Text:
        return "action_map_hypothermia_skin_color"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="hypothermia_skin_color", tracker=tracker)

class MapHypothermiaEnv(Action):
    
    def name(self) -> Text:
        return "action_map_hypothermia_env"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="hypothermia_env", tracker=tracker)

# ============== Allergy actions ==============
class MapAllergyCause(Action):
    
    def name(self) -> Text:
        return "action_map_aller_cause"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="aller_cause", tracker=tracker)
    
class MapAllergySymptoms(Action):
    
    def name(self) -> Text:
        return "action_map_aller_symptoms"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="aller_symptoms", tracker=tracker)
class ActionSetAllergyHistory(Action):
    def name(self) -> str:
        return "action_map_aller_history"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        intent = tracker.latest_message["intent"]["name"]
        is_travel = intent == "affirmative"
        return [SlotSet("aller_history", is_travel)]

# ============== fall actions ==============
class MapFallConscious(Action):
    
    def name(self) -> Text:
        return "action_map_fall_conscious"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="fall_conscious", tracker=tracker)
class MapFallMovement(Action):
    
    def name(self) -> Text:
        return "action_map_fall_movement"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="fall_movement", tracker=tracker)

# ================= fever =====================
class MapFeverTemperature(Action):
    
    def name(self) -> Text:
        return "action_map_fever_temperature"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="fever_temperature", tracker=tracker)

class ActionSetInfoTravelSlot(Action):
    def name(self) -> str:
        return "action_map_fever_travel"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        intent = tracker.latest_message["intent"]["name"]
        is_travel = intent == "affirmative"
        return [SlotSet("fever_travel", is_travel)]
# ================ headache ====================
class MapHeadLife(Action):
    
    def name(self) -> Text:
        return "action_map_headachelifestyle"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        """ Runs custom utility to read entities and fill in the slot """
        return SlotMappingUtilities.extract_slot_from_last_intent(slot="headache_lifestyle", tracker=tracker)
# ========================================================


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

