import streamlit as st
from config import BANNER

def home_page():
    # Display the banner image
    st.image(BANNER)

    # Section 1: Overview of Alzheimer's Disease
    st.subheader("Understanding Alzheimer's Disease")
    st.write("""
        Alzheimer's disease (AD) is a chronic condition that gradually damages the brain. It is most commonly recognized for causing memory loss, but it also leads to challenges with thinking, problem-solving, decision-making, and completing everyday tasks. Additionally, it can result in changes to a person’s personality and behavior. The exact cause of AD remains unclear, though genetics are believed to play a significant role. For instance, the APOE e4 variant of the APOE gene is known to heighten the risk of developing Alzheimer's.
    """)

    # Section 2: Importance of Early Detection
    st.subheader("The Value of Early Diagnosis")
    st.write("""
        Detecting Alzheimer's disease early is critical as it provides the best opportunity for managing the condition effectively and enhancing the quality of life. Recognizing the disease in its initial stages enables prompt interventions that can slow its advancement, giving individuals and their loved ones time to prepare for what lies ahead. Furthermore, early diagnosis opens doors to support resources and participation in research studies, offering hope for discovering better treatments to combat this challenging illness.
    """)

    # Section 3: Project Objective
    st.subheader("Goal of This Project")
    st.write("""
        This project aims to create a machine learning model designed for the early identification of Alzheimer's disease. As a debilitating brain disorder impacting millions globally, Alzheimer's requires timely detection to improve patient outcomes and explore potential treatments. By utilizing advanced machine learning methods, this initiative seeks to build a model capable of predicting the risk of Alzheimer's disease using relevant data, ultimately supporting better care and intervention strategies.
    """)

    # Add section about Alzheimer's and dementia relationship
    st.subheader("Alzheimer's and Dementia: What's the Connection?")
    st.write("""
        Alzheimer's disease is the most common cause of dementia, a general term for cognitive decline severe enough to interfere with daily life. In this project, a prediction of Alzheimer's Disease (AD) or Late Mild Cognitive Impairment (LMCI) indicates the presence of dementia, as Alzheimer's is a primary cause of dementia. However, other types of dementia (e.g., vascular dementia) may also exist and require further medical evaluation.
    """)

    # Add a small spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Caption to guide users to the prediction page
    st.caption("Done exploring? Head over to the `Prediction Page` to try out some predictions.")