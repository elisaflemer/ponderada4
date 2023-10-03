import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests


# Function to make predictions using the server API
def get_diabetes_prediction(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level, gender):
    # Extract JWT token from the secrets store
    jwt_token = st.session_state.jwt_token

    data = {
        "age": int(age),
        "hypertension": int(hypertension),
        "heart_disease": int(heart_disease),
        "bmi": int(bmi),
        "hba1c_level": int(hba1c_level),
        "blood_glucose_level": int(blood_glucose_level),
        "gender_Female": int(gender == 'Female'),
        "gender_Male": int(gender == 'Male')
    }
    
    # Include the JWT token in the request headers
    headers = {"Authorization": f"Bearer {jwt_token}"}

    response = requests.post("http://44.218.232.113:5000/api/predict", json=data, headers=headers)
    response_json = response.json()
    print(response_json)
    print(response.status_code)
    if response.status_code == 200:
        return response.json()
    elif response_json['error']['message'] == 'jwt expired':
        st.session_state.logged_in = False
        st.rerun()
    else:
        print(response_json)

# Login Page
def login_page():
    st.title("Login Page")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        # Send a request to the authentication server to obtain the JWT token
        response = requests.post("http://44.218.232.113:5000/api/users/login", json={"email": email, "password": password})

        if response.status_code == 200:
            # Store the JWT token in Streamlit secrets
            jwt_token = response.json()["token"]
            st.session_state.jwt_token = jwt_token
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Login failed. Please try again.")

    st.title("Create new user")
    username = st.text_input("register_username")
    email = st.text_input("register_email")
    password = st.text_input("register_password", type="password")
    confirm_password = st.text_input("confirm_password", type="password")
    register_button = st.button("Register")

    if register_button:
        if password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        else:
            # Send a request to the server to register the user
            response = requests.post("http://44.218.232.113:5000/api/users/", json={"email": email, "password": password, "name": username})

            if response.status_code == 201:
                st.success("Registration successful! You can now log in.")
                st.rerun()
            else:
                st.error("Registration failed. Please try again.")

# Check if the user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Main App
if st.session_state.logged_in:
    st.title("Diabetes Prediction")
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page:", ["Predict", "Get insights"])

    if page == "Predict":
        # Input Form
        st.subheader("Enter Patient Information:")
        age = st.number_input("Age", min_value=0)
        hypertension = st.checkbox("Hypertension")
        heart_disease = st.checkbox("Heart Disease")
        bmi = st.number_input("BMI")
        hba1c_level = st.number_input("HbA1c Level")
        blood_glucose_level = st.number_input("Blood Glucose Level")
        gender = st.radio("Gender", ["Female", "Male"])

        if st.button("Predict"):
            # Make a prediction request to the server
            prediction = get_diabetes_prediction(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level, gender)

            if prediction is not None:
                if prediction["prediction"] == '1':
                    st.success(f"The patient does have diabetes.")
                else:
                    st.success(f"The patient does not have diabetes.")
            else:
                st.error("Prediction failed. Please try again.")

    elif page == "Get insights":
        st.header("Data visualization")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        data = pd.read_csv("diabetes_prediction_dataset.csv")
       # Filter data for people with diabetes and without diabetes
        diabetic_data = data[data["diabetes"] == 1]
        non_diabetic_data = data[data["diabetes"] == 0]

        # Create two rows to compare the graphs
        column1, column2 = st.columns(2)

        with column1:
            st.subheader("Age (Diabetic)")
            plt.figure(figsize=(8, 6))
            sns.histplot(data=diabetic_data, x='age', bins=20, kde=True)
            plt.xlabel("Age")
            plt.ylabel("Count")
            st.pyplot()

        with column1:
            st.subheader("BMI vs. Glucose (Diabetic)")
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=diabetic_data, x="bmi", y="blood_glucose_level", hue="gender")
            plt.xlabel("BMI")
            plt.ylabel("Blood Glucose Level")
            st.pyplot()

        # Row 2: Compare BMI vs. Blood Glucose Level (Diabetic)
        with column2:
            st.subheader("Age (Non-Diabetic)")
            plt.figure(figsize=(8, 6))
            sns.histplot(data=non_diabetic_data, x='age', bins=20, kde=True)
            plt.xlabel("Age")
            plt.ylabel("Count")
            st.pyplot()

        # Row 2: Compare BMI vs. Blood Glucose Level (Non-Diabetic)
        with column2:
            st.subheader("BMI vs. Glucose (Non-Diabetic)")
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=non_diabetic_data, x="bmi", y="blood_glucose_level", hue="gender")
            plt.xlabel("BMI")
            plt.ylabel("Blood Glucose Level")
            st.pyplot()

                # Scatter plot of BMI vs. Age colored by Diabetes
        st.subheader("Scatter plot of BMI vs. Age (Colored by Diabetes)")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=data, x="bmi", y="age", hue="diabetes")
        plt.xlabel("BMI")
        plt.ylabel("Age")
        plt.title("Scatter plot of BMI vs. Age (Colored by Diabetes)")
        st.pyplot()

        # Box plot of Blood Glucose Level by Diabetes
        st.subheader("Box plot of Blood Glucose Level by Diabetes")
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=data, x="diabetes", y="blood_glucose_level")
        plt.xlabel("Diabetes")
        plt.ylabel("Blood Glucose Level")
        plt.title("Box plot of Blood Glucose Level by Diabetes")
        st.pyplot()

        # Countplot of Diabetes vs. Hypertension
        st.subheader("Countplot of Diabetes vs. Hypertension")
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x="diabetes", hue="hypertension")
        plt.xlabel("Diabetes")
        plt.title("Countplot of Diabetes vs. Hypertension")
        st.pyplot()
else:
    login_page()
