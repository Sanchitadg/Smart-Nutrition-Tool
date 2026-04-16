import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Food_Nutrition_Dataset.csv")

# Title
st.title("🥗 Smart Nutrition Tool")

# Category selection
category = st.selectbox("Select Category", df["category"].unique())

# Filter by category
cat = df[df["category"] == category]

# Food selection
food_name = st.selectbox("Select Food", cat["food_name"].unique())

# Filter by food
food = cat[cat["food_name"] == food_name]

# Extract nutrients
cal = food.iloc[0]["calories"]
pro = food.iloc[0]["protein"]
carb = food.iloc[0]["carbs"]
fat = food.iloc[0]["fat"]

# Display
st.subheader("📊 Nutritional Information")
st.write("Energy:", cal)
st.write("Protein:", pro, "g")
st.write("Carbs:", carb, "g")
st.write("Fat:", fat, "g")
