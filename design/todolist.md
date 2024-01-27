## Behaviors to handle

### Quality checkup
- [ ] Over-informative user
- [ ] Mixed initiative
- [ ] Low coherence user
- [ ] Conversational markers
- [ ] Error handling
    - No speech
    - Ambiguous input
    - Error escalation: give indications on the correct input

### Pathologies
- [x] Abdominal pain
- [x] Respiratory distress
- [x] Fainting
- [ ] Poisoning/drug abuse
- [ ] Hyperthermia
- [x] Hypothermia
- [x] Allergic reaction
- [x] Fall
- [x] Fever
- [x] Headache

### Issues
- [ ] custom slot mapping: how to apply it conditionally? It always runs for all slots and it empties the values...
- [ ] Once general info are filled, how to detect whether an emergency has been already reported? Probably global slot mapping or some logical check. We broke down pain_type into different pathologies. Otherwise how would we detect the scenarios?

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