# ishkarim-bench

> **Infrastruktura benchmarkowa CPU-first — RAPL energia, FTS5 mikrotesty, BEIR evaluation**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Pomiar zużycia energii (mJ/query) przez Intel RAPL
- Reprodukowalne benchmarki FTS5 z seedowanymi danymi testowymi
- Ewaluacja retrieval quality (BEIR subset) lokalnie bez płatnych API

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-bench

# Demo (10 sekund)
python projects/ishkarim-bench/demo.py
```

## Użycie w kodzie

```python
import ishkarim_bench as m

# Wszystkie 34 katalogi wiedzy obszaru 'bench'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_bench.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Wybór między modelami embeddingów przy ograniczonym budżecie CPU/energii
- Uzasadnienie kosztu zużycia energii klientowi (SLA mJ/query)
- Regresja testów po zmianie tokenizera lub parametrów indeksu FTS5

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 34 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_bench.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_bench_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_bench.py --quick
```

## Struktura projektu

```
ishkarim-bench/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 34 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_bench/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_bench.py         ← testy jednostkowe
│   └── test_bench_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_bench.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 34 katalogów wiedzy obszaru `bench`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
