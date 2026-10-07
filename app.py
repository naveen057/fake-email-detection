import streamlit as st
import joblib
import re
import string


# Load model and TF-IDF vectorizer
model = joblib.load("fake_email_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")


# Text cleaning function
def clean_text(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Page configuration
st.set_page_config(
    page_title="Fake Email Detector",
    page_icon="📧"
)


# Title
st.title("📧 Fake Email Detection System")

st.write(
    "Enter an email below to check whether it is "
    "Spam or Legitimate."
)


# Email input
email = st.text_area(
    "Enter Email Content",
    height=250,
    placeholder="Paste the email message here..."
)


# Prediction
if st.button("🔍 Detect Email"):

    if email.strip() == "":
        st.warning("Please enter an email.")

    else:

        cleaned_email = clean_text(email)

        # Convert text to TF-IDF
        email_vector = tfidf.transform([cleaned_email])

        # Predict
        prediction = model.predict(email_vector)[0]

        # Probability
        probability = model.predict_proba(email_vector)[0]

        spam_probability = probability[1] * 100
        ham_probability = probability[0] * 100

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("🚨 SPAM / SUSPICIOUS EMAIL")
        else:
            st.success("✅ LEGITIMATE EMAIL")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Legitimate",
                f"{ham_probability:.2f}%"
            )

        with col2:
            st.metric(
                "Spam",
                f"{spam_probability:.2f}%"
            )