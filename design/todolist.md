## Behaviors to handle

### Quality checkup
- [ ] Over-informative user
- [x] Mixed initiative
- [ ] Low coherence user
- [x] Conversational markers
- [ ] Grounding
    - Meaning: establishing a common reality shared among the speakers. Speakers can perform grounding by: attending to one's logic, providing the next relevant contribution, completing or paraphrasing one's contributions, repeating verbatim. 
    - [ ] Example 1: "I need X's phone number", "ok, first I need to know from which town". "fist" = grounding term that informs of a sequential procedure to collect info with some rules.
    - [x] Example 2: providing aknowledgements after one's utternce is a sign of grounding. e.g. "my phone number is X", "okay, what is your town name?". "okay" informs about a transition and a correct reception of the content.
- [ ] Error handling
    - No speech
    - Ambiguous input
    - Error escalation: give indications on the correct input

### Testing
- [ ] The model confuses pain_area with reports_pain
- [ ] Implement end of the conversation and reset
- [ ] Test when user changes their mind during QA and wants to call an ambulance.
- [x] Abdominal pain
- [x] Respiratory distress
- [x] Fainting
- [ ] Hypothermia
- [ ] Allergic reaction
- [ ] Fever

### Issues/TODO
- [ ] what happens if I re-set a reported pain? story twist?
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
