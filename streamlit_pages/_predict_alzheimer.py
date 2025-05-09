import time
import joblib
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from config import (
    PTRACCAT_CATEGORIES,
    APOE_CATEGORIES,
    PTHETHCAT_CATEGORIES,
    APOE4_CATEGORIES,
    PTGENDER_CATEGORIES,
    IMPUTED_CATEGORIES,
    ABBREVIATION,
    CONDITION_DESCRIPTION,
    DEMENTIA_IMPLICATION
)

def prediction_page():
    def convert_to_one_hot(selected_category, all_categories):
        one_hot = [True if category == selected_category else False for category in all_categories]
        for value in one_hot:
            user_input.append(value)

    def predict_alzheimer(input_data):
        loaded_model = joblib.load('model/alzheimer_model.pkl')
        predictions = loaded_model.predict(input_data)
        return predictions

    # Function to evaluate model accuracy
    def evaluate_model():
        # Load test dataset
        try:
            test_data = pd.read_csv("data/test_data.csv")
            X_test = test_data.drop(columns=["DX.bl"])  # Features (using DX.bl as the label column)
            y_test = test_data["DX.bl"]  # True labels
        except Exception as e:
            st.error(f"Failed to load test data: {str(e)}")
            return

        # Make predictions on the test set
        y_pred = predict_alzheimer(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)

        # Display accuracy
        st.subheader("Model Evaluation")
        st.write(f"**Accuracy**: {accuracy * 100:.2f}%")
        st.write(f"Based on a test set of {len(X_test)} samples.")

    st.title("Patient Information")

    age = st.number_input("Age", min_value=0, max_value=122, step=1, value=65)
    gender = st.selectbox("Gender", ("Male", "Female"))
    education = st.number_input("Years of Education", min_value=0, value=12)

    st.write("<br>", unsafe_allow_html=True)

    st.header("Demographics")
    ethnicity = st.radio("Ethnicity", ("Hisp/Latino", "Not Hisp/Latino", "Unknown"))
    race_cat = st.radio("Race Category", ("White", "Black", "Asian"))

    st.write("<br>", unsafe_allow_html=True)

    st.header("Genetic Information")
    apoe_allele_type = st.selectbox("APOE Allele Type", ["APOE4_0", "APOE4_1", "APOE4_2"])
    apoe_genotype = st.selectbox("APOE4 Genotype", ("2,2", "2,3", "2,4", "3,3", "3,4", "4,4"))
    imputed_genotype = st.radio("Imputed Genotype", ("True", "False"))

    st.header("Cognitive Assessment")
    mmse = st.number_input("MMSE Score", min_value=0, max_value=30, step=1)

    st.write("<br>", unsafe_allow_html=True)
    # Add two buttons side by side
    col1, col2 = st.columns(2)
    with col1:
        predict_button = st.button("Predict")
    with col2:
        evaluate_button = st.button("Evaluate Model")  # New button for evaluation
    st.write("")

    loading_bar = st.empty()
    if age and education and mmse and apoe_genotype and race_cat and gender and apoe_allele_type and imputed_genotype and ethnicity and predict_button:
        loading_bar.write("Thank you for entering the patient's information.")
        progress_text = "Please wait, we're predicting your clinical condition..."
        my_bar = loading_bar.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1, text=progress_text)

        user_input = [age, education, mmse]

        convert_to_one_hot("PTRACCAT_" + race_cat, PTRACCAT_CATEGORIES)
        convert_to_one_hot("APOE Genotype_" + apoe_genotype, APOE_CATEGORIES)
        convert_to_one_hot("PTETHCAT_" + ethnicity, PTHETHCAT_CATEGORIES)
        convert_to_one_hot(apoe_allele_type, APOE4_CATEGORIES)
        convert_to_one_hot("PTGENDER_" + gender, PTGENDER_CATEGORIES)
        convert_to_one_hot("imputed_genotype_" + imputed_genotype, IMPUTED_CATEGORIES)

        data = pd.DataFrame([user_input])
        predicted_condition = predict_alzheimer(data)
        
        loading_bar.empty()

        st.write("")
        st.write("")
        st.write("### Predicted Clinical Condition:", unsafe_allow_html=True)
        st.write(f"## <b>{ABBREVIATION[predicted_condition[0]]}</b> ({predicted_condition[0]})", unsafe_allow_html=True)
        st.write(f"{CONDITION_DESCRIPTION[predicted_condition[0]]}", unsafe_allow_html=True)
        
        # Add dementia implication
        st.write(f"### Dementia Implication:", unsafe_allow_html=True)
        st.write(f"{DEMENTIA_IMPLICATION[predicted_condition[0]]}", unsafe_allow_html=True)
        
        # Add disclaimer
        st.write("")
        st.write("**Note**: This prediction is based on machine learning and should not be considered a medical diagnosis. Please consult a healthcare professional for an accurate assessment.", unsafe_allow_html=True)

    # Evaluate model if the button is clicked
    if evaluate_button:
        evaluate_model()