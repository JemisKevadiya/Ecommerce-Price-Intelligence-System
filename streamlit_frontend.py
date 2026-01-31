import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align: center;'>🎓 Student Exam Performance Indicator</h1>
    <p style='text-align: center; font-size:18px;'>
        Predict a student's <b>Math Score</b> using demographic & academic data
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- FORM + RESULTS LAYOUT ----------------
col1, col2 = st.columns([1.2, 1])

# ================= LEFT COLUMN (FORM) =================
with col1:
    st.subheader("📝 Enter Student Details")

    with st.form("prediction_form"):
        gender = st.selectbox("Gender", ["male", "female"])

        ethnicity = st.selectbox(
            "Race / Ethnicity",
            ["group A", "group B", "group C", "group D", "group E"]
        )

        parental_level_of_education = st.selectbox(
            "Parental Level of Education",
            [
                "associate's degree",
                "bachelor's degree",
                "high school",
                "master's degree",
                "some college",
                "some high school"
            ]
        )

        lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])

        test_preparation_course = st.selectbox(
            "Test Preparation Course",
            ["none", "completed"]
        )

        reading_score = st.slider("Reading Score", 0, 100, 50)
        writing_score = st.slider("Writing Score", 0, 100, 50)

        submit = st.form_submit_button("🔮 Predict Math Score")

# ================= RIGHT COLUMN (RESULTS) =================
with col2:
    st.subheader("📊 Prediction Result")

    if submit:
        payload = {
            "gender": gender,
            "ethnicity": ethnicity,
            "parental_level_of_education": parental_level_of_education,
            "lunch": lunch,
            "test_preparation_course": test_preparation_course,
            "reading_score": reading_score,
            "writing_score": writing_score
        }

        try:
            with st.spinner("Predicting performance..."):
                time.sleep(1.2)  # UX smoothness
                response = requests.post(
                    "http://127.0.0.1:5000/predict_api",
                    data=payload
                )

            if response.status_code == 200:
                prediction = response.json()["prediction"]

                # ---------- Performance Category ----------
                if prediction < 40:
                    level = "Poor 😟"
                    color = "red"
                elif prediction < 60:
                    level = "Average 😐"
                    color = "orange"
                elif prediction < 80:
                    level = "Good 🙂"
                    color = "green"
                else:
                    level = "Excellent 🌟"
                    color = "darkgreen"

                # ---------- METRIC CARDS ----------
                m1, m2 = st.columns(2)
                m1.metric("📘 Predicted Math Score", f"{prediction:.2f}")
                m2.metric("🏆 Performance Level", level)

                st.divider()

                # ---------- BAR / GAUGE CHART ----------
                df = pd.DataFrame({
                    "Score Type": ["Predicted Math Score"],
                    "Score": [prediction]
                })

                fig, ax = plt.subplots()
                ax.barh(df["Score Type"], df["Score"])
                ax.set_xlim(0, 100)
                ax.set_xlabel("Score")
                ax.set_title("Math Score Visualization")

                st.pyplot(fig)

            else:
                st.error(f"Prediction failed ❌: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("❌ Flask server is not running!")

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    "<p style='text-align:center;'>Built with ❤️ using Flask & Streamlit</p>",
    unsafe_allow_html=True
)
