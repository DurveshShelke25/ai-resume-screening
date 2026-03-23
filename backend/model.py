def match_resume(job_desc, resume):
    job_desc = job_desc.lower()
    resume = resume.lower()

    skills = [
        "python", "sql", "machine learning", "data analysis",
        "pandas", "numpy", "java", "c++", "excel"
    ]

    jd_skills = [skill for skill in skills if skill in job_desc]
    resume_skills = [skill for skill in skills if skill in resume]

    matched = list(set(jd_skills) & set(resume_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    if len(jd_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(jd_skills)) * 100

    return {
        "score": round(score, 2),
        "matched": matched,
        "missing": missing
    }