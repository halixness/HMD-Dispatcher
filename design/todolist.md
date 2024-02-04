## Behaviors to handle

### Report
- [ ] Create google forms for all the extrinsic evaluation experiments
- [ ] Run extrinsic evaluation experiments
- [ ] Run all intrinsic evaluation experiments
- [ ] Illustrate sample rasa shell conversations with the chatbot
- [ ] Record 2 videos for 3 cases: ask ambulance, report emergency, interrupt with human agent
- [ ] Run on Alexa
- [x] Finish the interaction aspects part
- [x] Refine the conversation flow diagram

### Quality checkup
- [x] Grounding
    - Meaning: establishing a common reality shared among the speakers. Speakers can perform grounding by: attending to one's logic, providing the next relevant contribution, completing or paraphrasing one's contributions, repeating verbatim. 
    - [x] Example 1: "I need X's phone number", "ok, first I need to know from which town". "fist" = grounding term that informs of a sequential procedure to collect info with some rules.
    - [x] Example 2: providing aknowledgements after one's utternce is a sign of grounding. e.g. "my phone number is X", "okay, what is your town name?". "okay" informs about a transition and a correct reception of the content.
- [x] Error handling
    - [x] Over-informative user
    - [x] Low coherence user
    - [x] No speech
    - [x] Ambiguous input
    - [ ] Error escalation: give indications on the correct input
- [x] Mixed initiative
- [x] Conversational markers

### Testing
- [ ] User asks to restart : tested, keeps running action_default_fallback
- [ ] test two stage fallback
- [ ] implement phone validation
- [x] what happens if I reset a reported pain? story twist?
    - Agent moves on to the next form: OK!
- [x] Test over informative user
    - The model skips the questions and jumps to the missing one! Cool beans!!!!!
    - Just improve "is_pain_reported" mapping to toggle with detected entities
- [x] Test when user changes their mind during QA and wants to call an ambulance.
- [x] The model confuses pain_area with reports_pain
- [x] Implement end of the conversation and reset
- [x] Abdominal pain
- [x] Respiratory distress
- [x] Fainting
- [x] Allergy
- [x] Fever

### Issues/TODO
- [ ] Improve conversation markers
    - Before each utterance, set a conversation marker slot that changes depending on the previous intent
- [x] implement QA for fever
- [x] re-test negative answers
- [x] the model loops through the same question
- [x] The model seems not to generalize negative answers. We may use a custom mapping for that. => retraining and fixing other intents solved it.
- [x] Refactor abdominal_pain_area
