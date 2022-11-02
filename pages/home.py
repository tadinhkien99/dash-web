#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    home.py
# @Author:      Kuro
# @Time:        11/1/2022 9:37 AM

from dash import html


def home():
    return html.Div(children=[
        html.H1(children='This is our Home page'),

    ])
