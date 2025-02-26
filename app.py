# Import the Libraries and Set up the Local Environment
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai


from pdf import read_pdf
from analysis import profile

# Lets create the Front end
st.header('Resume Analysis: :blue[ Your LLM-Powered Resume Analyzer]',
          divider='green')
st.subheader('Tips for using the Application')

notes = f'''
* **Upload the Resume (pdf):** The first step is to upload the resume for analysis.
* **Paste the Taget JD:** Share the Details of the Job Description in the Text Area below.
* **Unleash the Power of LLMs:** Here, the Gemini Model will analyze the Job Description supplied with Resume uploaded and will provide insights such as **ATS Score**,
**Probability of Getting Selected** and so on.
    '''
    
st.markdown(notes)

# Sidebar
st.sidebar.header('Upload the Resume')
user_profile = st.sidebar.file_uploader("Please Upoad the Resume here",type=['pdf'])
st.sidebar.markdown('Created by Nikhil Vinod')
st.sidebar.markdown('LinkedIn: https://www.linkedin.com/in/nikk-vd')

# Job Description Box
st.subheader('Enter the Job Description',divider=True)
job_desc = st.text_area('Copy Paste the Job Description from LinkedIn or any Job Portal',
                        max_chars=10000)


# Submit button
submit = st.button("Submit")


if submit:
    st.markdown(profile(user_profile=user_profile,job_desc = job_desc))
else:
    st.markdown("")

