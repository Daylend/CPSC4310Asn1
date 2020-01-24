#!/usr/bin/python3
import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.lm import Vocabulary
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
import cProfile
"""
 How many word tokens does each category/genre have?
 How many word types does each category/genre have?
 What is the vocabulary size of the whole corpus?
 
 With stopwords, without stopwords, without stopwords and lemmatization,
 without stopwords and stemming.
 
 Display by category.
 Use the brown corpus.
"""

nltk.download('brown')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def getTags(words):
    tags = nltk.pos_tag(words)

    taglist = dict()

    for t in tags:
        # Tags are stored at t[1]
        tag = t[1]
        # Track occurances of each tag
        if tag in taglist:
            taglist[tag] += 1
        else:
            taglist[tag] = 1

    return taglist

def printCategory(cat, words):
    wtags = getTags(words)
    print("Category: " + str(cat))
    print("\tWord tokens with stopwords: " + str(len(words)))
    print("\tWord types with stopwords: " + str(len(wtags)))
    print("\tVocab size with stopwords: " + str(len(set(words))))
    print("-----------------------------")
    sw = stopwords.words('english')
    # Exclude stopwords from list of words
    nostopwords = [w for w in words if w.lower() not in sw]
    nostopwordtags = getTags(nostopwords)
    print("\tWord tokens without stopwords: " + str(len(nostopwords)))
    print("\tWord types without stopwords: " + str(len(nostopwordtags)))
    print("\tVocab size without stopwords: " + str(len(set(nostopwords))))
    print("-----------------------------")
    lmtzr = WordNetLemmatizer()
    # Lemmatize each word in list of no stop words
    lemmatized = [lmtzr.lemmatize(w) for w in nostopwords]
    lemmatizedtags = getTags(lemmatized)
    print("\tWord tokens without stopwords and lemmatization: " + str(len(lemmatized)))
    print("\tWord types without stopwords and lemmatization: " + str(len(lemmatizedtags)))
    print("\tVocab size without stopwords and lemmatization: " + str(len(set(lemmatized))))
    print("-----------------------------")
    stmr = PorterStemmer()
    # Stem each word in list of no stop words
    stemmed = [stmr.stem(w) for w in nostopwords]
    stemmedtags = getTags(stemmed)
    print("\tWord tokens without stopwords and stemmed: " + str(len(stemmed)))
    print("\tWord types without stopwords and stemmed: " + str(len(stemmedtags)))
    print("\tVocab size without stopwords and stemmed: " + str(len(set(stemmed))))
    print("-----------------------------")


for cat in brown.categories():
    printCategory(cat, brown.words(categories=cat))

#print(stopwords.words('english'))