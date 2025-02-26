from pdf import read_pdf
import os
import google.generativeai as genai
import streamlit as st

# Configure the key
genai.configure(api_key='AIzaSyBmYsYPeQyAQtdZRdAK_YELlsKHltKA6HI')
model = genai.GenerativeModel("gemini-1.5-pro") #Initiate the Model


def profile(user_profile,job_desc):
    if user_profile is not None:
        pdf = read_pdf(user_profile)
        st.sidebar.markdown("The Resume has been uploaded.")
    else:
        st.warning("Upload the Resume")
    
    # ATS Score    
    ats_score = model.generate_content(f'''compare the {pdf} with job description {job_desc} and suggest the ATS Score in percentage of the resume.''')

    # Chances of Selection
    chance = model.generate_content(f'''compare the {pdf} with job description {job_desc} and suggest the probability in percentage of getting selected''')

    # Keyword analysis
    keyword =  model.generate_content(f'''compare the {pdf} with job description {job_desc} and analyse the keywords missing in the resume with the job description and mention them in bold and give narratives how to add them in resume.''')
    
    
    # Tailor Projects as per JD
    projects = model.generate_content(f'''compare the {pdf} with job description {job_desc} and give me the list of projects or hackathons (in bold) with problem statements and probabilty of selection as per the Jo Description.''')
    
    
    # SWOT Analysis
    swot = model.generate_content(f'''compare the {pdf} with job description {job_desc} and provide a SWOT analysis''')
    
    
    # Improvement Tips
    improve = model.generate_content(f'''compare the {pdf} with job description {job_desc} and suggest improvements in the resume so that the ATS score increases and it is better aligned and mention the comments (in bold)''')
    
    
    # Tailor made Resume
    resume = model.generate_content(f'''recreate the new resume basis the {pdf} to highlight the relevant skill, projects and experience according to the job description {job_desc} ''')
    
    
    # Display the Results
    return (st.write(ats_score.text),
            st.write(chance.text),
            st.write(keyword.text),
            st.write(projects.text),
            st.write(swot.text),
            st.write(improve.text),
            st.write(resume.text))



