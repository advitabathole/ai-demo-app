import streamlit as st
from src.load_model import load

st.title("AI Sentiment Analyzer")
st.write("Enter text and the model will predict the sentiment.")

model, vectorizer = load()

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        X = vectorizer.transform([user_input])
        prediction = model.predict(X)[0]
        st.success(f"Prediction: **{prediction.upper()}**")

