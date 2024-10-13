"""This is a sample file for hw3. 
It contains the functions that should be submitted,
except all it does is output a random value.
- Dr. Licato"""

import random
import gensim.models.keyedvectors as word2vec
from sklearn.linear_model import LogisticRegression
from scipy.spatial.distance import cosine as cosDist
import numpy as np
import json

model = None

def setModel(Model):
	global model
	model = Model

def findPlagiarism(sentences, target):
	global model # load global word2vec model
 
	def sentence2vec(sentence):
		# tokenizew sentence by splitting words
		words = sentence.split()
		# filter out words not found in model
		valid_words = [word for word in words if word in model.wv]
		# if no valid words, return 0 vec
		if not valid_words:
			return np.zeros(model.vector_size)
		# average word vectores
		word_vectors = [model.wv[word] for word in valid_words]
		return np.mean(word_vectors, axis=0)

	# Get Vec for target sentence
	target_vec = sentence2vec(target)
	
	# Tracking Variables
	max_sim = -1
	most_sim_idx = -1
 
	# Iterate through sentences
	for i, sentence in enumerate(sentences):
		# get vec for current sentence
		sentence_vec = sentence2vec(sentence)
		# calculate cosine similarity
		sim = cosDist(target_vec, sentence_vec)
		# similarity tracking
		if sim > max_sim:
			max_sim = sim
			most_sim_idx = i
	return most_sim_idx
 
def classifySubreddit_train(file):
	pass

def classifySubreddit_test(text):
	return "subredditName"