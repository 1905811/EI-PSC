import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from parsers.paper_parser import parse_paper


def run_test():
    text = """High Efficiency Perovskite Solar Cells

DOI: 10.1039/D5EE01234A

This is the abstract.
"""

    paper = parse_paper(text)

    print("Title:", paper.title)
    print("DOI:", paper.doi)
    print("Full text:", paper.full_text)


if __name__ == "__main__":
    run_test()