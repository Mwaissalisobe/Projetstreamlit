import streamlit as st
import joblib
import numpy as np
#import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import LabelEncoder,StandardScaler
#from sklearn.neighbors import KNeighborsClassifier
"from sklearn.metrics import accuracy_score

model_path = "Financial.pkl"
#model = joblib.load(model_path)

    # Entrées utilateur

age_of_respondent = st.number_input("donner l'age du conserne :")
gender_of_respondent = st.number_input("donner le genre:")
marital_status= st.number_input("donner le statut:")
job_type = st.number_input( "donner le type job:")

if st.button("🔮 Prédire "):
    # Créer l'input pour le modèle sous forme de tableau numpy
    input_data = np.array([[age_of_respondent, gender_of_respondent, marital_status, job_type]])

    # Faire la prédiction
    prediction = model.predict(input_data)[0]
    # Afficher le résultat
    if prediction == 1:
        st.success("✅ Les personnes disposer un compte bancaire ")
    else:
        st.error("❌ Les personnes qui ne diposer pas un compte bancaire.")

    
