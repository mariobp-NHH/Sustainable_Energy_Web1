from dash import Dash, html, dcc
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

colors= {
    "c": "rgb(38, 70, 83)", #"charcoal"
    "p-g": "rgb(42, 157, 143)", #"persian-green"
    "o-y-c": "rgb(233, 196, 106)", #"orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)", #"sandy-brown"
    "b-s": "rgb(231, 111, 81)" #"burnt-sienna"
    }

from .layout import html_layout
from .parameters import parameters
from .simulations import quantities, bounds_GO, CDF_GO, bounds_spot, CDF_spot, exp_price, plot_exp_price
from .spot_go_figures import fig_area_function, fig_kapital_function, fig_strategies, fig_prices, graph_in


def create_dash_spot_go(flask_app):
    dash_app = Dash(server=flask_app, name="Dashboard", url_base_pathname="/spot_go/",
                    external_stylesheets=[
                        "/static/dash_spot_go.css",
                        "/static/main.css",
                        "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css",
                        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css",
                        "https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.css",
                        "https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
                    ])

    dash_app.index_string = html_layout

    dash_app.layout = html.Div([

        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Label('Demand high-node spot (ah-s)'),
                        dcc.Slider(id="ah_s",
                                   min=7,
                                   max=8,
                                   step=None,
                                   marks={
                                       7: '7',
                                       7.2: '7,2',
                                       7.4: '7.4',
                                       7.6: '7.6',
                                       7.8: '7.8',
                                       8: '8',
                                   },
                                   value=7,
                                   ),

                        html.Label('Demand low-node spot (al-s)'),
                        dcc.Slider(id="al_s",
                                   min=7,
                                   max=8,
                                   step=None,
                                   marks={
                                       7: '7',
                                       7.2: '7,2',
                                       7.4: '7.4',
                                       7.6: '7.6',
                                       7.8: '7.8',
                                       8: '8',
                                   },
                                   value=7,
                                   ),

                        html.Label('Demand high-node GO (ah-go)'),
                        dcc.Slider(id="ah_go",
                                   min=3,
                                   max=4,
                                   step=None,
                                   marks={
                                       3: '3',
                                       3.1: '3.1',
                                       3.2: '3.2',
                                       3.3: '3.3',
                                       3.4: '3.4',
                                       3.5: '3.5',
                                       3.6: '3.6',
                                       3.7: '3.7',
                                       3.8: '3.8',
                                       3.9: '3.9',
                                       4: '4',
                                   },
                                   value=3.5,
                                   ),

                        html.Label('Demand low-node GO (al-go)'),
                        dcc.Slider(id="al_go",
                                   min=3,
                                   max=4,
                                   step=None,
                                   marks={
                                       3: '3',
                                       3.1: '3.1',
                                       3.2: '3.2',
                                       3.3: '3.3',
                                       3.4: '3.4',
                                       3.5: '3.5',
                                       3.6: '3.6',
                                       3.7: '3.7',
                                       3.8: '3.8',
                                       3.9: '3.9',
                                       4: '4',
                                   },
                                   value=3.5,
                                   ),
                    ]),

                    html.Div([
                        html.Label('Green capacity high-node (kh)'),
                        dcc.Slider(id="kh",
                                   min=3,
                                   max=11.1,
                                   step=None,
                                   marks={
                                       3: '3',
                                       3.5: '3.5',
                                       4: '4',
                                       4.5: '4.5',
                                       5: '5',
                                       5.5: '5.5',
                                       6: '6',
                                       6.5: '6.5',
                                       7: '7',
                                       7.5: '7.5',
                                       8: '8',
                                       8.5: '8.5',
                                       9: '9',
                                       9.5: '9.5',
                                       10: '10',
                                       10.5: '10.5',
                                       11.1: '11.1',
                                   },
                                   value=11.1,
                                   ),

                        html.Label('Green capacity low-node (kl)'),
                        dcc.Slider(id="kl",
                                   min=3,
                                   max=11.1,
                                   step=None,
                                   marks={
                                       3: '3',
                                       3.5: '3.5',
                                       4: '4',
                                       4.5: '4.5',
                                       5: '5',
                                       5.5: '5.5',
                                       6: '6',
                                       6.5: '6.5',
                                       7: '7',
                                       7.5: '7.5',
                                       8: '8',
                                       8.5: '8.5',
                                       9: '9',
                                       9.5: '9.5',
                                       10: '10',
                                       10.5: '10.5',
                                       11.1: '11.1',
                                   },
                                   value=11.1,
                                   ),
                    ]),

                    html.Div([
                        html.Label('Plot'),
                        dcc.RadioItems(id='plot',
                                       options=[
                                           {'label': 'Strategies', 'value': 'strategies'},
                                           {'label': 'Prices', 'value': 'prices'}
                                       ],
                                       value='strategies',
                                       labelStyle={'display': 'inline-block'},
                                       className="char-btn1"
                                       ),

                        html.Label('Cases'),
                        dcc.RadioItems(id='cases',
                                       options=[
                                           {'label': 'Pool GO', 'value': 'case1'},
                                           {'label': 'Separated GO', 'value': 'case2'},
                                           {'label': 'Green capacity', 'value': 'case3'}
                                       ],
                                       value='case2',
                                       labelStyle={'display': 'inline-block'},
                                       className="char-btn2"
                                       ),
                    ]),

                ], className="box"),
                html.Div([
                    dcc.Graph(
                        id="fig_demand",
                        figure={
                            "layout": {
                                "title": "Spot market"
                            }
                        }
                    ),
                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig_kapital",
                        figure={
                            "layout": {"title": "GO market"}
                        }
                    ),
                ], className="box"),

            ], className="section_developers3_css"),
        ], className="container"),

        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(
                        id="fig1",
                        figure={
                            "layout": {
                                "title": "Discriminatory, ex-ante (strategies)"
                            }
                        }
                    ),
                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig2",
                        figure={
                            "layout": {
                                "title": "Discriminatory, ex-ante \ ex-post (strategies)"
                            }
                        }
                    ),
                ], className="box"),

                html.Div([
                    dcc.Graph(
                        id="fig3",
                        figure={
                            "layout": {
                                "title": "Discriminatory, ex-post (strategies)"
                            }
                        }
                    ),
                ], className="box"),
            ], className="section_developers3_css"),
        ], className="container"),

    ], className="container")

    # Initialize callbacks after our app is loaded
    # Pass dash_app as a parameter
    init_callbacks(dash_app)

    return dash_app

def init_callbacks(dash_app):


    @dash_app.callback(
        [
            Output('fig_demand', 'figure'),
            Output('fig_kapital', 'figure'),
            Output("fig1", "figure"),
            Output("fig2", "figure"),
            Output("fig3", "figure")
        ],
        [
            Input('ah_s', 'value'),
            Input('al_s', 'value'),
            Input('ah_go', 'value'),
            Input('al_go', 'value'),
            Input('kh', 'value'),
            Input('kl', 'value'),
            Input('plot', 'value'),
            Input('cases', 'value'),
        ]
    )
    def update_graph(a_input, b_input, c_input, d_input, e_input, f_input, g_input, h_input):
        # Get parameters
        ah, al, ah_go, al_go, kh, kl, plot, cases, T, pmaxs, pmaxgo, N, N2 = parameters(
            a_input, b_input, c_input, d_input, e_input, f_input, g_input, h_input)

        # Quantities
        q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, al, ah_go,
                                                                                                        al_go, T, cases)
        # GO1:
        b11go, b12go, b1go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch=1)
        F1go1, F1go2, pgo1 = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, b1go, pmaxgo,
                                    branch=1)
        E1go1, E1go2 = exp_price(F1go1, F1go2, pgo1)
        # GO2:
        b21go, b22go, b2go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch=2)
        F2go1, F2go2, pgo2 = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, b2go, pmaxgo,
                                    branch=2)
        E2go1, E2go2 = exp_price(F2go1, F2go2, pgo2)
        # Spot
        b1sgo, b2sgo, bsgo = bounds_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, b1go, b2go, pmaxs)
        F1sgo, F2sgo, psgo = CDF_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, N, bsgo, b1go, b2go, pmaxs)
        E1sgo, E2sgo = exp_price(F1sgo, F2sgo, psgo)
        b1s, b2s, bs = bounds_spot(q11, q12, q21, q22, 0, 0, 0, 0, 0, 0, pmaxs)
        F1s, F2s, ps = CDF_spot(q11, q12, q21, q22, 0, 0, 0, 0, N, bs, 0, 0, pmaxs)
        E1s, E2s = exp_price(F1s, F2s, ps)
        # GO1 Price
        E1go1_lst, E1go2_lst, a2_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, cases, branch=1)
        # Spot Price
        Esgo1_lst, Esgo2_lst, a2_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, cases, branch=0)
        Es1_lst, Es2_lst, a2_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, cases, branch=-1)
        # GO2 Price
        E2go1_lst, E2go2_lst, a2_lst = plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, cases, branch=2)

        fig_demand, fig_kapital, fig1, fig2, fig3 = graph_in(plot, ah, al, ah_go, al_go,
                                                             kh, kl,
                                                             pgo1, F1go1, F1go2, E1go1, E1go2,
                                                             pgo2, F2go1, F2go2, E2go1, E2go2,
                                                             psgo, F1sgo, F2sgo, E1sgo, E2sgo,
                                                             ps, F1s, F2s, E1s, E2s,
                                                             pmaxgo, pmaxs, a2_lst, E1go1_lst, E1go2_lst,
                                                             Esgo1_lst, Esgo2_lst,
                                                             Es1_lst, Es2_lst,
                                                             E2go1_lst, E2go2_lst)

        return fig_demand, fig_kapital, fig1, fig2, fig3
