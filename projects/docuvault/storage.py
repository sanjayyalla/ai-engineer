
import numpy as np
from pathlib import Path
import json
from models import Document, KnowledgeBase


def knowledge_base_to_dict(kb: KnowledgeBase) -> dict:
    documents_dict = {
        doc_id: document_to_dict(document)
        for doc_id, document in kb.documents.items()
    }
    vectors_dict = {
        doc_id: vector.tolist()
        for doc_id, vector in kb.vectors.items()
    }
    return {
        "documents": documents_dict,
        "vocabulary": kb.vocabulary,
        "vectors": vectors_dict,
    }


def document_to_dict(doc: Document) -> dict:
    return {
        "doc_id": doc.doc_id,
        "title": doc.title,
        "content": doc.content,
        "source_path": str(doc.source_path),
    }


def save_knowledge_base(kb: KnowledgeBase, path: Path) -> None:
    knowledge_base_dict = knowledge_base_to_dict(kb)
    with open(path, "w") as f:
        json.dump(knowledge_base_dict, f, indent=2)


def load_knowledge_base(path: Path) -> KnowledgeBase:
    kb = KnowledgeBase()

    with open(path, "r") as f:
        content = json.load(f)

    kb.vocabulary = content.get("vocabulary", [])
    kb.documents = {
        int(doc_id): Document(
            doc_id=int(document["doc_id"]),
            title=document["title"],
            content=document["content"],
            source_path=Path(document["source_path"]),
        )
        for doc_id, document in content.get("documents", {}).items()
    }

    kb.vectors = {
        int(doc_id): np.array(vector)
        for doc_id, vector in content.get("vectors", {}).items()
    }

    return kb
