import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash_bootstrap_components as dbc

data = pd.read_csv("assets/datasets/Clean_bc_accessories.csv")

def grafica_histograma(data):
    fig_histograma = px.histogram(data, y='Price', nbins=20, title='Distribución de Precios de Productos',
                                  orientation='h')
    fig_histograma.update_traces(marker=dict(color="#7fb3d5"))
    fig_histograma.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_histograma

def grafica_top_caros():
    top_caros = data.nlargest(10, 'Price')
    fig_barras_caros = px.bar(top_caros, x='Title', y='Price', title='Top 10 Productos más Caros')
    fig_barras_caros.update_traces(marker=dict(color="#a93226"))
    fig_barras_caros.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barras_caros

def grafica_top_baratos():
    top_baratos = data.nsmallest(10, 'Price')  # Filtra los 10 productos más baratos
    fig_barras_baratos = px.bar(top_baratos, x='Title', y='Price', title='Top 10 Productos más Baratos')
    fig_barras_baratos.update_traces(marker=dict(color="#45b39d"))  # Cambia el color de las barras
    fig_barras_baratos.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barras_baratos


def dashboard():
    body = html.Div([
        dbc.Row(html.Div([
                html.H3("Distribución de Precios, 10 Productos Más Caros y Más Baratos", style={"color": "white", "text-align": "center", "margin-top": "30px"})]), className="row_uno"),
        dbc.Row([
                dbc.Col(dcc.Graph(id="figDistribucionPrecios")),  # Gráfico de distribución de precios
                dbc.Col(dcc.Graph(id="figTopCaros")),  # Gráfico de los productos más caros
                dbc.Col(dcc.Graph(id="figTopBaratos")),  # Gráfico de los productos más baratos
            ])
        ])
    return body

@callback(
    Output("figDistribucionPrecios", "figure"),
    Input("figDistribucionPrecios", "id")
)
def update_histograma(_):
    fig_histograma = grafica_histograma(data)
    return fig_histograma

@callback(
    Output("figTopCaros", "figure"),
    Input("figTopCaros", "id")
)
def update_top_caros(_):
    fig_barras_caros = grafica_top_caros()
    return fig_barras_caros

@callback(
    Output("figTopBaratos", "figure"),
    Input("figTopBaratos", "id")
)
def update_top_baratos(_):
    fig_barras_baratos = grafica_top_baratos()
    return fig_barras_baratos


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dashboard()

if __name__ == "__main__":
    app.run_server(debug=True)


