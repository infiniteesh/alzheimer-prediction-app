import streamlit as st

# PAGE CONFIG
CSS = open("assets/css/styles.css", 'r').read()

# ASSETS
BACKGROUND = "assets/images/bg.webp"
BANNER = "assets/images/banner.webp"
DEFAULT_IMAGE = "assets/images/default.webp"
SIDE_BANNER = "assets/images/side_banner.webp"
EMOJI = "assets/images/emo.webp"

# PREDICTION PAGE
APOE_CATEGORIES = ['APOE Genotype_2,2', 'APOE Genotype_2,3', 'APOE Genotype_2,4', 
                   'APOE Genotype_3,3', 'APOE Genotype_3,4', 'APOE Genotype_4,4']
PTHETHCAT_CATEGORIES = ['PTETHCAT_Hisp/Latino', 'PTETHCAT_Not Hisp/Latino', 'PTETHCAT_Unknown']
IMPUTED_CATEGORIES = ['imputed_genotype_True', 'imputed_genotype_False']
PTRACCAT_CATEGORIES = ['PTRACCAT_Asian', 'PTRACCAT_Black', 'PTRACCAT_White']
PTGENDER_CATEGORIES = ['PTGENDER_Female', 'PTGENDER_Male']
APOE4_CATEGORIES = ['APOE4_0', 'APOE4_1', 'APOE4_2']
ABBREVIATION = {
                "AD": "Alzheimer's Disease ",
                "LMCI": "Late Mild Cognitive Impairment ",
                "CN": "Cognitively Normal"
            }

CONDITION_DESCRIPTION = {
    "AD": "This indicates that the individual's data aligns with characteristics commonly associated with "
        "Alzheimer's disease. Alzheimer's disease is a progressive neurodegenerative disorder that affects "
        "memory and cognitive functions.",
    "LMCI": "This suggests that the individual is in a stage of mild cognitive impairment that is progressing "
            "towards Alzheimer's disease. Mild Cognitive Impairment is a transitional state between normal "
            "cognitive changes of aging a   nd more significant cognitive decline.",
    "CN": "This suggests that the individual has normal cognitive functioning without significant impairments. "
        "This group serves as a control for comparison in Alzheimer's research."
}

# NEWS PAGE
NEWS_API_KEY = "9c26cb930eef4299b496cb4e13d746d8"
# KEYWORD = "alzheimer"

# CHATBOT PAGE
GEMINI_API_KEY = "AIzaSyB_CZbXVv6ESIbMHI1LCI-CTnucggNS4ps"
BASE_PROMPT = "You are an empathetic and knowledgeable virtual assistant helping users understand their Alzheimer's disease risk predictions. Provide clear explanations about Alzheimer's symptoms, stages, and risk factors using simple language. Avoid giving medical diagnoses or treatment advice. Always remind users to consult a healthcare professional for medical concerns. Be supportive, non-judgmental, and informative."
 # or your actual prompt"

# TEAM MEMBERS PAGE
TEAM_MEMBERS = [
    {
        "name": "Omkar Pandey",
        "role": "Final Year Student - CSE AI",
        "links": ["https://www.linkedin.com/in/omkar_pandey", "https://github.com/omkar_pandey"],
        
    },
    {
        "name": "Nitish Kumar Gupta",
        "role": "Final Year Student - CSE AI",
        "links": ["https://www.linkedin.com/in/infiniteesh", "https://github.com/infiniteesh"],
    
    },
    {
        "name": "Payoli Verma",
        "role": "Final Year Student - CSE AI",
        "links": ["https://www.linkedin.com/in/Payoli/", "https://github.com/Payoli"],
      
    },
    {
        "name": "Nishant Gupta",
        "role": "Final Year Student - CSE AI",
        "links": ["https://www.linkedin.com/in/Nishant_Gupta", "https://github.com/Nishant"],
       
    },
]