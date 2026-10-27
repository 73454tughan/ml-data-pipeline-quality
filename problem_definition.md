# Problem Definition: Adult Census Income Prediction Pipeline

**Student:** Tughan Bulut Kurtulus (Student ID: 73454)  
**Dataset:** UCI Adult Dataset (OpenML ID: adult, version: 2)  
**Task Type:** Supervised Binary Classification / Tabular Data Engineering  

---

### 1. Business & Technical Objective
The primary goal of this machine learning system is to accurately predict whether an individual's annual income exceeds $50,000 USD (`income > 50K`) based on 1994 United States Census Bureau survey data. From a socioeconomic and public policy perspective, such predictive models support targeted social assistance, economic mobility research, and demographic wage gap analysis.

### 2. Input Features & Target Variable
* **Inputs (14 Features):**
  * **Numerical (6):** `age` (continuous), `fnlwgt` (final sampling weight), `education-num` (years of education), `capital-gain` (monetary capital gains), `capital-loss` (monetary capital losses), `hours-per-week` (weekly work hours).
  * **Categorical (8):** `workclass` (employment sector), `education` (highest educational attainment), `marital-status` (civil status), `occupation` (job role), `relationship` (familial role), `race` (ethnic demographic), `sex` (biological sex), `native-country` (country of origin).
* **Target Output:**
  * Binary variable: `income > 50K` (Positive class `1`: income > $50K; Negative class `0`: income <= $50K).

### 3. Success Metrics & Justification
* **Primary Metric (F1-Score - Positive Class):** The dataset exhibits a substantial class imbalance: approximately 75.9% of instances earn `<=50K` and only 24.1% earn `>50K`. A trivial majority-class classifier achieves nearly 76% accuracy while providing zero utility for identifying high-income earners. Therefore, the harmonic mean of precision and recall (**F1-score**) is our primary evaluation criterion.
* **Secondary Metric (Classification Accuracy):** Tracks overall correctness across both classes.

### 4. Operational & Engineering Constraints
1. **Strict Zero-Leakage Guarantee:** Preprocessing steps (missing value imputation parameters, outlier clipping boundaries, categorical frequency mappings, numerical feature scalers) must be learned **strictly from the training partition (70%)** and applied downstream to the test set (30%).
2. **Reproducible Pipeline:** All stochastic operations (train/test stratification, cross-validation, baseline modeling) are governed by pinned pseudo-random seeds. Pipeline configuration is centralized in `config.yaml`, and data integrity is cryptographically guaranteed via SHA-256 hashing.
3. **No Silent Row Drops:** Ingestion and validation must log all anomalies and missingness without silently altering sample distributions before the stratified train/test split.
