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

Specific slots:
- **[fainting_scenario]** What were you doing when you fainted?
- **[fainting_warnings]** Did you experience any warning signs before fainting?
- **[fainting_prevsucc]** How did you feel right before and right after you fainted?
- **[fainting_currmedication]** Have you recently started any new medication?
- **[fainting_familyconditions]** Do you have a family history of sudden and unexplained deaths?
- **[fainting_haschestpain]** Have you experienced chest pain or palpitations before fainting?
- **[fainting_frequency]** Have you fainted more than once in a short period of time?
- **[fainting_medconditions]** Do you have any existing medical conditions such as heart problems, diabetes, or low blood pressure?

### Asking help for poisoning

Specific slots:
- **[poisoning_exposure]** What substances or chemicals were you exposed to?
- **[poisoning_exposuredetails]** When and where did the exposure occur?
- **[poisoning_symptoms]** What symptoms are you experiencing? 
- **[poisoning_recentmeds]** Have you taken any medications or drugs recently?
- **[poisoning_allergies]** Do you have any known allergies to medications or substances?

### Asking help for hyperthermia

Specific slots:
- **[hyperthermia_bodytemp]** What is your body temperature?
- **[hyperthermia_behavior1]** Are you experiencing heavy sweating, weakness, dizziness, or headache?
- **[hyperthermia_drinks]** Have you been drinking enough fluids?
- **[hyperthermia_hotenv]** Have you been in a hot or humid environment for an extended period?
- **[hyperthermia_behavior2]** Are you experiencing nausea, vomiting, or muscle cramps?

### Asking help for hypothermia

Specific slots:
- **[hypothermia_symptoms]** What are the patient's current symptoms? 
- **[hypothermia_coldexposure]** Has the patient been exposed to cold weather or cold water? 
- **[hypothermia_bodytemp]** What is the patient's body temperature? 
- **[hypothermia_behavior1]** Is the patient experiencing shivering, slurred speech, slow breathing, weak pulse, clumsiness, drowsiness, or low energy? 
- **[hypothermia_conditions]** Are there any underlying medical conditions that could have contributed to the hypothermia?

### Asking help for allergic reaction

Specific slots:
- **[allergy_symptoms]** What kinds of symptoms do you have?
- **[allergy_symptomsduration]** How long have you had them?
- **[allergy_symptomsfreq]** When do your symptoms happen, and how long do they last?
- **[allergy_triggers]** Do your symptoms get worse when you're around certain triggers, such as pets or specific environments?

### Asking help for fall

Specific slots:
- **[fall_height]** Did you fall from a height of more than one meter?
- **[fall_seizure]** Have you had a seizure?
- **[fall_behavior1]** Do you have headaches or does your head feel heavy?
- **[fall_runnynose]** Do you have a runny nose?
- **[fall_weakness]** Do you feel any weakness in your arms or legs? 

### Asking help for fever

Specific slots:
- **[fever_time]** When did the fever begin, and for how long has it lasted?
- **[fever_progress]** Has the fever worsened or become better since its onset?
- **[fever_symptoms]** What other symptoms are being experienced along with the fever?
- **[fever_exposures]** Have there been any recent exposures to sick individuals or new medications?
- **[fever_patterns]** Is the fever accompanied by any specific patterns such as chills, rigors, or sweat?

### Asking help for headache

Specific slots:
- **[headache_location]** Where is the pain located?
- **[headache_feeling]** What does the headache feel like?
- **[headache_trigger]** What triggers or aggravates the headaches?
- **[headache_relief]** What relieves the headaches?

## Contextual digressions
I envision contextual digressions to be questions the user asks at some point during a story (a scenario). From my research, I've found a range of general questions; I then queried an LLM to answer these in context of each pathology (scenario) with relevant sources.

### What may have caused this condition?
Question and variants:
- Can you tell me what might have led to this condition?
- Do you have any idea what could be the cause of this condition?
- Could you explain what may have triggered this condition?
- Any thoughts on what might be behind this condition?
- What are the potential causes of this condition?
- Is it possible to identify the factors that may have caused this condition?
- Do we know what could have brought about this condition?
- Can you shed light on what may have contributed to this condition?

### Will it be permanent?
Question and variants:
- Is it going to be permanent?
- Will this be permanent?
- Can we expect this to be permanent?
- Is the permanence of this guaranteed?
- Are we looking at a permanent situation?
- Will it remain this way indefinitely?
- Can we anticipate this being permanent?
- Is there a possibility of this being permanent?
- Might this be permanent?

### How is this condition treated or managed?
Questions and variants:
- What are the treatment options for this condition?
- How can this condition be managed effectively?
- What are the ways to treat or control this condition?
- Could you explain the treatment approach for this condition?
- How might one go about treating or handling this condition?
- What are the available methods for managing this condition?
- Can you outline the treatment or management strategies for this condition?
- What are the recommended approaches for treating or dealing with this condition?
- How is it typically recommended to address this condition?

### What will be the long-term effects on my life?
Questions and variants:
- What are the potential long-term implications for my life?
- How will my life be affected in the long run?
- What long-term effects can I expect on my life?
- What will be the lasting impact on my life?
- How might this situation shape my life in the long term?
- What are the enduring consequences for my life?
- In the grand scheme of things how will this affect my life over time?
- What long-term changes can I anticipate in my life?
- What will be the prolonged influence on my life?

### How can I learn more about my condition?
Questions and variants:
- How can I find more information about my condition?
- What are the best ways to educate myself about my condition?
- Is there a recommended approach to learning more about my condition?
- What resources are available for understanding my condition better?
- Are there any specific methods for gaining knowledge about my condition?
- In what ways can I increase my understanding of my condition?
- What are some effective strategies for getting more information about my condition?
- How should I go about educating myself about my condition?
- Are there any tips for delving deeper into the details of my condition?

### Could my lifestyle or habits be contributing to my pain?
Questions and variants:
- Might the way I live or my habits be causing my discomfort?
- Could the pain I'm experiencing be linked to my lifestyle choices or habits?
- Is it possible that my pain is a result of the way I live or my daily habits?
- Do you think my pain could be connected to the way I lead my life or the habits I have?
- I'm wondering if the way I live or my habits could be playing a part in the pain I'm feeling. What do you think?
- Could my pain be influenced by my lifestyle or the habits I follow?
- Might there be a connection between my pain and the way I conduct my life or my habits?
- Do you think my pain might be due to the way I live or the habits I maintain?
- I'm curious if my pain could be impacted by my lifestyle or the habits I engage in. What's your take on this?

### Are there any lifestyle changes or home remedies that could help alleviate my symptoms?
Questions and variants:
- What are some lifestyle changes or home remedies that could help alleviate my symptoms?
- Are there any natural ways or home remedies to ease my symptoms?
- Could you suggest some home remedies or lifestyle adjustments that may relieve my symptoms?
- What are some ways to alleviate my symptoms naturally such as through lifestyle changes or home remedies?
- I'm looking for advice on lifestyle changes or home remedies that could help with my symptoms. Any suggestions?
- Do you know of any home remedies or lifestyle changes that are effective in alleviating symptoms?
- Are there any natural or home-based solutions that could help ease my symptoms?
- What lifestyle modifications or home remedies would you recommend to help ease my symptoms?
- Could you provide information on home remedies or changes in lifestyle that may assist in alleviating my symptoms?

### What should I do if my symptoms persist or worsen?
Questions and variants:
- If my symptoms don't improve or get worse what actions should I take?
- In case my symptoms persist or become more severe what would be the recommended course of action?
- What steps should I follow if my symptoms continue or worsen over time?
- Should my symptoms persist or worsen what should be my next steps?
- If my symptoms don't get better or worsen what would you advise me to do?
- In the event that my symptoms persist or deteriorate what actions do you recommend I take?
- What are the appropriate measures to take if my symptoms linger or worsen?
- If my symptoms stay the same or worsen what should be my plan of action?
- Should my symptoms not improve or worsen what steps should I be prepared to take?