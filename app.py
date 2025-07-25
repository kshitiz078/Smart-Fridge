import streamlit as st
import numpy as np
import joblib
import pandas as pd

st.title("🧊 Smart Fridge - Food Expiry Predictor")

model = joblib.load("model.pkl")
st.success("Model loaded successfully")

# Input fields
purchase_month = st.slider("Purchase Month (0=Jan, 1=Feb, ..., 11=Dec)", 0, 11, 0) / 11
purchase_day = st.slider("Day of the Week (0=Sun, ..., 6=Sat)", 0, 6, 0) / 6
quantity = st.slider("Quantity Bought", 1, 5, 1) / 5
days_until_expiry = st.slider("Days Until Expiry", 1, 30, 7) / 30

st.subheader("Item Category")
item_options = ['item_beverage', 'item_dairy', 'item_fruit', 'item_grain', 'item_meat', 'item_snack', 'item_vegetable']
selected_item = st.selectbox("Select Item Type", item_options)

st.subheader("Storage Type")
storage_options = ['storage_freezer', 'storage_fridge', 'storage_pantry']
selected_storage = st.selectbox("Select Storage Type", storage_options)

# Construct input feature vector
input_dict = {
    'purchase_month': purchase_month,
    'purchase_day_of_week': purchase_day,
    'days_until_expiry': days_until_expiry,
    'quantity': quantity
}
for col in item_options:
    input_dict[col] = 1 if col == selected_item else 0
for col in storage_options:
    input_dict[col] = 1 if col == selected_storage else 0

input_df = pd.DataFrame([input_dict])

# Debug output
st.write("🔍 Model was trained on:", model.feature_names_in_ if hasattr(model, 'feature_names_in_') else "Unknown")
st.write("📥 Input features:", input_df.columns.tolist())

try:
    pred = model.predict(input_df)[0]
    if st.button("Predict"):
        if pred == 1:
            st.success("✅ The item is likely to be used before expiry!")
        else:
            st.error("⚠️ The item may go to waste! Consider using it soon.")
except ValueError as e:
    st.error(f"🚫 Feature mismatch error: {e}")