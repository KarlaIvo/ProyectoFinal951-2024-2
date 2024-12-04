import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash_bootstrap_components as dbc

data = pd.read_csv("assets/datasets/Clean_bc_accessories.csv")

def grafica_hist(data):
    fig_hist = px.histogram(data, y='Price', nbins=20, title='Distribución de Precios de Accesorios',
                                  orientation='h')
    fig_hist.update_traces(marker=dict(color="#7fb3d5"))
    fig_hist.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_hist

@callback(
    Output("figDistPrice", "figure"),
    Input("figDistPrice", "id")
)
def act_hist(_):
    fig_hist = grafica_hist(data)
    return fig_hist

def grafica_caros():
    caros = data.nlargest(10, 'Price')
    fig_barCar = px.bar(caros, x='Title', y='Price', title='Top 10 Accesorios más Caros')
    fig_barCar.update_traces(marker=dict(color="#a93226"))
    fig_barCar.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barCar

@callback(
    Output("figCaros", "figure"),
    Input("figCaros", "id")
)
def act_caros(_):
    fig_barras_caros = grafica_caros()
    return fig_barras_caros

def grafica_baratos():
    baratos = data.nsmallest(10, 'Price')
    fig_barBara = px.bar(baratos, x='Title', y='Price', title='Top 10 Accesorios más Baratos')
    fig_barBara.update_traces(marker=dict(color="#45b39d"))
    fig_barBara.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barBara

@callback(
    Output("figBaratos", "figure"),
    Input("figBaratos", "id")
)
def act_bara(_):
    fig_barBara = grafica_baratos()
    return fig_barBara

def dashboard():
    body = html.Div([
        dbc.Row(html.Div([
                html.H3("Distribución de Precios, 10 Productos Más Caros y Más Baratos", style={"color": "white", "text-align": "center", "margin-top": "30px"})]), className="row_uno"),
        dbc.Row([
                dbc.Col(dcc.Graph(id="figDistPrice")),
                dbc.Col(dcc.Graph(id="figCaros")),
                dbc.Col(dcc.Graph(id="figBaratos")),
            ])
        ])
    return body


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dashboard()

if __name__ == "__main__":
    app.run_server(debug=True)


