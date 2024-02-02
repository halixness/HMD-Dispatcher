## Behaviors to handle

### Quality checkup
- [ ] Grounding
    - Meaning: establishing a common reality shared among the speakers. Speakers can perform grounding by: attending to one's logic, providing the next relevant contribution, completing or paraphrasing one's contributions, repeating verbatim. 
    - [ ] Example 1: "I need X's phone number", "ok, first I need to know from which town". "fist" = grounding term that informs of a sequential procedure to collect info with some rules.
    - [x] Example 2: providing aknowledgements after one's utternce is a sign of grounding. e.g. "my phone number is X", "okay, what is your town name?". "okay" informs about a transition and a correct reception of the content.
- [ ] Error handling
    - Over-informative user
    - Low coherence user
    - No speech
    - Ambiguous input
    - Error escalation: give indications on the correct input
- [x] Mixed initiative
- [x] Conversational markers

### Testing
- [ ] what happens if I re-set a reported pain? story twist?
    - I also have this other issue: the agent may detect whether it's in the middle of something (then ask to finish the current request first), then moves on to collecting a new request with proper var setup
- [x] Test when user changes their mind during QA and wants to call an ambulance.
- [x] The model confuses pain_area with reports_pain
- [x] Implement end of the conversation and reset
- [x] Abdominal pain
- [x] Respiratory distress
- [x] Fainting

### Issues/TODO
- [ ] Improve conversation markers
    - Before each utterance, set a conversation marker slot that changes depending on the previous intent
- [x] implement QA for fever
- [x] re-test negative answers
- [x] the model loops through the same question
- [x] The model seems not to generalize negative answers. We may use a custom mapping for that. => retraining and fixing other intents solved it.
- [x] Refactor abdominal_pain_area


### Added pathologies
- [x] Abdominal pain
- [x] Respiratory distress
- [x] Fainting
- [x] Hypothermia
- [x] Allergic reaction
- [x] Fever

### High priority
- [x] the agent should alert they're going to ask specific questions
- [x] maybe the agent should give some feedback after some questions being answered.
- [x] after collecting specific questions, the agent should give a feedback.
- [x] initial prompt: what's your emergency?
- [ ] test all points of interruption to talk with human operator
- [ ] implementing pain related questions
- [ ] improve the NLU to parse home addresses
- [ ] improve the NLU to parse symptoms
- [ ] implementing user questions

### Low priority
- [ ] Handling multiple types of pain reported at once
- [ ] implementing agent repeating the address and number as confirmation
- [ ] implement phone number repetition and verification
- [x] Adding more variants of the prompted text
