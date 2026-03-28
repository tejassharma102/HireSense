import streamlit as st
from model import analyze_resume

st.title("📄 Smart Resume Analyzer (SkillLens)")

resume = st.text_area("Paste your Resume")
job_desc = st.text_area("Paste Job Description")

def get_grade(score):
    if score >= 80:
        return "A (Excellent)"
    elif score >= 60:
        return "B (Good)"
    elif score >= 40:
        return "C (Average)"
    else:
        return "D (Needs Improvement)"

if st.button("Analyze"):
    if resume and job_desc:
        score, suggestions = analyze_resume(resume, job_desc)

        percentage = round(score * 100, 2)
        grade = get_grade(percentage)

        # ✅ Final Score
        st.success(f"✅ Resume Score: {percentage}%")
        st.info(f"📊 Grade: {grade}")

        # ✅ Progress bar
        st.progress(int(percentage))

        st.subheader("💡 Suggestions:")
        for s in suggestions:
            st.write("- " + s)
    else:
        st.warning("Please enter both resume and job description")