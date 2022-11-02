#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    ai_page.py
# @Author:      Kuro
# @Time:        11/1/2022 9:52 AM

import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objects as go
from dash import html, dcc, callback, Output, Input, State

from model import build_model
from utils import GRAPH_CONFIG, split_data, X, y, scale_data


def AI_page():
    return html.Div(children=[
        html.H1(children='Train model'),
        html.Div([
            html.Label("Select test size:", style={'margin-left': '1em'}),
            dcc.Dropdown(
                id='test_size',
                options=[0.1, 0.2, 0.3],
                value=0.2,
                style={"width": "5em", 'margin-left': '0.5em'}
            )
        ]),
        dbc.Row([
            dbc.Col([
                html.Label("Select number of hidden layers:", style={'margin-left': '1em'}),
                dcc.Dropdown(
                    id='hidden',
                    options=[3, 5, 7],
                    value=3,
                    style={"width": "5em", 'margin-left': '0.5em'}
                )
            ]),
            dbc.Col([
                html.Label("Select learning rate:"),
                dcc.Dropdown(
                    id='lr',
                    options=[0.01, 0.001, 0.0001],
                    value=0.001,
                    style={"width": "8em"}
                )
            ]),
            dbc.Col([
                html.Label("Select batch size:"),
                dcc.Dropdown(
                    id='batch_size',
                    options=[32, 64, 128],
                    value=128,
                    style={"width": "6em"}
                )
            ]),
            dbc.Col([
                html.Label("Select epochs:"),
                dcc.Dropdown(
                    id='epochs',
                    options=[150, 250, 500],
                    value=250,
                    style={"width": "6em"}
                )
            ]),

            dbc.Col([
                html.Label("Select Dropout layer:"),
                dcc.RadioItems(id='dropout', options=["Yes", "No"], value="No", inline=True, labelStyle={'display': 'inline-block', 'marginRight': '7px'})
            ]),

        ]),
        html.Div(
            dbc.Button(id='train_btn', children="Train", style={'verticalAlign': 'middle', "margin-top": "30px", "margin-bottom": "30px", 'width': '200px'},
                       n_clicks=0),
            style={"textAlign": "center"}
        ),
        dcc.Loading(
            id="loading",
            type="default",
            children=dcc.Graph(
                id="graph_ai",
                config=GRAPH_CONFIG,
            ),
        ),

    ])


@callback(
    Output("graph_ai", "figure"),
    Input("train_btn", "n_clicks"),
    State("test_size", "value"),
    State("hidden", "value"),
    State("lr", "value"),
    State("batch_size", "value"),
    State("epochs", "value"),
    State("dropout", "value"),
    prevent_initial_call=True,
)
def page_return(n_clicks, test_size, hidden_layers, lr, batch_size, epochs, dropout):
    if n_clicks != 0:
        X_train, X_test, y_train, y_test = split_data(X, y, test_size)
        X_train, X_test = scale_data(X_train, X_test)
        model = build_model(hidden_layers, lr, dropout)
        model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=batch_size, verbose=0, shuffle=False, epochs=epochs)
        y_pred = model.predict(X_test)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=np.array(y_test).flatten(), y=y_pred.flatten(), mode='markers'))
        fig.add_trace(
            go.Scatter(
                name='Y=80',
                x=[np.array(y_test).flatten().min(), np.array(y_test).flatten().max()],
                y=[np.array(y_test).flatten().min(), np.array(y_test).flatten().max()],
                mode="lines",
                marker=dict(color='rgb(150, 150, 0)'),
                showlegend=False
            )
        )
        return fig
    else:
        return go.Figure(go.Scatter(x=[], y=[]))
