#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    analytics.py
# @Author:      Kuro
# @Time:        11/1/2022 9:38 AM

from dash import html, dcc, dash_table

from utils import GRAPH_CONFIG


def analytics(fig1, fig2, fig3, fig4, fig5, df_show):
    return html.Div(children=[
        html.H4(children='Data Table'),
        dash_table.DataTable(
            df_show.to_dict('records'),
            [{"name": i, "id": i} for i in df_show.columns],
            page_size=100,
            page_current=0,
            filter_action="native",
            sort_action='native',
            sort_mode='multi',
            style_table={
                'overflow': 'scroll',
                'width': '100%',
                'height': '300px',
            },
            style_cell={'textAlign': 'left'},
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'borderBottom': '1px solid black'
            },
        ),
        dcc.Graph(
            id="graph_1",
            config=GRAPH_CONFIG,
            figure=fig1
        ),
        dcc.Graph(
            id="graph_2",
            config=GRAPH_CONFIG,
            figure=fig2
        ),
        dcc.Graph(
            id="graph_3",
            config=GRAPH_CONFIG,
            figure=fig3
        ),
        dcc.Graph(
            id="graph_4",
            config=GRAPH_CONFIG,
            figure=fig4
        ),
        # dcc.Graph(
        #     id="graph_5",
        #     config=GRAPH_CONFIG,
        #     figure=fig5
        # ),

    ])
