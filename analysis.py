from pdf import read_pdf
import os
import google.generativeai as genai
import streamlit as st

# Configure the key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro") #Initiate the Model


def profile(user_profile,job_desc,service):
    if user_profile is not None:
        pdf = read_pdf(user_profile)
        st.sidebar.markdown("The Resume has been uploaded.")
    else:
        st.warning("Upload the Resume")
    
    
    if service=='ATS Score':
        # ATS Score    
        ats_score = model.generate_content(f'''compare the {pdf} with job description {job_desc} and suggest the ATS Score in percentage of the resume.Show the ATS Score first and then details in very short"''')
        return st.write(ats_score.text)

    elif service=='Chance of Selection':
        # Chances of Selection
        chance = model.generate_content(f'''compare the {pdf} with job description {job_desc} and suggest the probability in percentage of getting selected. Show the probability of selection first and then details in short.''')
        return st.write(chance.text)
    
    elif service=='Keywords':
        # Keyword analysis
        keyword =  model.generate_content(f'''compare the {pdf} with job description {job_desc} and analyse the keywords missing in the resume with the job description and mention them in bold and give narratives how to add them in resume.''')
        return st.write(keyword.text)
        
    elif service=='Tailor Project as per JD':
        # Tailor Projects as per JD
        projects = model.generate_content(f'''Analyse the job description {job_desc} and give me the list of projects or hackathons (in bold) with problem statements the user needs to do so that the probabilty of selection as per the Job Description. Display it in a tabular format.''')
        return st.write(projects.text)
    
    elif service=='SWOT Analysis':
        # SWOT Analysis
        swot = model.generate_content(f'''compare the {pdf} with job description {job_desc} and provide a SWOT analysis''')
        return st.write(swot.text)    
    
    elif service=='Tips for Improvement':
        # Improvement Tips
        improve = model.generate_content(f'''compare the {pdf} with job description {job_desc} and suggest improvements in the resume so that the ATS score increases and it is better aligned and mention the comments (in bold)''')
        return st.write(improve.text)    
    
    elif service=='Tailor made Resume as per JD':
        # Tailor made Resume
        resume = model.generate_content(f'''recreate the new resume basis the {pdf} to highlight the relevant skill, projects and experience according to the job description {job_desc} ''')
        return st.write(resume.text)    


