"""
metric.py — fragmenty kodu z WORK.md dla obszaru bench.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 1 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Edukacyjne backtesty strategii giełdowych
for strategy in [MOM, MR]:
    for (train, test) in rolling_splits(prices, train_years=3, test_years=1):
        best_cfg = argmax_over_grid(cfgs, equity(train, strategy, cfg))
        test_curve = equity(test, strategy, best_cfg)
        results.append(metrics(test_curve))
