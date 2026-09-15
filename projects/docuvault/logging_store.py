from pathlib import Path
from datetime import datetime
import pandas as pd


def log_search(query: str, results: list[tuple[int, float]], log_path: Path) -> None:
    """Logs one row per result returned by a search."""
    rows = [
        {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "doc_id": doc_id,
            "score": score,
        }
        for doc_id, score in results
    ]
    df = pd.DataFrame(rows)

    if log_path.exists():
        df.to_csv(log_path, mode="a", header=False, index=False)
    else:
        df.to_csv(log_path, mode="w", header=True, index=False)


def generate_report(log_path: Path) -> None:
    if not log_path.exists():
        print("No searches logged yet.")
        return

    df = pd.read_csv(log_path)

    print(f"Total searches logged (rows): {len(df)}")
    print(f"Unique queries: {df['query'].nunique()}")
    print(f"Average score: {df['score'].mean():.4f}")
    print("\nTop 5 highest-scoring results:")
    print(df.sort_values("score", ascending=False).head(5).to_string(index=False))

    print("\nMost frequently retrieved documents:")
    print(df.groupby("doc_id")["score"].agg(["count", "mean"]).sort_values("count", ascending=False).head(5))