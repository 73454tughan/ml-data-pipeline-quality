# Dataset Schema & Quality Validation Report
**Audited Rows:** 48842  
**Audited Columns:** 15  
**Policy:** No rows were silently dropped. All anomalies recorded.

## 1. Value Ranges Audit
| Column | Allowed Range | Observed Min | Observed Max | Violations Count | Status |
|---|---|---|---|---|---|
| `age` | [17, 90] | 17.0 | 90.0 | 0 | PASSED |
| `hours-per-week` | [1, 99] | 1.0 | 99.0 | 0 | PASSED |
| `capital-gain` | [0, 99999] | 0.0 | 99999.0 | 0 | PASSED |
| `capital-loss` | [0, 4356] | 0.0 | 4356.0 | 0 | PASSED |

## 2. Missing Values & '?' Character Policy Audit
| Column | '?' Count | NaN Count | Total Missing | % of Dataset | Handled by Imputer |
|---|---|---|---|---|---|
| `workclass` | 0 | 2799 | 2799 | 5.73% | YES (Mode/Median) |
| `occupation` | 0 | 2809 | 2809 | 5.75% | YES (Mode/Median) |
| `native-country` | 0 | 857 | 857 | 1.75% | YES (Mode/Median) |

## 3. Policy Adherence Summary
* **Range Violations Total:** 0
* **Type Inconsistencies:** 0
* **Preservation Policy:** 100% of rows retained for downstream stratified splitting.
* **Missing Indicator:** Recognized `'?'` as valid placeholder requiring imputation.
