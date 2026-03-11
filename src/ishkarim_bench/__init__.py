"""
ishkarim_bench — moduł z obszaru bench.

Benchmarki CPU-first: FTS5 mikro-testy, RAPL energia, BEIR, retrieval harness.

Źródła: 34 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "bench"



MODULES: list[str] = [
    'Algorytmy giełdowe CPU‑friendly i OSS',
    'Algorytmy giełdowe w trybie edukacyjnym',
    'Analiza Strix narzędzia',
    'Backtesting i ryzyko: algotrading na CPU',
    'Benchmark APEX‑Agents: AI w biurze nie daje rady',
    'Benchmarking CPU dla lokalnych modeli',
    'Edukacyjne backtesty strategii giełdowych',
    'Eksperyment CPU↔GPU-analiza energii (luty 2026)',
    'Eksperyment z pojedynczym zadaniem',
    'Godot 4.6: wydanie stabilne i dopracowane',
    'Kalibracja energii CPU i Joule token_04',
    'Kalibracja wysokości budynków: GBA vs M4Heights',
    'Kwantyzacja i micro-benchmarking dla CPU',
    'Local CPU benchmarking: tools & methods',
    'Lokalne AI działające wyłącznie na CPU',
    'Luty 2026: CPU↔GPU i efektywność energetyczna',
    'Narzędzia i metody pomiaru CPU',
    'New survey: CPU-only AGI trends',
    'New tools for local CPU energy',
    'Nowe CPU przyjazne AI bez GPU',
    'Nowe narzędzia do lokalnych pomiarów CPU',
    'Nowe narzędzia i benchmarki CPU',
    'Nowe pomiary CPU - iGPU i aktualne testy',
    'Ograniczona indukcja schematów: ścieżka audytowalna',
    'Pomiar energii CPU i ONNX Execution Providers',
    'Pomiar energii CPU i TTFT w CI z pyRAPL i vLLM',
    'Pomiar pamięci i energii: Faiss, PipeANN, cuda‑membench',
    'Przegląd narzędzi do indukcji schematów (2026)',
    'RFC test dokumentu obciążeniowego',
    'Rekord - replay — rr i kontenery audytowe',
    'Repozytoria CPU-first do pomiaru energii na token',
    'Samsung rusza z produkcją HBM4 dla Nvidii',
    'Scheduler Steam Decka w centrach danych Meta',
    'Zbiór M4Heights do szacowania wysokości budynków',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "bench"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
