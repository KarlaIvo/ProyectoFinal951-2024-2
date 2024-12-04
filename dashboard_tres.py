import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash_bootstrap_components as dbc

data = pd.read_csv("assets/datasets/Clean_bc_collabs.csv")

def grafica_hist(data):
    fig_hist = px.histogram(data, y='Price', nbins=20, title='Distribución de Precios de Colaboraciones', orientation='h')
    fig_hist.update_traces(marker=dict(color="#7fb3d5"))
    fig_hist.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_hist

@callback(
    Output("figDistPriceColb", "figure"),
    Input("figDistPriceColb", "id")
)
def act_hist(_):
    fig_hist = grafica_hist(data)
    return fig_hist

def grafica_caros():
    caros = data.nlargest(10, 'Price')
    fig_barCaros = px.bar(caros, x='Title', y='Price', title='Top 10 Colaboraciones más Caras')
    fig_barCaros.update_traces(marker=dict(color="#a93226"))
    fig_barCaros.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barCaros

@callback(
    Output("figColbCaros", "figure"),
    Input("figColbCaros", "id")
)
def act_caros(_):
    fig_barCaros = grafica_caros()
    return fig_barCaros

def grafica_baratos():
    baratos = data.nsmallest(10, 'Price')
    fig_barBaratos = px.bar(baratos, x='Title', y='Price', title='Top 10 Colaboraciones más Baratas')
    fig_barBaratos.update_traces(marker=dict(color="#45b39d"))
    fig_barBaratos.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barBaratos

@callback(
    Output("figColbBaratos", "figure"),
    Input("figColbBaratos", "id")
)
def act_baratos(_):
    fig_barBaratos = grafica_baratos()
    return fig_barBaratos
def dashboard():
    body = html.Div([
        dbc.Row(html.Div([html.H3("Distribución de precios y 10 colaboraciones más caras", style={"color": "white", "text-align": "center", "margin-top": "30px"})]), className="row_uno"),
        dbc.Row([
            dbc.Col(dcc.Graph(id="figDistPriceColb")),
            dbc.Col(dcc.Graph(id="figColbCaros")),
            dbc.Col(dcc.Graph(id="figColbBaratos")),
        ])
    ])
    return body




app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dashboard()

if __name__ == "__main__":
    app.run_server(debug=True)
