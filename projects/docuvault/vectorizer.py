from pathlib import Path
from typing import List
import string
import numpy as np


def clean_text(text: str) -> List[str]:
    lower_case_text = [t.lower() for t in text.split()]
    cleaned_list = []
    for word in lower_case_text:
        curr_word = ""
        for char in word:
            if char not in string.punctuation:
                curr_word += char
        if curr_word:
            cleaned_list.append(curr_word)
    return cleaned_list

def word_frequencies(words_list: list[str]) -> dict[str,int]:
    counter_dict = {}
    for word in words_list:
        if word not in counter_dict:
            counter_dict[word] = 1
        else:
            counter_dict[word] +=1

    return counter_dict

def build_vocabulary(all_cleaned_word_lists: list[list[str]]) -> list[str]:
    all_words = set()
    for word_list in all_cleaned_word_lists:
        all_words.update(word_list)
    return sorted(all_words)


def end_to_end_build_vocabulary(folder_path : Path) -> list[str]:
    combined_vocabulary_list = []
    for file in folder_path.iterdir():
        if file.is_file():
            with open(file,"r",encoding="utf-8") as f:
                content = f.read()
            cleaned_file_text = clean_text(content)
            combined_vocabulary_list.append(cleaned_file_text)

    return build_vocabulary(combined_vocabulary_list)

# doc1_words = clean_text("Hello, World! This is RAG.")
# doc2_words = clean_text("RAG is great for search")
# vocab = build_vocabulary([doc1_words, doc2_words])
# print(vocab)


# freq = word_frequencies(doc1_words)
# print(freq)

def vectorize(word_freq: dict[str, int], vocabulary: list[str]) -> np.ndarray:
    arr = [word_freq.get(word, 0) for word in vocabulary]
    return np.array(arr)

def cosine_similarity(vector1:np.ndarray, vector2 : np.ndarray) -> np.float64:
    similarity_score = vector1.dot(vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return similarity_score

# vector1 = vectorize(word_frequencies(doc1_words),vocab)
# vector2 = vectorize(word_frequencies(doc2_words),vocab)

# print(cosine_similarity(vector1,vector2))

