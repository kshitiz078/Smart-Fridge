# Smart-Fridge
A Streamlit-powered ML app that predicts food spoilage risk based on storage type, purchase timing, and item category.

# 🧊 Smart Fridge – Food Expiry Predictor

An intelligent ML-powered application that predicts whether stored food items will be used before they expire, helping reduce food waste. Built with **scikit-learn**, deployed using **Streamlit**.

---

## 📊 Problem Statement

Many households throw away food simply because they forget expiry dates. This project predicts the likelihood of spoilage based on:
- Item type
- Storage environment
- Purchase timing
- Quantity and shelf life

---

## 🚀 Features

- Logistic Regression model trained on synthetic food expiry dataset
- Encodes categorical variables (item type & storage type)
- Interactive web UI built with **Streamlit**
- Predicts if a food item is likely to be wasted or used in time

---

## 🧠 Technologies Used

| Purpose               | Tools                  |
|-----------------------|------------------------|
| Model Training        | scikit-learn, pandas   |
| UI / Deployment       | Streamlit              |
| Serialization         | joblib                 |
| Visualization & EDA   | Matplotlib, Seaborn    |

---

## 📂 Project Structure

smart-fridge-expiry-predictor/

├── project3.ipynb ← Model training + EDA

├── app.py ← Streamlit web app

├── model.pkl ← Trained model file

├── food_expiry_tracker.csv.xls ← Dataset

├── requirements.txt

├── LICENSE

└── README.md


---

## 📦 Installation

```bash
git clone https://github.com/yourusername/smart-fridge-expiry-predictor.git
cd smart-fridge-expiry-predictor
pip install -r requirements.txt
streamlit run app.py

```
