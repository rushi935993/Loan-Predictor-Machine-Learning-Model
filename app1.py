import streamlit as st
import pickle 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("loan.pkl", "rb") as f:
    predictor = pickle.load(f)

st.set_page_config(page_title = "Loan Predictor", layout="wide")


df = pd.read_csv('loan.csv')

def introduction():
    st.title(" Loan Approval Prediction App")
    
    st.image("loan.jpg", width=200)
    
    st.markdown("""
    This application uses a machine learning model (XGBoost Classifier) to predict whether a loan application will be approved or not based on user input.

    The app is divided into multiple pages:
    - **Introduction**: Project overview and goals
    - **Data Exploration**: Look at raw data and basic statistics
    - **Data Visualization**: See patterns and trends
    - **Prediction**: Input applicant data and get a prediction
    """)

def data_exploration():
    st.title(" Data Exploration")
    st.write("Sample Data")
    st.write(df.head())
    st.write("Data Summary")
    st.write(df.describe(include='all'))
    st.write("Missing Values")
    st.write(df.isnull().sum())
    
def data_visualization():
    st.title("Data Visualization")
    col1, col2 = st.columns(2)
    with col1:
        sns.countplot(data=df, x='Loan_Status')
        st.pyplot(plt.gcf())
        plt.clf()


def prediction():
    st.title("Predict Loan Approval")
    st.markdown("### Enter Applicant Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        # age = st.number_input("Choose your age:", min_value = 18, max_value = 70)
        Gender = st.selectbox("Choose your gender:", ["Male", "Female"])
        Married = st.selectbox("Choose Married Or Not:", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["0","1", "2", "3", "3+"])
        Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    
    with col2:
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        applicant_income = st.number_input("Applicant Income", min_value=0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=1)
        submit = st.button("Submit")

    with col3:
        loan_term = st.selectbox("Loan Amount Term", [360, 180, 120, 84, 60, 36, 12])
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])
    
    with open("loan.pkl", "rb") as f:
        predictor = pickle.load(f)

    if submit:
        data = [Gender, Married, Dependents, Education,self_employed,applicant_income,coapplicant_income, loan_amount, loan_term, credit_history, property_area]
        
        data = pd.DataFrame([data], columns = ["Gender","Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"])
        
        data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
        data['Married'] = data['Married'].map({'Yes': 1, 'No': 0})
        data['Dependents'] = data['Dependents'].replace('3+', 3).astype(int)
        data['Education'] = data['Education'].map({'Graduate': 1, 'Not Graduate': 0})
        data['Self_Employed'] = data['Self_Employed'].map({'Yes': 1, 'No': 0})
        data['Property_Area'] = data['Property_Area'].map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})
        
        data['Total_Income'] = data['ApplicantIncome'] + data['CoapplicantIncome']
        data['Income_to_Loan'] = data['Total_Income'] / data['LoanAmount']

        
        prediction = predictor.predict(data)
        
        if prediction == 1:
            st.write("Loan approved")
        elif prediction ==0:
            st.write("Loan rejected")

def about_me():
    st.title("About Me")
    
    st.image("my_photo.jpg", width=200, caption="Data Science Student But Part Time A Livery Designer!")

    st.markdown("""
    Hey there!

    Myself Rushikesh Patil, I'm a passionate third-year student currently pursuing a degree in **Artificial Intelligence & Data Science**.  
    With a strong interest in real-world applications of Machine Learning and Data Science, I'm constantly exploring new projects to grow my skills.

    ---

    What I'm Into:
    - **Machine Learning** - building smart, predictive models that make sense of data.
    - **Data Analysis** - uncovering patterns and insights hidden in messy datasets.
    - **Deep Learning** - playing around with neural networks and cool architectures.
    - **Streamlit** - creating clean, interactive apps to showcase ML work.

    ---

    Tools & Tech I Use:
    - **Languages**: Python, SQL, a bit of HTML/CSS
    - **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn
    - **Platforms**: Jupyter, Streamlit, Google Colab

    ---

    ### My Goal:
    To solve real-life problems using AI/ML, and eventually contribute to impactful tech — whether it's in finance, healthcare, or even space!

    ---

    ### Let's Connect!
    If you're into ML, data, or just love building cool stuff — let’s collaborate!

    """)
        
pages = {
    "1. Introduction": introduction,
    "2. Data Exploration": data_exploration,
    "3. Data Visualization": data_visualization,
    "4. Prediction": prediction,
    "5. About Me": about_me
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages[selection]()
