## Behaviors to handle

### Questions

### Issues
- [x] Slots are filled even when they already contain a value. E.g. medical questions, classified intent "pain_type" overwrites current slot value. This can happen arbitrarily. Fixed with conditions in slot mapping on active loop!

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