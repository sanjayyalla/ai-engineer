from models import Document
from pathlib import Path
current_dir = Path(__file__).resolve().parent
print(current_dir)
path1 = Path("docs\python_book.txt")
print(path1)
doc1 = Document(1, "Python Programming", "This is a Python programming book",source_path=path1 )
print(doc1)
print(len(doc1))