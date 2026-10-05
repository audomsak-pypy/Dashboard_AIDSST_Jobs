# 🚀 Handoff Document for Antigravity: AI & Data Science Labor Market Dashboard

**To:** Antigravity (Dashboard Generation Agent / Framework)
**Project Name:** AI & Data Science Labor Market Overview
**Objective:** Generate an interactive dashboard to visualize global trends in the AI, Data Science, and Statistics job market, focusing on salaries, career levels, essential skills, and graduation trends based on Open Data sources.

## 📂 1. Open Data Sources (Reference)

The dashboard design and mock data generation should be modeled after the following open-source datasets:

1. **Number of Graduates:** 
   * **Source:** Stanford AI Index Report Dataset (GitHub)
   * **Link:** [Stanford AI Index Data Repository](https://github.com/ai-index-hai-stanford/AI-Index-2020)
   * **Details:** Covers PhD and Master's graduates in AI, Computer Science, and Statistics globally.

2. **Employment, Salaries, Company Size & Career Levels:**
   * **Source:** Data Science Job Salaries 2023-2024 (Kaggle / ai-jobs.net)
   * **Link:** [Data Science Salaries on Kaggle](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023)
   * **Details:** Contains anonymized salary data (`salary_in_usd`), career levels (Entry, Mid, Senior, Executive), company locations, and company sizes (S, M, L).

3. **Required Skills in Job Applications:**
   * **Source:** Kaggle Machine Learning & Data Science Survey
   * **Link:** [Kaggle Survey Data 2022/2023](https://www.kaggle.com/c/kaggle-survey-2022/data)
   * **Details:** In-depth survey detailing programming languages, tools, and cloud platforms required by organizations and possessed by applicants.

## 📊 2. Data Schema & Variables (Context)

The dashboard will process data based on the following conceptual schema (derived from the datasets above):

* **Employment & Salary Data (Main Dataset):**
  * `work_year`: Year of the record (e.g., 2023, 2024)
  * `experience_level`: EN (Entry), MI (Mid), SE (Senior), EX (Executive)
  * `job_title`: e.g., Data Scientist, AI Engineer, Statistician
  * `salary_in_usd`: Standardized salary for comparison
  * `employee_residence` / `company_location`: Country codes (e.g., US, IN, GB, TH)
  * `company_size`: S (<50), M (50-250), L (>250)

* **Skills Data (Aggregated):**
  * `skill_name`: e.g., Python, SQL, R, Machine Learning, AWS
  * `demand_frequency`: Percentage or count of mentions in job postings

* **Graduates Data (Aggregated):**
  * `year`: Academic year
  * `degree_type`: PhD, Masters
  * `graduates_count`: Number of graduates globally

## 🎨 3. Dashboard Layout & UI Components

Please generate a dashboard with the following layout structure:

### **Header Section**
* **Title:** "Global AI & Data Science Labor Market 2023-2024"
* **Global Filters:**
  * Dropdown: `Experience Level` (All, Entry, Mid, Senior, Executive)
  * Dropdown: `Company Size` (All, S, M, L)

### **Top Row: KPI Scorecards**
1. **Average Global Salary (USD):** Dynamically calculated based on filters.
2. **Top In-Demand Skill:** E.g., "Python (85%)".
3. **Highest Paying Country (Avg):** E.g., "United States".

### **Middle Row: Main Visualizations**
1. **Salary by Experience Level (Bar Chart):**
   * X-Axis: Experience Level (EN, MI, SE, EX)
   * Y-Axis: Average `salary_in_usd`
   * *Color scheme: Gradient from light blue (EN) to dark blue (EX).*

2. **Top 10 Essential Skills (Horizontal Bar Chart):**
   * X-Axis: Demand Frequency
   * Y-Axis: Skill Name

### **Bottom Row: Distribution & Trends**
1. **Job Distribution by Company Size (Pie or Donut Chart):**
   * Categories: S, M, L
   * Value: Count of jobs

2. **AI & Stats Graduates Trend (Line Chart):**
   * X-Axis: Year
   * Y-Axis: `graduates_count`
   * Breakdown: Line per Degree Type (Master's vs PhD)

## ⚙️ 4. Execution Instructions for Antigravity

1. **Framework:** Use your default web-based dashboard framework (e.g., React + Recharts, Plotly Dash, or Streamlit equivalent depending on your environment).
2. **Mock Data:** Since direct database connection is not provided in this prompt, please **generate realistic mock data** based on the schema and Open Data sources listed above to populate the charts initially.
3. **Styling:** Use a clean, modern, and professional theme (Light mode preferred, with tech-oriented colors like Blue/Teal/Slate).
4. **Interactivity:** Ensure that selecting a filter in the Header automatically updates the KPI scorecards and the Bar/Pie charts.
5. **Output:** Please generate the full necessary code (HTML/JS/CSS or Python/React component) to render this dashboard perfectly.