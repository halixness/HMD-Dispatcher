# NLU Schema
Diego Calanzone. University of Trento, AY. 2023-2024.

## Scenarios
I define the scenarios based on the pathologies to handle. From a [recent research](https://www.unitekemt.com/blog/most-common-ems-emergencies-for-emts-and-paramedics/), the most common are (plus some additions):
- Abdominal pain
- Respiratory difficulty
- Fainting
- Poisoning/drug abuse
- Hyperthermia
- Hypothermia
- Allergic reaction
- Fall
- Fever
- Headache

## Intents
General slots:
- **[full_name]**
- **[address]**
- **[phone_number]**

### Asking help for abdominal pain 

Specific slots:
- **[pain_time]** When does the pain occur? In the morning? After eating? Always?
- **[pain_area]** Where does the pain occur? In the entire abdomen or a specific area?
- **[pain_type]** What type of pain are you experiencing? Dull ache? Sharp pain? Persistent or in waves?
- **[pain_worsening]** What makes the pain worse? Coughing?
- **[pain_relief]** What makes the pain better? Eating? Not eating?
- **[pain_duration]** How long have you experienced this pain? Days? Months?

### Asking help for respiratory difficulty

Specific slots:
- **[respiratory_difficulty_atnight]** Do you have any problems breathing at night? 
- **[respiratory_difficulty_usepillows]** Do you use pillows to help you get in a position to breathe easier? 
- **[respiratory_difficulty_pastexp]** Has this happened before?
- **[respiratory_difficulty_frequency]** Did this episode come on suddenly? 
- **[respiratory_difficulty_familiarity]** Do you have any relatives suffering from respiratory difficulties or lung diseases?

### Asking help for fainting

