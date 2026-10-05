import pandas as pd
import numpy as np
import random

def generate_mock_data():
    np.random.seed(42)
    random.seed(42)

    # --- Tab 1: Education & Supply ---
    # 1. Graduates Volume
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    programs = ["B.Sc. Data Science", "M.Sc. AI", "B.Sc. Statistics", "Ph.D. Computer Science"]
    graduates_data = []
    for year in years:
        for prog in programs:
            base = 100 if "B.Sc" in prog else 50
            graduates_data.append({
                "Year": year,
                "Program Name": prog,
                "Number of Graduates": int(base + (year - 2019) * 20 * random.uniform(0.8, 1.2))
            })
    df_graduates = pd.DataFrame(graduates_data)

    # 2. Core Courses & Learned Skills
    courses_skills = [
        {"Program Name": "B.Sc. Data Science", "Course Name": "Intro to Data Science", "Skill": "Python"},
        {"Program Name": "B.Sc. Data Science", "Course Name": "Database Systems", "Skill": "SQL"},
        {"Program Name": "B.Sc. Data Science", "Course Name": "Machine Learning 101", "Skill": "Machine Learning"},
        {"Program Name": "M.Sc. AI", "Course Name": "Deep Learning", "Skill": "Deep Learning"},
        {"Program Name": "M.Sc. AI", "Course Name": "Natural Language Processing", "Skill": "NLP"},
        {"Program Name": "M.Sc. AI", "Course Name": "Advanced ML", "Skill": "Python"},
        {"Program Name": "B.Sc. Statistics", "Course Name": "Probability Theory", "Skill": "R"},
        {"Program Name": "B.Sc. Statistics", "Course Name": "Statistical Modeling", "Skill": "Statistical Analysis"},
        {"Program Name": "Ph.D. Computer Science", "Course Name": "Research Methods", "Skill": "Research"},
        {"Program Name": "Ph.D. Computer Science", "Course Name": "Advanced Algorithms", "Skill": "C++"}
    ]
    df_courses_skills = pd.DataFrame(courses_skills)

    # 3. Employment Rate Post-Graduation
    employment_data = []
    for cohort in [2019, 2020, 2021, 2022, 2023]:
        for prog in programs:
            employment_data.append({"Cohort": cohort, "Program Name": prog, "Year After Grad": "Year 1", "Employment Rate": random.uniform(50, 75)})
            employment_data.append({"Cohort": cohort, "Program Name": prog, "Year After Grad": "Year 2", "Employment Rate": random.uniform(70, 85)})
            employment_data.append({"Cohort": cohort, "Program Name": prog, "Year After Grad": "Year 3", "Employment Rate": random.uniform(80, 95)})
    df_employment = pd.DataFrame(employment_data)

    # 4. Tuition Fees
    tuition_data = [
        {"Program Name": "B.Sc. Data Science", "Tuition Fee (USD)": 20000},
        {"Program Name": "M.Sc. AI", "Tuition Fee (USD)": 30000},
        {"Program Name": "B.Sc. Statistics", "Tuition Fee (USD)": 15000},
        {"Program Name": "Ph.D. Computer Science", "Tuition Fee (USD)": 5000}, # often funded
    ]
    df_tuition = pd.DataFrame(tuition_data)

    # --- Tab 2: Labor Market & Demand ---
    # 1. Job Vacancies
    dates = pd.date_range(start="2022-01-01", end="2024-01-01", freq="MS")
    job_titles = ["AI Engineer", "Data Analyst", "Data Scientist", "Machine Learning Engineer"]
    vacancies_data = []
    for date in dates:
        for title in job_titles:
            base = 500 if title in ["Data Analyst", "Data Scientist"] else 300
            vacancies_data.append({
                "Date": date,
                "Job Title": title,
                "Job Openings": int(base + random.randint(-50, 200) + (date.year - 2022)*100)
            })
    df_vacancies = pd.DataFrame(vacancies_data)

    # 2. Required Skills & 3. Hiring Companies
    skills_list = ["Python", "SQL", "R", "Machine Learning", "Deep Learning", "NLP", "AWS", "Docker", "Statistical Analysis", "Tableau"]
    companies = ["TechCorp", "DataGen", "HealthAI", "FinancePlus", "RetailAnalytics", "CloudNet"]
    industries = {"TechCorp": "Technology", "DataGen": "Consulting", "HealthAI": "Healthcare", "FinancePlus": "Finance", "RetailAnalytics": "Retail", "CloudNet": "Technology"}
    
    hiring_data = []
    for i in range(200): # 200 mock job postings
        comp = random.choice(companies)
        title = random.choice(job_titles)
        req_skills = random.sample(skills_list, k=random.randint(2, 5))
        for skill in req_skills:
            hiring_data.append({
                "Company": comp,
                "Industry": industries[comp],
                "Job Title": title,
                "Skill": skill,
                "Job ID": i
            })
    df_hiring = pd.DataFrame(hiring_data)
    
    # Required skills aggregated
    df_required_skills = df_hiring["Skill"].value_counts().reset_index()
    df_required_skills.columns = ["Skill", "Frequency"]

    # 4. Salary by Experience Level
    experience_levels = ["Entry (EN)", "Mid (MI)", "Senior (SE)", "Executive (EX)"]
    salary_data = []
    for i in range(500):
        level = random.choice(experience_levels)
        if level == "Entry (EN)": base = 60000
        elif level == "Mid (MI)": base = 100000
        elif level == "Senior (SE)": base = 150000
        else: base = 200000
        salary_data.append({
            "Experience Level": level,
            "Job Title": random.choice(job_titles),
            "Salary": int(np.random.normal(base, base*0.15))
        })
    df_salary = pd.DataFrame(salary_data)

    # --- Tab 3: Skills Mismatch Analysis ---
    # Compare skills supply vs demand
    # Supply = proportion of courses teaching the skill
    total_courses = len(df_courses_skills)
    skill_supply = df_courses_skills.groupby("Skill").size() / total_courses * 100
    
    # Demand = proportion of job postings requiring the skill
    total_jobs = df_hiring["Job ID"].nunique()
    skill_demand = df_hiring.groupby("Skill")["Job ID"].nunique() / total_jobs * 100

    df_mismatch = pd.DataFrame({
        "Supply (%)": skill_supply,
        "Demand (%)": skill_demand
    }).fillna(0).reset_index()

    # Determine mismatch status
    def categorize_mismatch(row):
        if row["Demand (%)"] > 40 and row["Supply (%)"] < 20:
            return "Critical Shortage"
        elif row["Demand (%)"] < 20 and row["Supply (%)"] > 30:
            return "Oversupply"
        elif row["Demand (%)"] > 40 and row["Supply (%)"] >= 20:
            return "High Demand & Adequately Supplied"
        else:
            return "Balanced / Low Priority"
            
    df_mismatch["Status"] = df_mismatch.apply(categorize_mismatch, axis=1)

    return {
        "graduates": df_graduates,
        "courses_skills": df_courses_skills,
        "employment": df_employment,
        "tuition": df_tuition,
        "vacancies": df_vacancies,
        "hiring": df_hiring,
        "required_skills": df_required_skills,
        "salary": df_salary,
        "mismatch": df_mismatch
    }
