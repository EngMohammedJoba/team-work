import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# =========================
# Read Data
# =========================

df = pd.read_csv("data/Bank_Churn.csv")

# =========================
# KPIs
# =========================

total_customers = len(df)
churned_customers = df["Exited"].sum()
active_customers = total_customers - churned_customers
churn_rate = round((churned_customers / total_customers) * 100, 2)

# =========================
# Charts
# =========================

fig_churn = px.pie(
    df,
    names="Exited",
    title="Customer Churn Distribution"
)

fig_churn.update_layout(
    template="plotly_dark"
)

geo_df = df.groupby("Geography")["Exited"].mean().reset_index()

fig_geo = px.bar(
    geo_df,
    x="Geography",
    y="Exited",
    title="Churn Rate by Country"
)

fig_geo.update_layout(
    template="plotly_dark"
)

gender_df = df.groupby("Gender")["Exited"].mean().reset_index()

fig_gender = px.bar(
    gender_df,
    x="Gender",
    y="Exited",
    title="Churn Rate by Gender"
)

fig_gender.update_layout(
    template="plotly_dark"
)

fig_age = px.histogram(
    df,
    x="Age",
    color="Exited",
    nbins=30,
    title="Age Distribution"
)

fig_age.update_layout(
    template="plotly_dark"
)

fig_balance = px.box(
    df,
    x="Exited",
    y="Balance",
    title="Balance vs Churn"
)

fig_balance.update_layout(
    template="plotly_dark"
)

fig_salary = px.box(
    df,
    x="Exited",
    y="EstimatedSalary",
    title="Salary vs Churn"
)

fig_salary.update_layout(
    template="plotly_dark"
)

# =========================
# App
# =========================

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "🏦 Bank Customer Churn Dashboard"
    ),

    html.Div([

        html.Div([
            html.H3("Total Customers"),
            html.H2(f"{total_customers}")
        ], className="kpi-card"),

        html.Div([
            html.H3("Churned Customers"),
            html.H2(f"{churned_customers}")
        ], className="kpi-card"),

        html.Div([
            html.H3("Active Customers"),
            html.H2(f"{active_customers}")
        ], className="kpi-card"),

        html.Div([
            html.H3("Churn Rate"),
            html.H2(f"{churn_rate}%")
        ], className="kpi-card"),

    ], className="kpi-container"),

    html.Div([
        dcc.Graph(figure=fig_churn)
    ], className="chart-container"),

    html.Div([
        dcc.Graph(figure=fig_geo)
    ], className="chart-container"),

    html.Div([
        dcc.Graph(figure=fig_gender)
    ], className="chart-container"),

    html.Div([
        dcc.Graph(figure=fig_age)
    ], className="chart-container"),

    html.Div([
        dcc.Graph(figure=fig_balance)
    ], className="chart-container"),

    html.Div([
        dcc.Graph(figure=fig_salary)
    ], className="chart-container")

])

if __name__ == "__main__":
    app.run(debug=True)