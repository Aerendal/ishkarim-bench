#!/usr/bin/env python3
"""
demo.py — demo ishkarim-bench

Infrastruktura benchmarkowa CPU-first — RAPL energia, FTS5 mikrotesty, BEIR evaluation

Uruchomienie:
    python projects/ishkarim-bench/demo.py
"""
import sys, pathlib, time
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_bench as m

docs = m.load_knowledge_index()
from ishkarim_bench.utils import extract_tags

# Micro-benchmark: czas parsowania TAGS.md
t0 = time.perf_counter()
for doc in docs[:20]:
    extract_tags(pathlib.Path(__file__).parents[2] / doc["name"])
elapsed = time.perf_counter() - t0

print(f"Benchmark: ishkarim-bench")
print(f"  katalogi:        {len(docs)}")
print(f"  parse 20 TAGS:   {elapsed*1000:.2f} ms")
print(f"  per katalog:     {elapsed/20*1000:.3f} ms")
print(f"\nUruchom pełny benchmark: python benchmarks/bench_bench.py")

