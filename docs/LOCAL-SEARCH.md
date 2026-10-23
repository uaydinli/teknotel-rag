# Local Markdown retrieval

Prerequisite: Python 3.10+ (standard library only; no third-party dependencies).

```bash
python3 tools/rag_search.py "speedtest"
python3 tools/rag_search.py "looking glass" --limit 5
```

The CLI searches `README.md` and Markdown documents in `docs/`, `evidence/` and `projects/`. Output is UTF-8 JSON containing file path, title, simple token-match score and line-numbered excerpts. It is a deterministic lexical retrieval baseline, **not** semantic vector search or an LLM answer generator. Evidence labels must be interpreted from the source document; search scores are not confidence scores.
