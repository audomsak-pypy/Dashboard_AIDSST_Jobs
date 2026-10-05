# AI & Data Science Labor Market Dashboard

## Overview
This project is an Interactive Dashboard built to analyze and compare the supply of graduates against the labor market demand in the fields of AI, Data Science, and Statistics. It focuses on addressing the skills mismatch, salary expectations, and required skills based on mock data representing real-world open datasets.

## Objectives
- Visualize global trends in the AI, Data Science, and Statistics job markets.
- Compare the skills taught in university programs with the skills actively required by employers.
- Identify "Skills Mismatch" gaps indicating critical shortages or oversupplies of specific skills.

## Architecture & Tech Stack
- **Backend & Framework:** Python, Dash by Plotly
- **Data Visualization:** Plotly (Interactive Graphs)
- **UI Framework:** Dash Bootstrap Components
- **Interactivity:** Cross-filtering using Dash Callbacks

## Dashboard Structure
The dashboard is separated into three main tabs:
1. **Education & Supply:** Analyzes graduates volume, core courses, employment rate post-graduation, and tuition fees.
2. **Labor Market & Demand:** Evaluates job vacancies, required skills, hiring companies, and salaries across different experience levels.
3. **Skills Mismatch Analysis:** Compares skills supply against demand to discover critical shortages and oversupplied skills using quadrant analysis.

## Reference Data
The mock data generation strategy is based on the following real-world datasets:
- Stanford AI Index Report Dataset (Number of Graduates)
- Data Science Job Salaries 2023-2024 via Kaggle (Employment, Salaries, Company Size & Career Levels)
- Kaggle Machine Learning & Data Science Survey (Required Skills)

## Getting Started
Ensure you have Python installed. The required packages include `dash`, `dash-bootstrap-components`, `pandas`, and `plotly`. Run the `app.py` script to launch the dashboard locally.
