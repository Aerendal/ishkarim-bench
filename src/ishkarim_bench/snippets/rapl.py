"""
rapl.py — fragmenty kodu z WORK.md dla obszaru bench.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 4 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Luty 2026: CPU↔GPU i efektywność energetyczna
e0 = rapl_read_joules()   # {zone: joules}
result = fn()              # prefill() lub decode()
e1 = rapl_read_joules()
delta = {k: e1[k]-e0[k] for k in e0 if k in e1}

# ────────────────────────────────────────────────────────────

# Source: Nowe narzędzia do lokalnych pomiarów CPU
# Odczytaj energy_uj, obsłuż przepełnienie przez max_energy_range_uj
e1 = int(open('/sys/class/powercap/intel-rapl:0/energy_uj').read())
# ... uruchom zadanie ...
e2 = int(open('/sys/class/powercap/intel-rapl:0/energy_uj').read())
joules = (e2 - e1) / 1e6  # z korekcją wrap-around gdy e2 < e1

# ────────────────────────────────────────────────────────────

# Source: Pomiar energii CPU i ONNX Execution Providers
# Obsługa wrap licznika RAPL
def delta_energy_uj(e0, e1, max_range):
    if e1 >= e0:
        return e1 - e0
    if max_range:
        return (max_range - e0) + e1
    raise ValueError("wrap bez max_energy_range_uj")

# ────────────────────────────────────────────────────────────

# Source: Pomiar energii CPU i ONNX Execution Providers
# Wykrywanie stref RAPL
for z in sorted(SYS_POWERCAP.glob("intel-rapl:*")):
    name_f, energy_f = z / "name", z / "energy_uj"
    if name_f.exists() and energy_f.exists():
        zones.append(RaplZone(path=z, name=name_f.read_text().strip(), ...))
