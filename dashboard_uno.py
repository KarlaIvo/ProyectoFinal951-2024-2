import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Input, Output
import dash_bootstrap_components as dbc

data = pd.read_csv("assets/datasets/Clean_bc_accessories.csv")
def grafica_pastel(data, names_col, values_col):
    fig = px.pie(
        data,
        names=names_col,
        values=values_col,
        title='Distribución de Precios por Accesorio',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    return fig



def tarjeta_filtro():
    control = dbc.Card(
        [html.Div([
                dbc.Label("Accesorio:", style={"margin-left": "10px", "font-weight": "bold"}),
                dcc.Dropdown(
                    id="ddAccesorio",  # Cambiado el ID para reflejar el nuevo propósito
                    options=[{"label": "Todos", "value": "all"}] +
                            [{"label": titulo, "value": titulo} for titulo in data['Título'].unique()],
                    value="all"
                )
            ], style={"margin-bottom": "15px"}),
            html.Div([
                dbc.Label("Rango de Precios:", style={"margin-left": "10px", "font-weight": "bold"}),
                dbc.InputGroup(
                    [
                        dbc.Input(
                            id="minPrice",
                            type="number",
                            placeholder="Mínimo",
                            min=0
                        ),
                        dbc.Input(
                            id="maxPrice",
                            type="number",
                            placeholder="Máximo",
                            min=0
                        )
                    ]
                )
            ])
        ],
        body=True,
        style={"padding": "15px", "margin-bottom": "15px"}
    )
    return control


def grafica_box(y_cols):
    fig_box = px.box(data,y=y_cols,
                     title="Grafica de Caja y Bigotes")
    fig_box.update_layout(
        paper_bgcolor="#fadbd8",
        plot_bgcolor="#ffffff",
        title=dict(font=dict(size=20), x=0.5),
    )
    return fig_box



def dashboard():
    body = html.Div([
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H3("Filtros", style={"color": "#d98880"}),
                    html.Hr(),
                    tarjeta_filtro()
                ]),
                style={"background-color": "#fadbd8"}, width=4
            ),
            dbc.Col(
                html.Div([
                    dbc.Row(dcc.Graph(id="figLine")),
                    dbc.Row(dcc.Graph(id="figBox")),
                ]),
                width=8
            )
        ])
    ], style={"background-color": "#FFFFFF"})
    return body


@callback(
    Output(component_id="figLine",component_property="figure"),#salidas del evento
    Output(component_id="figBox",component_property="figure"),
    Input(component_id="ddCompany",component_property="value")#acciona el evento

)#decorador es decir funcionalidad extra
def update_grafica(value_company):
    # Filtrar o ajustar los datos según el valor seleccionado
    if value_company == "all":
        filtered_data = data
    else:
        filtered_data = data[data['Título'] == value_company]

    # Generar las gráficas
    fig_pastel = grafica_pastel(filtered_data, names_col='Título', values_col='Precio')
    fig_box = grafica_box(filtered_data, y_col='Precio')

    return fig_pastel, fig_box


