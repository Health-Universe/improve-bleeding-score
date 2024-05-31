import streamlit as st

# Title and description
st.title('IMPROVE Bleeding Risk Score Calculator')
st.write("""
This app calculates the IMPROVE Bleeding Risk Score, which helps to estimate the risk of bleeding in hospitalized patients. 
Please enter the relevant patient information to get the score.
""")

# Patient input fields
age = st.number_input('Age (years)', min_value=0, step=1)
active_cancer = st.selectbox('Active Cancer', ['No', 'Yes'])
history_of_bleeding = st.selectbox('History of Bleeding', ['No', 'Yes'])
renal_failure = st.selectbox('Renal Failure (GFR < 30 ml/min)', ['No', 'Yes'])
liver_failure = st.selectbox('Liver Failure', ['No', 'Yes'])
thrombocytopenia = st.selectbox('Thrombocytopenia (Platelets < 50x10^9/L)', ['No', 'Yes'])
sex = st.selectbox('Sex', ['Female', 'Male'])
antiplatelet_therapy = st.selectbox('On Antiplatelet Therapy', ['No', 'Yes'])

# Calculate IMPROVE Bleeding Risk Score
score = 0

if age >= 40:
    score += 1
if active_cancer == 'Yes':
    score += 2
if history_of_bleeding == 'Yes':
    score += 2
if renal_failure == 'Yes':
    score += 1
if liver_failure == 'Yes':
    score += 1
if thrombocytopenia == 'Yes':
    score += 4
if sex == 'Male':
    score += 1
if antiplatelet_therapy == 'Yes':
    score += 1

# Display the score
st.write(f'IMPROVE Bleeding Risk Score: {score}')

# Interpret the score
if score <= 1:
    st.write("Risk Level: Low")
elif score <= 2:
    st.write("Risk Level: Moderate")
else:
    st.write("Risk Level: High")
