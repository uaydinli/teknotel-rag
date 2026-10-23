#!/usr/bin/env python3
"""Minimal local full-text retrieval for the Teknotel evidence repository."""
import argparse
import json
import re
from pathlib import Path

SCAN_DIRS = ("docs", "evidence", "projects")
TOKEN = re.compile(r"[\w.-]+", re.UNICODE)


def tokenize(text: str) -> set[str]:
    return {word.lower() for word in TOKEN.findall(text) if len(word) > 1}


def search(root: Path, query: str, limit: int = 10) -> list[dict]:
    terms = tokenize(query)
    if not terms:
        return []
    results = []
    files = [root / "README.md"]
    for directory in SCAN_DIRS:
        folder = root / directory
        if folder.is_dir():
            files.extend(sorted(folder.rglob("*.md")))
    for path in files:
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines()
        heading = next((line.lstrip("# ").strip() for line in lines if line.startswith("# ")), relative)
        matches = []
        for number, line in enumerate(lines, 1):
            words = tokenize(line)
            overlap = terms & words
            if overlap:
                matches.append((len(overlap), number, line.strip()[:240]))
        if matches:
            matches.sort(key=lambda row: (-row[0], row[1]))
            results.append({"path": relative, "title": heading, "score": sum(x[0] for x in matches),
                            "snippets": [{"line": n, "text": text} for _, n, text in matches[:3]]})
    return sorted(results, key=lambda item: (-item["score"], item["path"]))[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search Teknotel RAG Markdown evidence")
    parser.add_argument("query", help="Text to search")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    print(json.dumps(search(args.root.resolve(), args.query, args.limit), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
