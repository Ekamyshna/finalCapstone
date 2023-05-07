# Importing spacy
import spacy
nlp = spacy.load('en_core_web_sm')

# Storing the garden path sentences in a list called gardenpathSentences
gardenpathSentences = ("The horse raced past the barn fell. The old man the boat.\
Mary gave the child a Band-Aid.\
That Jill is never here hurts.\
The cotton clothing is made of grows in Mississippi.")

doc = nlp(gardenpathSentences)

# Tokenise each sentence in the list 
print([token.orth_ for token in doc if not token.is_punct | token.is_space])

# Performing named entity recognition
nlp_garden = nlp(gardenpathSentences)
print([(i, i.label_, i.label) for i in nlp_garden.ents])

# Using spacy.explain to look up and print the meaning of entities that I don’t understand
print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))

# Two entities that I looked up were "PERSON" and "GPE"

# Explanation for "PERSON" - refers to People, including fictional
# The entity name "PERSON" makes sense for the word that is associated with it

# Explanation for "GPE" - refers to Countries, cities, states
# The entity name "GPE" makes sense for the word that is associated with it


