from pathlib import Path
import numpy as np

from exceptions import EmptyKnowledgeBaseError
class Document:
    def  __init__(self, doc_id: int , title : str , content : str , source_path: Path): 
        self.doc_id = doc_id
        self.title= title
        self.content = content
        self.source_path = source_path

    def __repr__(self):
        # return (f"This file title is {self.title} and the overview of content is {self.content[:20]}")
        return f"Document(doc_id={self.doc_id}, title={self.title!r}, content={self.content[:20]!r}...)"

    # def __len__(self):
    #     return len(self.content)

    def __len__(self):
        # with open(self.source_path) as file:
        #     res = file.read()
        return len(self.content.split())



class KnowledgeBase:

    def __init__(self):
        self.documents : dict[int, Document] = {}
        self.vocabulary : list[str] = []
        self.vectors : dict[int,np.ndarray] = {}

    def ingest_folder(self, folder_path : Path) -> None:
        path = Path(folder_path)
        self.documents = {}
        self.vocabulary = []
        self.vectors = {}

        for file in sorted(path.iterdir(), key=lambda p: p.name):
            if file.is_file() and file.suffix == ".txt":
                with open(file,"r",encoding="utf-8") as f:
                    content = f.read()

                title = file.stem
                doc_id = len(self.documents)
                source_path = file.absolute()
                document = Document(doc_id,title, content,source_path)
                self.documents[doc_id] = document
        self.vectorize_documents()

    # def vectorize_documents(self):
    #     from vectorizer import clean_text, build_vocabulary, word_frequencies, vectorize

    #     combined_cleaned_list = []

    #     for docs in self.documents.values():
    #         cleaned_list = clean_text(docs.content)
    #         combined_cleaned_list.append(cleaned_list)

    #     combined_vocabulary = build_vocabulary(combined_cleaned_list)

    #     self.vocabulary = combined_vocabulary

    #     for docs in self.documents.values():
    #         self.vectors[docs.doc_id] = vectorize(word_frequencies(combined_cleaned_list[docs.doc_id]),combined_vocabulary)

    def vectorize_documents(self):
        if not self.documents:
            raise EmptyKnowledgeBaseError("There are no documents in the KnowledgeBaseS")
        from vectorizer import clean_text , build_vocabulary , word_frequencies , vectorize
        cleaned_by_id = {doc_id : clean_text(doc.content) for doc_id, doc in self.documents.items()}
        self.vocabulary = build_vocabulary(list(cleaned_by_id.values()))

        for doc_id, cleaned_words in cleaned_by_id.items():
            self.vectors[doc_id] = vectorize(word_frequencies(cleaned_words), self.vocabulary)


kb = KnowledgeBase()

kb.ingest_folder("docs")

print(kb.documents)
print(kb.vectors)