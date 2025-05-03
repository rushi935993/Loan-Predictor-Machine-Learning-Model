# 🏦 Loan Approval Predictor
This is a Streamlit-based web application that predicts whether a loan application will be approved or rejected using a machine learning model. Built using the XGBoost Classifier, it provides users with an intuitive interface to explore data, visualize trends, and interactively test the model.
# 



![image](https://github.com/user-attachments/assets/a14e362d-41a2-4a2e-84ae-e7a31afca7e8)



# 🚀 Features
1.📊 Data Exploration: View raw data and summary statistics.

2.📈 Data Visualization: Understand trends and patterns in loan approvals.

3.🤖 Loan Prediction: Input applicant details and get instant approval predictions.

4.💡 About Me: Know the developer behind this project.
#
![image](https://github.com/user-attachments/assets/5b5b3668-8a74-42e9-841a-d4da92a17b4e)



# 🛠️ Tech Stack
Frontend: Streamlit

Machine Learning Model: XGBoost Classifier (trained separately and loaded via Pickle)

Data Handling & Visualization: pandas, seaborn, matplotlib
#

![image](https://github.com/user-attachments/assets/432b7033-de06-475c-867c-a9dbc6ffc870)

#

![image](https://github.com/user-attachments/assets/b05579f2-1213-426f-b259-b105c8b3054b)



# 📂 Files Included
app1.py: Main Streamlit app file containing all UI logic and model integration.

loan.pkl: Pre-trained ML model used for prediction.

loan.csv: Dataset used for analysis and model training.

loan.ipynb: Jupyter Notebook used for preprocessing and model training (not shown here, but part of the repo).

# 🔍 How It Works
User inputs applicant information (gender, income, loan amount, etc.).

The inputs are preprocessed (e.g., encoding, feature engineering).

The model predicts loan approval (1 for approved, 0 for rejected).

Result is displayed directly in the app.


# 👨‍💻 About the Developer
I'm Rushikesh Patil, a third-year AI & Data Science student passionate about real-world ML applications, data analysis, and interactive web apps.
Let's connect and build something amazing together!
#
![image](https://github.com/user-attachments/assets/5a050ab4-f235-4328-bf2e-1c133aed919c)
#
![image](https://github.com/user-attachments/assets/4eb607ff-750c-4429-8d0c-b59be92f021f)



# 📌 Getting Started
Clone this repo

Install required packages
1.pip install streamlit
2.pip install matplotlib
3.pip install numpy
4.pip install scikit-learn
4.pip install seaborn

Run the app with:

bash
Copy
Edit
streamlit run app1.py
