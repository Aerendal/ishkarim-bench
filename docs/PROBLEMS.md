# PROBLEMS — ishkarim-bench

> Infrastruktura benchmarkowa CPU-first — RAPL energia, FTS5 mikrotesty, BEIR evaluation

## ✅ Co ten projekt rozwiązuje

- ✅ Pomiar zużycia energii (mJ/query) przez Intel RAPL **bez GPU**
- ✅ Reprodukowalne benchmarki FTS5 z seedowanymi danymi testowymi
- ✅ Ewaluacja retrieval quality (BEIR subset) lokalnie bez płatnych API
- ✅ Porównanie wariantów: BM25 vs dense vs hybrid z identycznym harnesem
- ✅ CI-friendly benchmarki z progami jakości — test fails jeśli latencja > threshold

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Benchmarki GPU — skupione wyłącznie na CPU/iGPU (Intel/AMD)
- ❌ Distributed benchmarking — single-node only
- ❌ Automatyczne wykrywanie regresji wydajności w CI bez dodatkowej konfiguracji
- ❌ Benchmarki modeli zamkniętych (GPT-4, Claude) — tylko lokalne/open-source

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **RAPL dostęp** wymaga roota lub `perf_event_paranoid=0` — może być zablokowany przez IT
- ⚠️ **Thermal throttling CPU** wpływa na wyniki — brak automatycznej normalizacji
- ⚠️ **BEIR mini-subset** nie jest w pełni reprezentatywny dla wszystkich dziedzin
- ⚠️ **Brak testów statystycznych** istotności różnic — p-value nie jest obliczane

---

## 🎯 Przypadki użycia

- 🎯 Wybór między modelami embeddingów przy ograniczonym budżecie CPU/energii
- 🎯 Uzasadnienie kosztu zużycia energii klientowi (SLA mJ/query)
- 🎯 Regresja testów po zmianie tokenizera lub parametrów indeksu FTS5
- 🎯 Raport porównawczy dla stakeholderów: 'nasz system vs alternatywy'

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
