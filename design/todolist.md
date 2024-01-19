## Behaviors to handle

### Questions
- [ ] Is it good practice to keep separate forms for each scenario (type of pain)? We have variable amounts of questions. No, we'll have a general form of questions regardless of the emergency.
- [ ] Is it good practice to receive any input text to a form question with "from_text", regardless of the detected intent?

### High priority
- [x] the agent should alert they're going to ask specific questions
- [x] maybe the agent should give some feedback after some questions being answered.
- [x] after collecting specific questions, the agent should give a feedback.
- [x] initial prompt: what's your emergency?
- [ ] How to fix questions that depend on whether a pain has been reported before? Probably custom actions.
- [ ] improve the NLU to parse home addresses
- [ ] improve the NLU to parse symptoms
- [ ] implementing user questions
- [ ] implementing all scenario forms

### Low priority
- [ ] how to handle any question the user asks while a form is being filled? (interruptions)
- [ ] Handling multiple types of pain reported at once
- [ ] Handling address and phone number reported in one message
- [ ] Adding more variants of the prompted text