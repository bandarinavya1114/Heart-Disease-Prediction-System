import streamlit as st
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓", layout="centered")

# Title and intro
st.title("💓 Heart Disease Prediction App")
st.write("Provide your medical details below to predict heart disease risk.")

# ---- Input fields in two columns ----
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="small-subheader">Age</div>', unsafe_allow_html=True)
    age = st.number_input('Enter Age', min_value=1, max_value=120, value=40, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Sex</div>', unsafe_allow_html=True)
    sex = st.selectbox('Select Gender', ['Male', 'Female'], label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Chest Pain Type (0–3)</div>', unsafe_allow_html=True)
    cp = st.number_input('Enter Chest Pain Type', 0, 3, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Resting Blood Pressure (mm Hg)</div>', unsafe_allow_html=True)
    trestbps = st.number_input('Enter Resting BP', 80, 200, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Serum Cholesterol (mg/dl)</div>', unsafe_allow_html=True)
    chol = st.number_input('Enter Cholesterol Level', 100, 600, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Fasting Blood Sugar > 120 mg/dl?</div>', unsafe_allow_html=True)
    fbs = st.selectbox('Fasting Blood Sugar', ['No', 'Yes'], label_visibility="collapsed")

with col2:
    st.markdown('<div class="small-subheader">Resting ECG Results (0–2)</div>', unsafe_allow_html=True)
    restecg = st.number_input('Enter Resting ECG Result', 0, 2, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Maximum Heart Rate Achieved</div>', unsafe_allow_html=True)
    thalach = st.number_input('Enter Max Heart Rate', 60, 250, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Exercise Induced Angina?</div>', unsafe_allow_html=True)
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'], label_visibility="collapsed")

    st.markdown('<div class="small-subheader">ST Depression (Oldpeak)</div>', unsafe_allow_html=True)
    oldpeak = st.number_input('Enter ST Depression', 0.0, 10.0, step=0.1, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Slope of ST Segment (0–2)</div>', unsafe_allow_html=True)
    slope = st.number_input('Enter Slope Value', 0, 2, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Major Vessels Colored (0–4)</div>', unsafe_allow_html=True)
    ca = st.number_input('Enter Major Vessels', 0, 4, label_visibility="collapsed")

    st.markdown('<div class="small-subheader">Thalassemia (1–3)</div>', unsafe_allow_html=True)
    thal = st.number_input('Enter Thalassemia Value', 1, 3, label_visibility="collapsed")
# ---- Convert categorical values ----
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'Yes' else 0
exang = 1 if exang == 'Yes' else 0

# ---- Prediction Function ----
def predict_heart_disease(data):
    input_data = np.asarray(data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return int(prediction[0])

# ---- Predict Button ----
st.markdown("---")
if st.button('💡 Predict Heart Disease'):
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal]
    result = predict_heart_disease(user_input)

    if result == 0:
        st.markdown('<div class="flying-icon">❤️</div>', unsafe_allow_html=True)
        st.success("✅ The person does **not** have heart disease.")
    else:
        st.markdown('<div class="flying-icon">💔</div>', unsafe_allow_html=True)
        st.error("⚠️ The person **has** heart disease.")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Logistic Regression Model")
