import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd

df = pd.read_csv("D:\Appraisals_Apr211.csv")
tm = df.TeamMember.unique()
pc = df.ProjectCode.unique()
pt = df.ProjectType.unique()

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in tm],
        value=tm[0],
        clearable=False,
    )]),


        html.Div([
    dcc.Dropdown(
        id="dropdown1",
        options=[{"label": x, "value": x} for x in pc],
        value=pc[0],
        clearable=False,
    )]),

    html.Div([dcc.Graph(id="pie-chart")],style={'width': '48%', 'display': 'inline-block'}),
    html.Div([dcc.Graph(id="bar-chart")],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
    html.Div([dcc.Graph(id="bar-chart1")],style={'width': '48%', 'display': 'inline-block'}),
    html.Div([dcc.Graph(id="bar-chart2")],style={'width': '48%', 'display': 'inline-block'}),
    html.Div([dcc.Graph(id="bar-chart3")],style={'width': '48%', 'display': 'inline-block'}),

    html.Div([dcc.Graph(id="bar-chart4")],style={'width': '48%', 'display': 'inline-block'}),
    html.Div([dcc.Graph(id="bar-chart5")],style={'width': '48%', 'display': 'inline-block'}),

])

@app.callback(
    Output("pie-chart", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart1(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.pie(df[ mask ], values='ActualEfforts', names='ProjectPhase', title='Phase Wise Effort Distribution', color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.bar(df[ mask ], x="ProjectPhase", y=["PlannedEfforts", "ActualEfforts"], barmode="group", color_discrete_map={
        'PlannedEfforts': 'indianred','ActualEfforts': 'lightsalmon'})
    return fig

@app.callback(
    Output("bar-chart1", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart1(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.bar(df[ mask ], x="ProjectPhase", y=["T_BugsIdentified", "T_BugsAccepted", "Bugs Rejection %"], barmode="group", color_discrete_map={
        'T_BugsIdentified': 'Yellow','T_BugsAccepted': 'Orchid', 'Bugs Rejection %': 'Tomato'})
    return fig

@app.callback(
    Output("bar-chart2", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart1(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.bar(df[ mask ], x="ProjectPhase", y=["Total ELOC/TCS Prep/TCS Exec", "Productivity"], barmode="group", color_discrete_map={
        'Total ELOC/TCS Prep/TCS Exec': 'PaleVioletRed','Productivity': 'PaleGreen'})
    return fig

@app.callback(
    Output("bar-chart3", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart1(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.bar(df[ mask ], x="ProjectPhase", y=["PhaseEscapedBugs"], barmode="group", color_discrete_map={
        'PhaseEscapedBugs': 'SandyBrown'})
    return fig

@app.callback(
    Output("bar-chart4", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart1(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.bar(df[ mask ], x="ProjectPhase", y=["T_Low", "T_Medium", "T_High"], barmode="stack", color_discrete_map={
        'T_Low': 'Wheat','T_Medium': 'Aquamarine', 'T_High': 'OrangeRed'})
    return fig

@app.callback(
    Output("bar-chart5", "figure"),
    [Input("dropdown", "value"),
     Input("dropdown1", "value")])
def update_bar_chart1(TeamMember, ProjectCode):
    mask = (df["ProjectCode"] == ProjectCode) & (df["TeamMember"] == TeamMember)
    fig = px.bar(df[ mask ], x="ProjectPhase", y=["Target DRE%","Actual DRE%" ], barmode="group",  color_discrete_map={
        'Target DRE%': 'RosyBrown', 'Actual DRE%': 'Aquamarine'})
    return fig

app.run_server(debug=True)