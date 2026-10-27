# Lab 4: Machine Learning Data Pipeline & Quality Engineering
**Student:** Tughan Bulut Kurtulus  
**Student ID:** 73454  
**Course:** Advanced Machine Learning / Data Engineering  
**Environment:** Python 3.11, Scikit-Learn, Pandas  

---

## 📌 Executive Summary

This repository provides a modular, reproducible, and **leakage-free** data pipeline for the UCI Adult Census Income dataset (`fetch_openml(name='adult', version=2, as_frame=True)`). It implements comprehensive schema and range validation, zero-leakage preprocessing, outlier clipping, derived feature engineering, duplicate-conflict auditing, cryptographic SHA-256 dataset tracking, and automated baseline model benchmarking.

---

## 🏆 Deliverables & Graded Evidence Checklist

| Requirement | Artifact / Evidence | Status |
|---|---|---|
| **1. Problem Definition** | [`problem_definition.md`](problem_definition.md) | ✅ Complete |
| **2. Ingestion Step** | [`src/ingestion.py`](src/ingestion.py) (Logs: 48,842 rows, 15 columns) | ✅ Verified |
| **3. Schema Validation** | [`src/validation.py`](src/validation.py) & [`reports/validation_report.md`](reports/validation_report.md) | ✅ 0 rows silently dropped |
| **4. Leakage-Free Preprocessing** | [`src/transformation.py`](src/transformation.py) & `results/preprocessor.joblib` | ✅ 70/30 stratified, train-only fit |
| **5. Feature Engineering** | [`src/feature_engineering.py`](src/feature_engineering.py) (`capital_net`, `hours_per_age`) | ✅ Tested with LogisticRegression |
| **6. Label-Quality Audit** | [`src/label_audit.py`](src/label_audit.py) & [`reports/label_quality_report.md`](reports/label_quality_report.md) | ✅ 50-row audit & duplicate conflicts |
| **7. Data Card & Reproducibility** | [`data_card.md`](data_card.md) & [`config/config.yaml`](config/config.yaml) | ✅ SHA-256 hash stored |
| **One-Command Runner** | [`run_pipeline.py`](run_pipeline.py) | ✅ Single CLI invocation |

---

## ⚙️ Architecture & Pipeline Flow

```
[OpenML Adult Dataset] (48842 x 15)
         │
         ▼
[1. Ingestion] ───────────────► Logs row/col count without modification
         │
         ▼
[2. Validation Suite] ────────► Validates types, ranges [17-90, 1-99], null policy '?'
         │                     (Generates reports/validation_report.md)
         ▼
[3. Stratified 70/30 Split] ──► X_train (70%), X_test (30%) stratified on income
         │
         ├───► Train deduplication (exact duplicates dropped from TRAIN only)
         ├───► Fit Imputer (Categorical mode, Numeric median on TRAIN only)
         ├───► Compute Outlier Percentiles (1st & 99th on TRAIN only)
         ├───► Transform Train & Test (Apply train parameters strictly)
         └───► Serialize Transformer ──► results/preprocessor.joblib
         │
         ▼
[4. Feature Engineering] ─────► capital_net = capital-gain - capital-loss
         │                     hours_per_age = hours-per-week / (age - 16)
         │
         ▼
[5. Model Evaluation] ────────► Baseline LogisticRegression (WITH vs WITHOUT features)
         │                     (Accuracy & F1 scores logged to results/baseline_metrics.json)
         ▼
[6. Label Quality Audit] ─────► Conflicting duplicate labels audit (reports/label_quality_report.md)
         │
         ▼
[7. Cryptographic Hashing] ───► Computes SHA-256 of processed data, updates config/config.yaml
```

---

## 📊 Experimental Results: Feature Engineering Impact

| Model Configuration | Accuracy | F1-Score (Income >50K) | Precision | Recall |
|---|---|---|---|---|
| **Baseline (Without Derived Features)** | **0.8540** | **0.6601** | 0.7289 | 0.6033 |
| **Enhanced (With `capital_net` & `hours_per_age`)** | **0.8578** (+0.0038) | **0.6696** (+0.0095) | 0.7381 | 0.6127 |

> Both Accuracy and F1-score demonstrated empirical improvements upon introducing `capital_net` and `hours_per_age`.

---

## 🚀 How to Run the Pipeline (One Command)

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Execution
Run the complete pipeline with a single command:
```bash
python run_pipeline.py
```
All reports, serializations, and configurations will be automatically populated in `results/`, `reports/`, and `config/`.
