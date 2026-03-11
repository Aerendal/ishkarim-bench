# ishkarim-bench

> Benchmarki CPU-first: FTS5 mikro-testy, RAPL energia, BEIR, retrieval harness.

## Instalacja

```bash
pip install -e projects/ishkarim-bench
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-bench
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_bench as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **34 katalogów** obszaru `bench`:

- `Algorytmy giełdowe CPU‑friendly i OSS`
- `Algorytmy giełdowe w trybie edukacyjnym`
- `Analiza Strix narzędzia`
- `Backtesting i ryzyko: algotrading na CPU`
- `Benchmark APEX‑Agents: AI w biurze nie daje rady`
- `Benchmarking CPU dla lokalnych modeli`
- `Edukacyjne backtesty strategii giełdowych`
- `Eksperyment CPU↔GPU-analiza energii (luty 2026)`
- … i 26 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### Algorytmy giełdowe CPU‑friendly i OSS

# WORK: Algorytmy giełdowe CPU‑friendly i OSS
## 0-Metadane
- Katalog: Algorytmy giełdowe CPU‑friendly i OSS
- Pliki: 22 (bez placeholderów: część 1–22)
- Tagi: backtesting, algorytmy-giełdowe, momentum, mean-reversion, pair-trading, Risk-Parity, HRP, walk-forward, event-driven, CPU-only, OSS, offline, deterministyczny, audit

### Algorytmy giełdowe w trybie edukacyjnym

# WORK: Algorytmy giełdowe w trybie edukacyjnym
## 0-Metadane
- Katalog: Algorytmy giełdowe w trybie edukacyjnym
- Pliki: 22 (bez placeholderów: część 1–23 z jednym plikiem 0-bajtowym)
- Tagi: backtesting-edukacyjny, event-driven, look-ahead-bias, survivorship-bias, OHLCV, data-contract, strategy-API, order-management, execution-model, portfolio-accounting, risk-management, btctl-CLI, offline, deterministyczny, audit

### Analiza Strix narzędzia

# WORK — Analiza Strix narzędzia
## 0-Metadane
- **Ścieżka:** Analiza Strix narzędzia/
- **Liczba plików:** 7/30 z treścią (Cz8–Cz30 puste — 0 bajtów)
- **Tagi:** strix pentest ai-agent architektura c4-model dokumentacja semantic-markers analiza-kodu security idor sql-injection knowledge-system archscan


## Struktura projektu

```
ishkarim-bench/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 34 katalogów-źródeł
├── src/
│   └── ishkarim_bench/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_bench.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-bench/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
