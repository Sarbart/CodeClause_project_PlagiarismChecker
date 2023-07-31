# -*- coding: utf-8 -*-
"""Plagiarism_Checkber.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O4JyrqlJbwJ4e15vdlJEVCCp_cnWfMUa
"""

Installing the required libraries

!pip install nltk
!pip install scikit-learn

Importing the necessary libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

>>> import nltk
  >>> nltk.download('punkt')

>>> import nltk
  >>> nltk.download('stopwords')

Preprocessing the text

def preprocess_text(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stop words and non-alphanumeric characters
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Join the words back into a sentence
    processed_text = " ".join(words)
    return processed_text

Creating a function to calculate similarity between two documents:

def calculate_similarity(text1, text2):
    # Preprocess the texts
    processed_text1 = preprocess_text(text1)
    processed_text2 = preprocess_text(text2)

    # Create tf-idf vectors for the two documents
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([processed_text1, processed_text2])

    # Calculate cosine similarity between the tf-idf vectors
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity_score[0][0]

Testing the plagiarism checker:

if __name__ == "__main__":
    # Sample texts to check for plagiarism
    text1 = "This is an original text for testing."
    text2 = "This is a similar text for testing plagiarism."
    text3 = "This text is completely different."

    similarity_threshold = 0.8

    similarity_score1 = calculate_similarity(text1, text2)
    similarity_score2 = calculate_similarity(text1, text3)

    print("Similarity Score between text1 and text2:", similarity_score1)
    print("Similarity Score between text1 and text3:", similarity_score2)

    if similarity_score1 >= similarity_threshold:
        print("text1 and text2 may be plagiarized.")
    else:
        print("text1 and text2 are not plagiarized.")

    if similarity_score2 >= similarity_threshold:
        print("text1 and text3 may be plagiarized.")
    else:
        print("text1 and text3 are not plagiarized.")



