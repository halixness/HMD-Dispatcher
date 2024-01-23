from rasa_sdk.events import EventType, SlotSet
from typing import List

class SlotMappingUtilities:
    
    @staticmethod
    def extract_slot_from_last_intent(slot, tracker) -> List:
        """
            Extract entities or whole answer while mapping an answer to a specific slot

        """
        detected_intent = tracker.get_intent_of_latest_message()
        if detected_intent == f"inform_pain_description":
            curr_slot_value = tracker.get_slot("slot")
            entity_value = f"{curr_slot_value}; " if curr_slot_value else "" # supports filling over time
            detected_entities = tracker.latest_message['entities']        
            # entities -> fill slot with entity values
            if len(detected_entities) > 0:
                for entity in tracker.latest_message['entities']:
                    if entity['entity'] == slot:
                        entity_value += f"{entity['value']}; "
            # no entities -> fill slot with the entire text
            else:    
                entity_value = tracker.latest_message.get("text")
            return [SlotSet(slot, entity_value)]
        else: return []