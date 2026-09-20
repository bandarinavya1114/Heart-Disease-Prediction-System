# Heart-Disease-Prediction-System
Binary classification model (Logistic Regression) predicting heart disease risk from patient health data, with a focus on preprocessing and feature engineering.
# Heart Disease Prediction System

A binary classification model that predicts heart disease risk from patient
health data using Logistic Regression.

---

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Approach](#approach)
- [Results](#results)
- [How to Run](#how-to-run)
- [Future Scope](#future-scope)

---

## Overview
Early identification of heart disease risk can support timely medical
intervention. This project builds a binary classifier to predict whether a
patient is at risk of heart disease, based on structured health data such as
age, blood pressure, cholesterol, and other clinical indicators. The focus was
on how data cleaning and feature engineering — not just model choice — improve
prediction reliability.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn
- **Model:** Logistic Regression

## Dataset
<!-- Fill in: dataset name/source (e.g. UCI Heart Disease Dataset), number of
records, and the features used. -->
- **Source:** _[add dataset name/link]_
- **Records:** _[add sample size]_
- **Features:** _[e.g. age, sex, chest pain type, resting BP, cholesterol, fasting blood sugar, max heart rate, etc.]_
- **Target:** Presence (1) or absence (0) of heart disease

## Approach
1. **Data cleaning** — handled missing values and inconsistent entries
2. **Feature engineering** — selected and transformed features most predictive
   of heart disease risk
3. **Model training** — trained a Logistic Regression classifier on the
   processed dataset
4. **Evaluation** — assessed model performance and iterated on preprocessing
   to improve reliability

## Results
<!-- Fill in your actual numbers here — this is the single most valuable part
of the README for a recruiter skimming it. -->
- **Accuracy:** _[add %]_
- **Precision / Recall / F1-score:** _[add if available]_
- Key takeaway: _[e.g. "Feature engineering improved accuracy by X% over the baseline model"]_

## How to Run
```bash
pip install pandas numpy scikit-learn
python heart_disease_prediction.py
```
<!-- Adjust filename/command to match your actual script -->

## Future Scope
- Compare Logistic Regression against ensemble models (Random Forest, XGBoost)
  for improved accuracy
- Add cross-validation for more robust performance estimates
- Deploy as a simple web app (e.g. Flask) for interactive risk prediction
