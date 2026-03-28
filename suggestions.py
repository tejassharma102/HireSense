def give_suggestions(resume, job_desc):
    suggestions = []

    resume = resume.lower()
    job_words = set(job_desc.lower().split())

    missing = [word for word in job_words if word not in resume]

    for word in list(missing)[:5]:
        suggestions.append(f"Consider adding '{word}'")

    if "project" not in resume:
        suggestions.append("Add project section")

    if "skill" not in resume:
        suggestions.append("Add skills section")

    if len(resume.split()) < 80:
        suggestions.append("Increase resume content")

    return suggestions