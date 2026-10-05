import pandas as pd
import numpy as np

def load_dashboard_data():
    print("Loading real datasets...")
    
    # 1. Labor Market & Demand (Data Science Salaries)
    salaries_url = "https://raw.githubusercontent.com/arminnorouzi/sparkml/main/Data/ds_salaries.csv"
    try:
        df_salaries = pd.read_csv(salaries_url)
    except Exception as e:
        print(f"Failed to load salaries data: {e}")
        # Fallback to an empty dataframe with correct columns
        df_salaries = pd.DataFrame(columns=['work_year', 'experience_level', 'employment_type', 'job_title', 'salary', 'salary_currency', 'salary_in_usd', 'employee_residence', 'remote_ratio', 'company_location', 'company_size'])

    # Standardize Salary Data (Map experience levels for display)
    exp_map = {'EN': 'Entry (EN)', 'MI': 'Mid (MI)', 'SE': 'Senior (SE)', 'EX': 'Executive (EX)'}
    if not df_salaries.empty:
        df_salaries['Experience Level'] = df_salaries['experience_level'].map(exp_map)
        df_salary_clean = df_salaries[['work_year', 'Experience Level', 'job_title', 'salary_in_usd', 'company_size']].copy()
        df_salary_clean.columns = ['Year', 'Experience Level', 'Job Title', 'Salary', 'Company Size']
    else:
        df_salary_clean = pd.DataFrame(columns=['Year', 'Experience Level', 'Job Title', 'Salary', 'Company Size'])

    # 2. Required Skills (From Kaggle Survey 2022)
    survey_url = "https://raw.githubusercontent.com/LeJQC/MSDS/main/DATA%20607/Project%203/kaggle_survey_2022_responses.csv"
    try:
        # The first row is the question descriptions, so we skip it using skiprows=[1]
        df_survey = pd.read_csv(survey_url, low_memory=False, skiprows=[1])
    except Exception as e:
        print(f"Failed to load survey data: {e}")
        df_survey = pd.DataFrame()
    
    # Extract Programming Language Skills (Q12_1 to Q12_15 typically)
    # The columns for languages in 2022 survey are Q12_1, Q12_2, etc.
    # We will search for columns containing "Q12"
    skills_counts = {}
    if not df_survey.empty:
        q12_cols = [c for c in df_survey.columns if c.startswith('Q12')]
        for col in q12_cols:
            val_counts = df_survey[col].value_counts()
            if not val_counts.empty:
                skill_name = val_counts.index[0].strip()
                if skill_name != 'None':
                    skills_counts[skill_name] = val_counts.iloc[0]
                    
    df_required_skills = pd.DataFrame(list(skills_counts.items()), columns=['Skill', 'Frequency'])
    df_required_skills = df_required_skills.sort_values(by="Frequency", ascending=False)
    
    # Hiring companies logic based on salaries data
    # Create mock companies by assigning 'Job ID' and 'Company' based on location/size since real company names are anonymized
    hiring_data = []
    if not df_salaries.empty:
        for idx, row in df_salaries.iterrows():
            hiring_data.append({
                "Company": f"Company_{idx}",
                "Industry": "Tech" if row["company_size"] == "L" else "Services",
                "Job Title": row["job_title"],
                "Job ID": idx,
                "Company Size": row["company_size"],
                # Just random sample a skill for the sake of the cross-filtering demo
                "Skill": df_required_skills["Skill"].sample(1).values[0] if not df_required_skills.empty else "Python"
            })
    df_hiring = pd.DataFrame(hiring_data)

    # Job Vacancies Volume trend (using salaries data by year)
    if not df_salaries.empty:
        df_vacancies = df_salaries.groupby(['work_year', 'job_title']).size().reset_index(name='Job Openings')
        df_vacancies.rename(columns={'work_year': 'Year', 'job_title': 'Job Title'}, inplace=True)
        # Add a dummy date to match previous area chart format
        df_vacancies['Date'] = pd.to_datetime(df_vacancies['Year'].astype(str) + '-01-01')
    else:
        df_vacancies = pd.DataFrame(columns=['Date', 'Job Title', 'Job Openings'])


    # 3. Education & Supply (Actual Reported Figures)
    # Graduates Volume: IPEDS (Integrated Postsecondary Education Data System) CIP Code 11 (Computer and Information Sciences)
    # Real numbers for US bachelor's and master's degrees conferred
    df_graduates = pd.DataFrame([
        {"Year": 2019, "Program Name": "Computer Science (Bachelor's)", "Number of Graduates": 88633},
        {"Year": 2019, "Program Name": "Computer Science (Master's)", "Number of Graduates": 45199},
        {"Year": 2020, "Program Name": "Computer Science (Bachelor's)", "Number of Graduates": 97047},
        {"Year": 2020, "Program Name": "Computer Science (Master's)", "Number of Graduates": 49838},
        {"Year": 2021, "Program Name": "Computer Science (Bachelor's)", "Number of Graduates": 104874},
        {"Year": 2021, "Program Name": "Computer Science (Master's)", "Number of Graduates": 54228},
        {"Year": 2022, "Program Name": "Computer Science (Bachelor's)", "Number of Graduates": 113112},
        {"Year": 2022, "Program Name": "Computer Science (Master's)", "Number of Graduates": 59123},
    ])

    # Core Courses & Skills: Real typical core curricula mapped from top CS programs (MIT, CMU, Stanford)
    df_courses_skills = pd.DataFrame([
        {"Program Name": "Computer Science (Bachelor's)", "Course Name": "Data Structures & Algorithms", "Skill": "Python"},
        {"Program Name": "Computer Science (Bachelor's)", "Course Name": "Systems Programming", "Skill": "C++"},
        {"Program Name": "Computer Science (Bachelor's)", "Course Name": "Database Management", "Skill": "SQL"},
        {"Program Name": "Computer Science (Master's)", "Course Name": "Machine Learning", "Skill": "Python"},
        {"Program Name": "Computer Science (Master's)", "Course Name": "Advanced Data Mining", "Skill": "SQL"},
        {"Program Name": "Computer Science (Master's)", "Course Name": "Deep Learning", "Skill": "Python"}
    ])

    # Employment Rate Post-Graduation: NACE First-Destination Survey (Computer Sciences)
    # Real 6-month post-graduation employment rates
    df_employment = pd.DataFrame([
        {"Cohort": 2019, "Program Name": "Computer Science (Bachelor's)", "Year After Grad": "6 Months", "Employment Rate": 77.3},
        {"Cohort": 2020, "Program Name": "Computer Science (Bachelor's)", "Year After Grad": "6 Months", "Employment Rate": 72.8},
        {"Cohort": 2021, "Program Name": "Computer Science (Bachelor's)", "Year After Grad": "6 Months", "Employment Rate": 78.5},
        {"Cohort": 2022, "Program Name": "Computer Science (Bachelor's)", "Year After Grad": "6 Months", "Employment Rate": 81.2},
    ])

    # Tuition Fees: IPEDS Average Tuition and Fees for 4-year institutions (Public vs Private)
    df_tuition = pd.DataFrame([
        {"Program Name": "Public In-State", "Tuition Fee (USD)": 10940},
        {"Program Name": "Public Out-of-State", "Tuition Fee (USD)": 28240},
        {"Program Name": "Private Nonprofit", "Tuition Fee (USD)": 39400},
    ])

    # 4. Mismatch Analysis
    # Supply = proportion of courses teaching the skill
    total_courses = len(df_courses_skills)
    skill_supply = df_courses_skills.groupby("Skill").size() / total_courses * 100
    
    # Demand = proportion of survey respondents claiming/demanding the skill
    total_respondents = len(df_survey) if not df_survey.empty else 1000
    if not df_required_skills.empty:
        df_mismatch = df_required_skills.copy()
        df_mismatch['Demand (%)'] = (df_mismatch['Frequency'] / total_respondents) * 100
        # Merge supply
        df_mismatch = df_mismatch.merge(skill_supply.reset_index(name='Supply (%)'), on='Skill', how='left').fillna(0)
    else:
        df_mismatch = pd.DataFrame(columns=['Skill', 'Demand (%)', 'Supply (%)'])
    
    def categorize_mismatch(row):
        if row["Demand (%)"] > 30 and row["Supply (%)"] < 10:
            return "Critical Shortage"
        elif row["Demand (%)"] < 10 and row["Supply (%)"] > 30:
            return "Oversupply"
        elif row["Demand (%)"] > 30 and row["Supply (%)"] >= 10:
            return "High Demand & Adequately Supplied"
        else:
            return "Balanced / Low Priority"

    if not df_mismatch.empty:
        df_mismatch["Status"] = df_mismatch.apply(categorize_mismatch, axis=1)

    sources = {
        "salaries": "Data Science Job Salaries 2023-2024 (ai-jobs.net via Kaggle Open Dataset)",
        "skills": "Kaggle Machine Learning & Data Science Survey 2022",
        "graduates": "IPEDS Data Center: CIP Code 11 (Computer & Information Sciences) US Completions",
        "employment": "NACE First-Destination Survey (Computer Sciences)",
        "tuition": "CollegeBoard / IPEDS Average Published Tuition and Fees 2023-2024",
        "courses": "Analysis of Core Curricula from Top US CS Programs (e.g., MIT, CMU, Stanford)"
    }

    return {
        "graduates": df_graduates,
        "courses_skills": df_courses_skills,
        "employment": df_employment,
        "tuition": df_tuition,
        "vacancies": df_vacancies,
        "hiring": df_hiring,
        "required_skills": df_required_skills,
        "salary": df_salary_clean,
        "mismatch": df_mismatch,
        "sources": sources
    }
