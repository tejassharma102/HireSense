# HIRE SENSE

### 1. Project Overview

Greetings. SkillLens is an AI-powered resume analysis application designed to help students and job seekers improve their resumes based on job descriptions. It is often observed that candidates fail to get shortlisted due to lack of keyword optimization and improper resume structuring. This results in low visibility in Applicant Tracking Systems (ATS).

SkillLens solves this problem by providing a smart platform that compares resumes with job descriptions using NLP techniques. It generates a similarity score and gives actionable suggestions, enabling users to enhance their resumes and improve their chances of selection.

### 2. Key Features

The application has been engineered with the following capabilities:

Interactive User Interface (Streamlit):
A clean and simple web-based interface allows users to input resume and job description easily.

Resume Matching System:
Compares resume content with job description using TF-IDF and Cosine Similarity.

Similarity Score Generation:
Provides a percentage score indicating how well the resume matches the job role.

Smart Suggestions:
Highlights missing keywords and suggests improvements to increase ATS score.

Text Preprocessing:
Removes stopwords, punctuation, and performs normalization for accurate analysis.

### 3. Technologies & Tools Used
Python (3.x): Core programming language
Streamlit: For building interactive UI
Scikit-learn: For TF-IDF vectorization and similarity calculation
NLTK: For text preprocessing
Cosine Similarity: For matching resume and job description
### 4. Project File Structure
The project is divided into six files for better modularity:

main.py is the entry point of the application.
model.py handles the overall processing logic.
preprocess.py is used for cleaning and preparing text data.
similarity.py calculates the similarity score.
suggestions.py generates improvement suggestions.
vectorizer.py converts text into numerical vectors using TF-IDF.
### 5. Detailed Installation Instructions
First, make sure Python is installed by checking the version in the terminal.
Clone the project repository and navigate into the folder.
Install the required libraries such as streamlit, nltk, and scikit-learn.
Download required NLTK datasets.
Run the application using the command streamlit run main.py.
### 6. Testing Guide

Scenario A: Resume Input
Action: Paste resume text in the input box
Expected Result: Text gets processed without errors

Scenario B: Job Description Input
Action: Enter job description
Expected Result: System accepts input and prepares for comparison

Scenario C: Score Calculation
Action: Click analyze button
Expected Result: Displays similarity score (e.g., 85%)

Scenario D: Suggestions
Action: View suggestions section
Expected Result: Missing keywords and improvements are shown

### 7. Future Enhancements
Resume PDF upload support
Advanced NLP models (BERT-based matching)
Skill extraction and visualization dashboard
Real-time job recommendation system
