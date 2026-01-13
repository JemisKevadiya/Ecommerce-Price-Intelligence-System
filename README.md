# 🎓 End-to-End Machine Learning Project

## Student Exam Performance Indicator

This project implements a complete **Machine Learning pipeline** to predict **student exam performance** based on demographic and educational factors. It provides multiple interfaces to interact with the trained model, including **FastAPI** and **Streamlit**.

---

## 📁 Project Structure

```bash
mlproject-main/
├── src/                    # Source code for the ML pipeline
│   ├── components/         # Data ingestion, transformation, and model training
│   ├── pipeline/           # Training and inference pipelines
│   ├── exception.py        # Custom exception handling
│   ├── logger.py           # Logging configuration
│   └── utils.py            # Utility functions
├── artifacts/              # Saved models and preprocessors (.pkl files)
├── notebook/               # Jupyter notebooks for EDA & experiments
├── app.py                  # Flask web application
├── fastapi_app.py          # FastAPI web application
├── streamlit_app.py        # Streamlit dashboard
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup script
└── README.md               # Project documentation
```

---

## 🚀 Features

* **End-to-End ML Pipeline**
  Covers data ingestion, preprocessing, model training, evaluation, and prediction.

* **Data Preprocessing**

  * Missing value handling
  * One-hot encoding of categorical features (Gender, Parental Education, etc.)
  * Scaling of numerical features (Reading & Writing scores)

* **Model Training & Selection**
  Trains multiple regression models (CatBoost, XGBoost, Random Forest, etc.) and selects the best-performing model.

* **Multiple Web Interfaces**

  * **FastAPI**: High-performance REST API with auto-generated Swagger documentation
  * **Streamlit**: Interactive UI for quick testing and visualization

* **Robust Error Handling**
  Custom exception handling and logging for production readiness.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd mlproject-main
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔹 1. Run the FastAPI Application

The FastAPI app provides a REST API along with Swagger UI documentation.

```bash
python fastapi_app.py
```

* **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **API Base URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🔹 2. Run the Streamlit Application

The Streamlit app offers an interactive interface for predicting student exam scores.

```bash
streamlit run streamlit_app.py
```

* **Application URL**: [http://localhost:8501](http://localhost:8501)

---

## 🔄 Data Pipeline Details

### 📥 Data Ingestion

* Reads data from CSV or database
* Performs train-test split

### 🔧 Data Transformation

* Handles missing values
* One-hot encoding of categorical variables
* Feature scaling for numerical columns

### 🧠 Model Training

* Trains multiple regression models
* Evaluates performance using metrics
* Selects and saves the best model

### 📊 Prediction

* Loads `model.pkl` and `preprocessor.pkl`
* Generates predictions for new input data

---

## 📜 License

This project is licensed under the **MIT License**.

---

✨ *This project is suitable for learning, academic submission, and showcasing an end-to-end Machine Learning workflow in production-ready form.*
