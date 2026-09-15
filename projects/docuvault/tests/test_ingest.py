from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from models import KnowledgeBase


def test_ingest_folder_overwrites_existing_documents(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "one.txt").write_text("alpha beta\n", encoding="utf-8")
    (docs_dir / "two.txt").write_text("beta gamma\n", encoding="utf-8")

    kb = KnowledgeBase()
    kb.ingest_folder(docs_dir)
    assert len(kb.documents) == 2

    kb.ingest_folder(docs_dir)

    assert len(kb.documents) == 2
    assert sorted(kb.documents.keys()) == [0, 1]
