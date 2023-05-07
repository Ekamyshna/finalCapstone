# finalCapstone
This is the last Capstone Project that I created and also NLP project on garden path sentences.
In a file called nlp_1.pdf, I categorised which type of NLP application applies for
each of the use-cases. In a file called nlp_2 I wrote a brief summary about IBM innovative technology Watson Discovery using NLP.
# Table of contents
* [Installation](https://github.com/Ekamyshna/finalCapstone/tree/master#installation-for-windows)
 * [What is NLP (Natural Language Processing)](https://en.wikipedia.org/wiki/Natural_language_processing)
 * [Examples of NLP and how it is used](https://www.wonderflow.ai/blog/natural-language-processing-examples)
 * [Natural Language Processing With spaCy in Python](https://realpython.com/natural-language-processing-spacy-python/#:~:text=spaCy%20is%20a%20free%2C%20open,general%2Dpurpose%20natural%20language%20processing.)
 * [Usage](https://github.com/Ekamyshna/finalCapstone/edit/master/README.md#usage)
 * [Credits](https://github.com/Ekamyshna/finalCapstone/edit/master/README.md#credits)
# Installation for Windows
![image](https://user-images.githubusercontent.com/127347872/236679858-656ee4ed-05d0-4ee0-a794-90b4d4613fd1.png)
![image](https://user-images.githubusercontent.com/127347872/236679795-6484e809-b20d-4e73-9d68-173a1cafb849.png)
![image](https://user-images.githubusercontent.com/127347872/236679905-22f9da35-12be-4bd8-a57a-ed4fb1024272.png)
# Usage
 * Read the introduction about [garden path sentences](https://en.wikipedia.org/wiki/Garden-path_sentence) and study a few of
the examples on Wikipedia
* Create a new Python file called garden.py
* Import spaCy 

![image](https://user-images.githubusercontent.com/127347872/236680547-be8a17e8-552d-4a3a-bf40-c9af0fd85fc3.png)
* Store the sentences you have identified or created in a list called
gardenpathSentences.

* Add the following sentences to your list:
 1. Mary gave the child a Band-Aid.
 2. That Jill is never here hurts.
 3. The cotton clothing is made of grows in Mississippi.

![image](https://user-images.githubusercontent.com/127347872/236680643-cfdd6dd2-032b-4589-8272-7dd6f9bca12a.png)

* Tokenise each sentence in the list and perform [named entity recognition](https://spacy.io/usage/linguistic-features#named-entities).

![image](https://user-images.githubusercontent.com/127347872/236681197-ebe1a630-0663-4f94-8b38-4220f417af71.png)
![image](https://user-images.githubusercontent.com/127347872/236681272-b770a729-fbc0-4375-b587-aa5b34341205.png)

* Examine how spaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don’t
understand. For example: print(spacy.explain("FAC"))

![image](https://user-images.githubusercontent.com/127347872/236681337-cdada56c-2a05-45d0-aa8d-6d580be0cf16.png)

*  At the bottom of your file, write a comment about two entities that you
looked up. For each entity answer the following questions:
  1. What was the entity and its explanation that you looked up?
  2. Did the entity make sense in terms of the word associated with it?

![image](https://user-images.githubusercontent.com/127347872/236681404-8da33319-9c63-4948-bb7a-baf5429fdea8.png)

# NLP_1
* In a file called nlp_1.pdf, categorise which type of NLP application applies for
each of the following use-cases:
 1. A model that allocates which mail folder an email should be sent to
    (work, friends, promotions, important), like Gmail’s inbox tabs.
 2. A model that helps decide what grade to award to an essay question.
     This can be used by a university professor who grades a lot of classes
     or essay competitions.
 3. A model that provides assistive technology for doctors to provide
    their diagnosis. Remember, doctors ask questions, so the model will
    use the patients’ answers to provide probable diagnosis for the
    doctor to weigh and make decisions
* Example

![image](https://user-images.githubusercontent.com/127347872/236681950-b6f54848-bc31-44b7-b9e6-5975c4c09b1e.png)

# Credits
* [NLP applications](https://datasciencedojo.com/blog/natural-language-processing-applications/)
* [NLP IBM Watson Discovery](https://www.ibm.com/cloud/watson-discovery)








