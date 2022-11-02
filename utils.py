#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    utils.py
# @Author:      Kuro
# @Time:        10/31/2022 3:25 PM

import pandas as pd

import plotly.express as px
from scipy.stats.mstats_basic import winsorize
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

GRAPH_CONFIG = dict({
    # "scrollZoom": True,
    "displayModeBar": True,
    # "staticPlot": True
    # "displaylogo": False,
    # "modeBarButtonsToRemove": ["zoom", "zoomin", "zoomout"],
})


def preprocess_df(path):
    df = pd.read_csv(path)
    df.head()
    df.fillna(df.mean(), inplace=True)

    df = df.rename(
        columns={'Country': 'country', 'Year': 'year', 'Status': 'status', 'Life expectancy ': 'life_expectancy',
                 'Adult Mortality': 'adult_mortality',
                 'infant deaths': 'infant_death', 'Alcohol': 'alcohol',
                 'percentage expenditure': 'percentage_expenditure', 'Hepatitis B': 'Hepatitis_b',
                 'Measles ': 'measles', ' BMI ': 'bmi', 'under-five deaths ': 'under_five_deaths', 'Polio': 'polio',
                 'Total expenditure': 'total_expenditure', 'Diphtheria ': 'diphtheria', ' HIV/AIDS': 'hiv_Aids',
                 'GDP': 'gdp', 'Population': 'population',
                 ' thinness  1-19 years': 'thinness_1_to_19', ' thinness 5-9 years': 'thinness_5_to_9',
                 'Income composition of resources': 'income_composition_of_resources', 'Schooling': 'schooling'})

    return df


def transform_outliers(data, col, lower_limit=0, upper_limit=0):
    data[col] = winsorize(data[col], limits=(lower_limit, upper_limit))
    return data[col]


def remove_outlier(df_non_outliers):
    col_list = list(df_non_outliers.columns)[3:]
    df_non_outliers[col_list[0]] = transform_outliers(df_non_outliers, col_list[0], lower_limit=.01)
    df_non_outliers[col_list[1]] = transform_outliers(df_non_outliers, col_list[1], upper_limit=.04)
    df_non_outliers[col_list[2]] = transform_outliers(df_non_outliers, col_list[2], upper_limit=0.2)
    df_non_outliers[col_list[3]] = transform_outliers(df_non_outliers, col_list[3], upper_limit=.0025)
    df_non_outliers[col_list[4]] = transform_outliers(df_non_outliers, col_list[4], upper_limit=.135)
    df_non_outliers[col_list[5]] = transform_outliers(df_non_outliers, col_list[5], lower_limit=.15)
    df_non_outliers[col_list[6]] = transform_outliers(df_non_outliers, col_list[6], upper_limit=0.2)
    df_non_outliers[col_list[6]] = transform_outliers(df_non_outliers, col_list[7], upper_limit=0)
    df_non_outliers[col_list[7]] = transform_outliers(df_non_outliers, col_list[8], upper_limit=0.15)
    df_non_outliers[col_list[8]] = transform_outliers(df_non_outliers, col_list[9], lower_limit=0.1)
    df_non_outliers[col_list[9]] = transform_outliers(df_non_outliers, col_list[10], upper_limit=0.02)
    df_non_outliers[col_list[10]] = transform_outliers(df_non_outliers, col_list[11], lower_limit=0.11)
    df_non_outliers[col_list[11]] = transform_outliers(df_non_outliers, col_list[12], upper_limit=0.2)
    df_non_outliers[col_list[12]] = transform_outliers(df_non_outliers, col_list[13], upper_limit=0.12)
    df_non_outliers[col_list[13]] = transform_outliers(df_non_outliers, col_list[14], upper_limit=0.1)
    df_non_outliers[col_list[14]] = transform_outliers(df_non_outliers, col_list[15], upper_limit=0.05)
    df_non_outliers[col_list[15]] = transform_outliers(df_non_outliers, col_list[16], upper_limit=0.05)
    df_non_outliers[col_list[16]] = transform_outliers(df_non_outliers, col_list[17], lower_limit=0.06)
    df_non_outliers[col_list[17]] = transform_outliers(df_non_outliers, col_list[18], lower_limit=0.04, upper_limit=0.07)
    return df_non_outliers


def encode_data(df):
    le = preprocessing.LabelEncoder()

    obj_col = df.select_dtypes(include="object").columns
    for col in obj_col:
        df[col] = le.fit_transform(df[col])
    return df


def split_data(X, y, ratio):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio, random_state=7)
    return X_train, X_test, y_train, y_test


def scale_data(X_train, X_test):
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test


def df_plot(df):
    fig1 = px.histogram(df, x='life_expectancy', template='ggplot2', title='Life Expectancy')
    fig2 = px.violin(df, x='status', y='life_expectancy', template='ggplot2', color='status', box=True, title='Life Expectancy on the Basis of Country Status')
    fig3 = px.line((df.sort_values(by='year')), x='year', y='life_expectancy',
                   animation_frame='country', animation_group='year', color='country', range_y=[40, 100],
                   markers=True, template='ggplot2', title='Country Wise Life Expectancy over the years')
    fig4 = px.scatter(df.sort_values(by='year'), x='life_expectancy', y='infant_death', color='country',
                      animation_frame='year', animation_group='country',
                      size='year', template='ggplot2', title='Life expectancy VS Infant Death of Countries')
    # fig5 = px.scatter_3d(df.sort_values(by='year'), x='life_expectancy', y='adult_mortality',
    #                      z='infant_death', size='life_expectancy', template='ggplot2', color='country',
    #                      title='Life Expectancy Vs Adult Mortality in Countries')
    fig5 = None
    return fig1, fig2, fig3, fig4, fig5


df = preprocess_df('Life Expectancy Data.csv')
fig1, fig2, fig3, fig4, fig5 = df_plot(df)
df_train = remove_outlier(df)
df_train = encode_data(df_train)
X = df_train.drop('life_expectancy', axis=1)
y = df_train['life_expectancy']
