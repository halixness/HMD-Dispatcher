from typing import Text, List, Any, Dict
from modules.geocoding import Geocoding

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# ========================== General info form validation 

class ValidateFormGeneralInfo(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_general_info"

    def validate_patient_homeaddr(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        """ 
            Validate a home address through geocoding API (just if the address exists)
        """
        address_is_valid = Geocoding.is_address_valid(slot_value)
        if not address_is_valid:
            dispatcher.utter_message(text="Can you repeat the given address please?")
            return {"patient_homeaddr": None}
        else:
            return {"patient_homeaddr": slot_value}

# ========================== General info form validation 