from typing import List
import string
from collections import Counter
import numpy as np


def clean_text(text : str) -> List[str]:
    lower_case_text = [t.lower() for t in text.split()]
    cleaned_list = []
    for word in lower_case_text:
        curr_word = ""
        for char in word:
            if char not in string.punctuation:
                curr_word+=char
            else :
                pass
        if curr_word:
            cleaned_list.append(curr_word)
    return cleaned_list


def word_frequencies(word_list: list[str]) -> dict[str, int]:
    return dict(Counter(word_list))


def build_vocabulary(all_cleaned_word_lists: list[list[str]]) -> list[str]:
    combined_list = []
    for word_list in all_cleaned_word_lists:
        for word in word_list:
            combined_list.append(word)
    return sorted(set(combined_list))


def vectorize(word_freq: dict[str, int], vocabulary: list[str]) -> np.ndarray:
    arr = []
    for word in vocabulary:
        if word not in word_freq.keys():
            arr.append(0)
        else:
            arr.append(word_freq.get(word))
    return np.array(arr)


def cosine_similarity(vector1: np.ndarray, vector2: np.ndarray) -> np.float64:
    similarity_score = vector1.dot(vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )
    return similarity_score


doc1_words = clean_text("Hello, World! This is RAG.")
doc2_words = clean_text("RAG is great for search")
vocab = build_vocabulary([doc1_words, doc2_words])
print(vocab)

freq = word_frequencies(doc1_words)
print(freq)

vector1 = vectorize(word_frequencies(doc1_words), vocab)
vector2 = vectorize(word_frequencies(doc2_words), vocab)

print(cosine_similarity(vector1, vector2))