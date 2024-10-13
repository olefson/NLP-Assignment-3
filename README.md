# NLP-Assignment-3

## Explanation of Functions

### findPlagiarism(sentences, target)

Description:
The findPlagiarism function detects which sentence from a given list of sentences is most likely to have been plagiarized to create the provided target sentence. The comparison is done by calculating the similarity between the target sentence and each sentence in the list using pre-trained Word2Vec embeddings. Cosine similarity is used to identify the most similar sentence.

#### Parameters
sentences (list of str): A list of sentences (strings) where each string represents a sentence.
target (str): The target sentence that has potentially been plagiarized from one of the sentences in the list.

#### Returns
int: The index of the sentence from the sentences list that is most similar to the target sentence based on cosine similarity.