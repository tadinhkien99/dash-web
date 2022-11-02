#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    app.py
# @Author:      Kuro
# @Time:        10/31/2022 3:24 PM


# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Filename:    treecheck.py
@Author:      kien.tadinh
@Time:        10/9/2022 1:22 PM
"""

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Output, Input

from pages.ai_page import AI_page
from pages.analytics import analytics
from pages.home import home
from utils import fig1, fig2, fig3, fig4, fig5, df

app = dash.Dash(__name__,
                assets_folder="assets",
                assets_url_path="assets",
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                    "https://cdn.jsdelivr.net/gh/lipis/flag-icons@6.6.6/css/flag-icons.min.css"
                ])

app.config['suppress_callback_exceptions'] = True

button_group = dbc.Nav(
    [
        dbc.NavItem(dcc.Link(
            dbc.Button(children='Home', className="nav-btn"),
            href='/', refresh=True),
        ),
        dbc.NavItem(dcc.Link(
            dbc.Button(children='Analytics', className="nav-btn"),
            href='/analytics', refresh=True),
        ),
        dbc.NavItem(dcc.Link(
            dbc.Button(children='AI', className="nav-btn"),
            href='/AI', refresh=True),
        ),

    ], className="nav"
)

page = html.Div(id="page-wrapper")

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    button_group,
    html.Div(children=page)
])


@app.callback(
    Output("page-wrapper", "children"),
    Input("url", "pathname"))
def page_return(pathname):
    if "analytics" in pathname:
        page = analytics(fig1, fig2, fig3, fig4, fig5, df)
    elif "AI" in pathname:
        page = AI_page()
    else:
        page = home()
    return page


if __name__ == "__main__":
    app.run_server()
