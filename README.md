# Heart Disease Prediction System

A binary classification model that predicts heart disease risk from patient
health data using Logistic Regression, with an interactive Streamlit app for
real-time predictions.

---

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Approach](#approach)
- [Results](#results)
- [Web App](#web-app)
- [How to Run](#how-to-run)
- [Future Scope](#future-scope)

---

## Overview
Early identification of heart disease risk can support timely medical
intervention. This project trains a Logistic Regression classifier on 13
clinical features (age, blood pressure, cholesterol, ECG results, etc.) to
predict the presence of heart disease, then wraps the trained model in a
Streamlit web app so a user can enter their own values and get an instant
prediction.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn
- **Model:** Logistic Regression
- **Deployment:** Streamlit
- **Model persistence:** Pickle (`.sav`)

## Dataset
- **Records:** 303 patients, 13 features + 1 target label
- **Target distribution:** 165 positive (heart disease) / 138 negative (healthy) — no missing values
- **Features:** age, sex, cp (chest pain type), trestbps (resting blood pressure), chol (serum cholesterol), fbs (fasting blood sugar), restecg (resting ECG), thalach (max heart rate), exang (exercise-induced angina), oldpeak (ST depression), slope, ca (major vessels colored), thal (thalassemia)
- **Target:** 1 = heart disease present, 0 = healthy

## Approach
1. **Data loading & validation** — loaded the CSV and confirmed no missing values across all 303 records
2. **Train/test split** — 80/20 stratified split (242 training samples, 61 test samples) to preserve class balance
3. **Model training** — trained a Logistic Regression classifier on the training set
4. **Evaluation** — measured accuracy on both training and held-out test data

## Results
| Metric | Score |
|---|---|
| Training accuracy | 85.1% |
| Test accuracy | 82.0% |

The close gap between training and test accuracy (85.1% vs. 82.0%) indicates the
model generalizes reasonably well without significant overfitting.

## Web App
A Streamlit interface (`streamlit_app.py`) lets a user enter their own clinical
values — age, blood pressure, cholesterol, ECG results, and more — across a
two-column form and get an instant prediction with a clear visual result (✅
healthy / ⚠️ at risk).

```bash
streamlit run streamlit_app.py
```

## How to Run
```bash
pip install pandas numpy scikit-learn streamlit

# Train the model (or use the pre-trained heart_disease_model.sav)
jupyter notebook Heart_Disease_Prediction.ipynb

# Launch the web app
streamlit run streamlit_app.py
```

## Future Scope
- Compare Logistic Regression against ensemble models (Random Forest, XGBoost)
  to see if test accuracy improves beyond 82%
- Increase `max_iter` in LogisticRegression and scale features (the current
  model raises a convergence warning at the default 100 iterations)
- Add cross-validation for a more robust performance estimate than a single
  train/test split
- Add feature importance / coefficient visualization to the Streamlit app for
  interpretability
