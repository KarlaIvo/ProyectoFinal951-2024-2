import welcome as w
import dashboard_uno as d1
import dashboard_dos as d2
import dashboard_tres as d3
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, Dash, callback


@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return w.welcome()
    elif pathname == "/dash-1":
        return d1.dashboard()
    elif pathname == "/dash-2":
        return d2.dashboard()
    elif pathname == "/dash-3":
        return d3.dashboard()

    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

def menu_dashboard():


    sidebar = html.Div(
        [
            html.H2("Dashboard", className="display-6",style={"font-weight": "bold","text-align":"center"}),#titulo parametro de calassname es el tipo de letra
            html.Hr(),
            html.P(
                "Menu", className="lead",style={"text-align":"center","color":"#d98880"}
            ),
            dbc.Nav(#varra de navegacion
                [
                    dbc.NavLink("Home", href="/", active="exact"),#opciones del menu el parametro de href= para donde te dirige
                    dbc.NavLink("Dashboard 1", href="/dash-1", active="exact"),
                    dbc.NavLink("Dashboard 2", href="/dash-2", active="exact"),
                    dbc.NavLink("Dashboard 3", href="/dash-3", active="exact"),
                    dbc.NavLink("Githbub", href="https://www.github.com", active="exact", target="_blank"),
                ],
                vertical=True,
                pills=True,#formas de pildoras
            ),
        ],
        className="sidebar",#dar un estilo a la parte izquierda
    )

    content = html.Div(id="page-content", className="content")#parte derecha que muestra el contenido

    return html.Div([dcc.Location(id="url"), sidebar, content])


if __name__ == "__main__":
    app = Dash(external_stylesheets=[dbc.themes.LITERA],suppress_callback_exceptions=True)  # temas predefinidos para los dashboards
    app.layout = menu_dashboard()
    app.run(debug=True)