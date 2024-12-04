import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Output, Input
import dash_bootstrap_components as dbc

data = pd.read_csv("assets/datasets/Clean_bc_bundles.csv")

def grafica_histograma(data):
    fig_histograma = px.histogram(data, y='Price', nbins=20, title='Distribución de Precios de Paquetes', orientation='h')
    fig_histograma.update_traces(marker=dict(color="#7fb3d5"))
    fig_histograma.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_histograma

def grafica_top_caros():
    top_caros = data.nlargest(10, 'Price')
    fig_barras_caros = px.bar(top_caros, x='Title', y='Price', title='Top 10 Paquetes más Caros')
    fig_barras_caros.update_traces(marker=dict(color="#a93226"))
    fig_barras_caros.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#fadbd8",
        title=dict(font=dict(size=20), x=0.5)
    )
    return fig_barras_caros

def grafica_top_baratos():
    top_baratos = data.nsmallest(10, 'Price')  # Filtra los 10 productos más baratos
    fig_barras_baratos = px.bar(top_baratos, x='Title', y='Price', title='Top 10 Paquetes más Baratos')
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
                html.H3("Distribución de precios y 10 Paquetes más caros y más baratos", style={"color": "white", "text-align": "center", "margin-top": "30px"})]), className="row_uno"),
        dbc.Row([
                dbc.Col(dcc.Graph(id="figDistribucionPreciosPaq")),  # Distribución de precios
                dbc.Col(dcc.Graph(id="figTopCarosPaq")),  # Top 10 paquetes más caros
                dbc.Col(dcc.Graph(id="figTopBaratosPaq")),  # Top 10 paquetes más baratos
        ])
    ])
    return body

# Callback para actualizar la gráfica de distribución de precios
@callback(
    Output("figDistribucionPreciosPaq", "figure"),  # Gráfica de distribución de precios
    Input("figDistribucionPreciosPaq", "id")
)
def update_histograma(_):
    fig_histograma = grafica_histograma(data)
    return fig_histograma

# Callback para actualizar la gráfica de los productos más caros
@callback(
    Output("figTopCarosPaq", "figure"),  # Gráfico de los top 10 productos más caros
    Input("figTopCarosPaq", "id")
)
def update_top_caros(_):
    fig_barras_caros = grafica_top_caros()
    return fig_barras_caros

# Callback para actualizar la gráfica de los productos más baratos
@callback(
    Output("figTopBaratosPaq", "figure"),  # Gráfico de los top 10 productos más baratos
    Input("figTopBaratosPaq", "id")
)
def update_top_baratos(_):
    fig_barras_baratos = grafica_top_baratos()
    return fig_barras_baratos

# Crear la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Configurar el layout de la aplicación
app.layout = dashboard()

if __name__ == "__main__":
    app.run_server(debug=True)
