from dash import html
import dash_bootstrap_components as dbc

def welcome():
    body = html.Div(
        [
            dbc.Row(
                html.Div([
                html.H3("Beauty Creations",style={"color": "white", "text-align": "center","margin-top": "30px"})]),className="row_uno"),
            html.Img(src="assets/imagenes/bc.png",
                     width=200, height=200, title="Python"),
            html.P("Objetivo: Mostrar los dashboards de la empresa Beauty Creations", className="custom_p"),
            html.Hr(),
            html.H4("Lista de Integrantes"),
            html.Ul(
                [
                    html.Li("Maria Fernanda Hernandez Aleman"),
                    html.Li("Karla Ivonne Zavala Bojorquez"),

                ]
            ),
            html.H4("Introduccion"),
            html.Ol("Presentantamos graficos de los distintos precios de productos de la marca esto enseñando la distribucion de precios, "
                    "los 10 productos mas caros y mas baratos de accesorios que manejan, paquetes que tienen disponbles y colaboraciones "
                    "que ha tenido la marca con distintas personalidades."
            )
        ]
    )
    return body