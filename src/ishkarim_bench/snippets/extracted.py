"""
extracted.py — fragmenty kodu z WORK.md dla obszaru bench.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 5 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Kalibracja energii CPU i Joule token_04
def diff_energy_j(start: EnergyReading, end: EnergyReading) -> float:
    maxr = min(start.max_range_uj, end.max_range_uj)
    if end.energy_uj >= start.energy_uj:
        diff_uj = end.energy_uj - start.energy_uj
    else:
        diff_uj = (maxr - start.energy_uj) + end.energy_uj
    return diff_uj / 1e6

# ────────────────────────────────────────────────────────────

# Source: Kalibracja wysokości budynków: GBA vs M4Heights
# Protokół kalibracji
sample = gba_query(bbox=region, n=500)
reference = m4heights_lookup(sample.ids)
bias = (sample.height - reference.height).mean()
rmse = sqrt(((sample.height - reference.height)**2).mean())
# Próg: |bias| < 2m AND RMSE < 5m → GBA nadaje się do LoD1

# ────────────────────────────────────────────────────────────

# Source: New tools for local CPU energy
if e_per_unit > baseline * 1.05 and wall_s_delta >= -0.03: → FAIL
if wall_s > baseline_wall * 1.03: → WARN
if tdie_trend_up or avg_mhz_trend_down: → "thermally unstable", odrzuć jako baseline

# ────────────────────────────────────────────────────────────

# Source: Nowe pomiary CPU - iGPU i aktualne testy
pipe = openvino_genai.LLMPipeline("model.F16.gguf", "CPU")
pipe.enable_save_ov_model = True
out = pipe.generate("prompt", config)

# ────────────────────────────────────────────────────────────

# Source: Repozytoria CPU-first do pomiaru energii na token
def read_energy_uj(domain_path):
    e = int(open(f"{domain_path}/energy_uj").read())
    max_e = int(open(f"{domain_path}/max_energy_range_uj").read())
    return e, max_e

def delta_energy(e0, e1, max_e):
    return (e1 - e0) if e1 >= e0 else (max_e - e0 + e1)
