"""
benchmark.py — kod wyekstrahowany z WORK.md dla obszaru bench.

Zawiera 2 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Kwantyzacja i micro-benchmarking dla CPU
# Kwantyzacja dynamic INT8
from onnxruntime.quantization import quantize_dynamic, QuantType
quantize_dynamic(
    model_input="model.onnx",
    model_output="model-int8.onnx",
    op_types_to_quantize=["MatMul", "Gemm"],
    per_channel=True,
    reduce_range=False,
    weight_type=QuantType.QInt8,
    extra_options={"WeightSymmetric": True, "ActivationSymmetric": False}
)

# Micro-benchmark (p50/p95)
import time, numpy as np
lat = []
for t in texts:
    enc = tok(t, return_tensors="np", padding="max_length", truncation=True, max_length=128)
    t0 = time.perf_counter()
    sess.run(None, {inp_name: enc["input_ids"], att_name: enc["attention_mask"]})
    lat.append((time.perf_counter()-t0)*1000)
p50, p95 = np.median(lat), np.percentile(lat, 95)

# Jakość: cosine drift po L2-norm
def l2norm(x): return x / (np.linalg.norm(x, axis=1, keepdims=True) + 1e-12)
# porównaj hit@k między FP32 i INT8 na dev-korpusie

# Source: Pomiar energii CPU i ONNX Execution Providers
# Struktura modułu bench_energy
bench_energy/
  rapl.py          # RAPL zones + snapshot + wrap
  nvml_power.py    # NVML sampler + energia przez całkowanie
  ort_runner.py    # ORT session + benchmark iteracji
  stats.py         # percentyle p50/p95/MAD
  manifest.py      # zapis JSONL + walidacja schematu
  gates.py         # Gate-Perf / Gate-Energy / Gate-Stability
scripts/
  bench_onnx_energy.py  # główne CLI
  gate_run.py           # uruchom bramki na manifestach
