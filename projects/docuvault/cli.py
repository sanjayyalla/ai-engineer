import argparse
from pathlib import Path

from models import KnowledgeBase
from storage import save_knowledge_base, load_knowledge_base
from search import search
from logging_store import log_search, generate_report
from exceptions import EmptyKnowledgeBaseError

STORE_PATH = Path("kb_store.json")
LOG_PATH = Path("search_log.csv")


def cmd_ingest(args):
    kb = load_knowledge_base(STORE_PATH) if STORE_PATH.exists() else KnowledgeBase()
    kb.ingest_folder(Path(args.folder))
    save_knowledge_base(kb, STORE_PATH)
    print(f"Ingested folder '{args.folder}'. Knowledge base now has {len(kb.documents)} documents.")


def cmd_search(args):
    if not STORE_PATH.exists():
        print("No knowledge base found. Run 'ingest' first.")
        return
    kb = load_knowledge_base(STORE_PATH)
    try:
        results = search(kb, args.query, top_k=args.top_k)
    except EmptyKnowledgeBaseError as e:
        print(f"Error: {e}")
        return

    for doc_id, score in results:
        doc = kb.documents[doc_id]
        print(f"[{score:.4f}] {doc.title} (id={doc_id})")

    log_search(args.query, results, LOG_PATH)


def cmd_report(args):
    generate_report(LOG_PATH)


def main():
    parser = argparse.ArgumentParser(prog="docuvault")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest")
    ingest_parser.add_argument("folder")
    ingest_parser.set_defaults(func=cmd_ingest)

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--top_k", type=int, default=5)
    search_parser.set_defaults(func=cmd_search)

    report_parser = subparsers.add_parser("report")
    report_parser.set_defaults(func=cmd_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()