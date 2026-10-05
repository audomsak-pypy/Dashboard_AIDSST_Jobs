import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_dashboard_data

# Load real data from internet
data = load_dashboard_data()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "AI & Data Science Labor Market Dashboard"

# Extracting DataFrames
df_graduates = data["graduates"]
df_courses_skills = data["courses_skills"]
df_employment = data["employment"]
df_tuition = data["tuition"]
df_vacancies = data["vacancies"]
df_hiring = data["hiring"]
df_required_skills = data["required_skills"]
df_salary = data["salary"]
df_mismatch = data["mismatch"]
sources = data.get("sources", {})

# ----------------- UI Layout -----------------
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("AI & Data Science Labor Market 2023-2024", className="text-center my-4"), width=12)
    ]),
    dbc.Tabs([
        # Tab 1: Education & Supply
        dbc.Tab(label="Education & Supply", tab_id="tab-1", children=[
            dbc.Row([
                dbc.Col([
                    html.H4("Graduates Volume"),
                    dcc.Graph(id="graduates-chart")
                ], width=6),
                dbc.Col([
                    html.H4("Core Courses & Learned Skills"),
                    dcc.Graph(id="courses-chart")
                ], width=6)
            ], className="mt-4"),
            dbc.Row([
                dbc.Col([
                    html.H4("Employment Rate Post-Graduation"),
                    dcc.Graph(id="employment-chart")
                ], width=8),
                dbc.Col([
                    html.H4("Tuition Fees (USD)"),
                    dcc.Graph(id="tuition-chart")
                ], width=4)
            ], className="mt-4")
        ]),

        # Tab 2: Labor Market & Demand
        dbc.Tab(label="Labor Market & Demand", tab_id="tab-2", children=[
            dbc.Row([
                dbc.Col([
                    html.H4("Job Vacancies Volume"),
                    dcc.Graph(id="vacancies-chart")
                ], width=7),
                dbc.Col([
                    html.H4("Top Required Skills"),
                    dcc.Graph(id="skills-chart")
                ], width=5)
            ], className="mt-4"),
            dbc.Row([
                dbc.Col([
                    html.H4("Hiring Companies for Selected Skill"),
                    dcc.Graph(id="companies-chart")
                ], width=6),
                dbc.Col([
                    html.H4("Salary by Experience Level"),
                    dcc.Graph(id="salary-chart")
                ], width=6)
            ], className="mt-4")
        ]),

        # Tab 3: Skills Mismatch Analysis
        dbc.Tab(label="Skills Mismatch Analysis", tab_id="tab-3", children=[
            dbc.Row([
                dbc.Col([
                    html.H4("Skills Supply vs Demand (Mismatch Gap)"),
                    dcc.Graph(id="mismatch-scatter")
                ], width=12)
            ], className="mt-4"),
            dbc.Row([
                dbc.Col([
                    html.H4("Detailed Supply vs Demand Breakdown"),
                    dcc.Graph(id="mismatch-bar")
                ], width=12)
            ], className="mt-4")
        ])
    ], id="tabs", active_tab="tab-1"),
    
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H5("Data Sources", className="mt-3"),
            html.Ul([
                html.Li(f"Graduates Data: {sources.get('graduates', 'N/A')}"),
                html.Li(f"Core Courses: {sources.get('courses', 'N/A')}"),
                html.Li(f"Employment Rates: {sources.get('employment', 'N/A')}"),
                html.Li(f"Tuition Fees: {sources.get('tuition', 'N/A')}"),
                html.Li(f"Job Salaries & Vacancies: {sources.get('salaries', 'N/A')}"),
                html.Li(f"Required Skills: {sources.get('skills', 'N/A')}"),
            ], className="text-muted", style={"fontSize": "0.9em"})
        ], width=12)
    ], className="mb-5")
], fluid=True)


# ----------------- Callbacks -----------------

# Tab 1 Callbacks
@app.callback(
    Output("graduates-chart", "figure"),
    Input("tabs", "active_tab")
)
def update_graduates_chart(_):
    fig = px.bar(df_graduates, x="Year", y="Number of Graduates", color="Program Name", barmode="stack")
    return fig

@app.callback(
    Output("courses-chart", "figure"),
    Input("graduates-chart", "clickData")
)
def update_courses_chart(clickData):
    filtered_df = df_courses_skills
    title = "Courses & Skills (All Programs)"
    if clickData:
        selected_program = clickData["points"][0]["curveNumber"]
        program_names = df_graduates["Program Name"].unique()
        if selected_program < len(program_names):
            prog = program_names[selected_program]
            filtered_df = df_courses_skills[df_courses_skills["Program Name"] == prog]
            title = f"Courses & Skills ({prog})"
    
    # We create a simple horizontal bar for skills, or a sunburst
    skill_counts = filtered_df["Skill"].value_counts().reset_index()
    skill_counts.columns = ["Skill", "Count"]
    fig = px.bar(skill_counts, x="Count", y="Skill", orientation='h', title=title)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

@app.callback(
    Output("employment-chart", "figure"),
    Input("tabs", "active_tab")
)
def update_employment_chart(_):
    fig = px.bar(df_employment, x="Cohort", y="Employment Rate", color="Year After Grad", barmode="group", facet_col="Program Name", facet_col_wrap=2)
    fig.update_layout(yaxis_title="Employment Rate (%)")
    return fig

@app.callback(
    Output("tuition-chart", "figure"),
    Input("tabs", "active_tab")
)
def update_tuition_chart(_):
    fig = px.bar(df_tuition, x="Program Name", y="Tuition Fee (USD)", color="Program Name")
    fig.update_layout(showlegend=False)
    return fig

# Tab 2 Callbacks
@app.callback(
    Output("vacancies-chart", "figure"),
    Input("tabs", "active_tab")
)
def update_vacancies_chart(_):
    fig = px.area(df_vacancies, x="Date", y="Job Openings", color="Job Title")
    return fig

@app.callback(
    Output("skills-chart", "figure"),
    Input("tabs", "active_tab")
)
def update_skills_chart(_):
    fig = px.bar(df_required_skills.sort_values("Frequency", ascending=True), x="Frequency", y="Skill", orientation='h')
    return fig

@app.callback(
    Output("companies-chart", "figure"),
    Input("skills-chart", "clickData")
)
def update_companies_chart(clickData):
    filtered_df = df_hiring
    title = "Hiring Companies (All Skills)"
    if clickData:
        selected_skill = clickData["points"][0]["y"]
        filtered_df = df_hiring[df_hiring["Skill"] == selected_skill]
        title = f"Hiring Companies for '{selected_skill}'"
    
    comp_counts = filtered_df.groupby(["Company", "Industry"]).size().reset_index(name="Count")
    fig = px.scatter(comp_counts, x="Company", y="Count", color="Industry", size="Count", title=title)
    return fig

@app.callback(
    Output("salary-chart", "figure"),
    Input("tabs", "active_tab")
)
def update_salary_chart(_):
    fig = px.box(df_salary, x="Experience Level", y="Salary", color="Experience Level")
    return fig


# Tab 3 Callbacks
@app.callback(
    Output("mismatch-scatter", "figure"),
    Input("tabs", "active_tab")
)
def update_mismatch_scatter(_):
    fig = px.scatter(df_mismatch, x="Demand (%)", y="Supply (%)", color="Status", hover_name="Skill", text="Skill")
    fig.update_traces(textposition='top center')
    # Add quadrants
    fig.add_hline(y=20, line_dash="dash", line_color="gray")
    fig.add_vline(x=40, line_dash="dash", line_color="gray")
    return fig

@app.callback(
    Output("mismatch-bar", "figure"),
    Input("tabs", "active_tab")
)
def update_mismatch_bar(_):
    df_melt = df_mismatch.melt(id_vars=["Skill"], value_vars=["Supply (%)", "Demand (%)"], var_name="Type", value_name="Percentage")
    fig = px.bar(df_melt, x="Percentage", y="Skill", color="Type", barmode="group", orientation='h')
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
