from exceptions import EmptyKnowledgeBaseError
from decorators import timer
from vectorizer import clean_text, cosine_similarity, vectorize, word_frequencies
from models import KnowledgeBase

@timer
def search(kb : KnowledgeBase , query_string : str, top_k: int = 5) -> list[tuple[int, float]]:

    if not kb.vectors or not kb.vocabulary:
            raise EmptyKnowledgeBaseError("Cannot search an empty knowledge base.")
    
    query_word_freq = word_frequencies(clean_text(query_string))
    
    query_vector = vectorize(query_word_freq,kb.vocabulary)
    similarity_vector = []
    for doc_id,vector in kb.vectors.items():
        similarity_vector.append((doc_id, cosine_similarity(query_vector,vector)))

    return sorted(similarity_vector, key = lambda pair : pair[1], reverse=True )[:top_k]

