from dash import Dash, html, dcc
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_defer_js_import as dji

import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

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
                        "https://pro.fontawesome.com/releases/v5.10.0/css/all.css",
                        "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css",
                        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/monokai-sublime.min.css"
                    ],
                    external_scripts=external_scripts)

    mathjax_script = dji.Import(src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_SVG")

    dash_app.index_string = html_layout

    dash_app.layout = html.Div([

        html.Div([
            html.Div([
                html.Div([

                    html.Div([
                        html.Div([
                            html.Label('Demand node 1, spot ($a_1^s$)'),
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

                            html.Label('Demand node 2, spot ($a_2^s$)'),
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

                            html.Label('Demand node 1, GO ($a_1^{go}$)'),
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

                            html.Label('Demand node 2, GO ($a_2^{go}$)'),
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
                        ], className="menu_box"),

                        html.Div([
                            html.Label('Green capacity node 1 ($\\alpha_1$)'),
                            dcc.Slider(id="kh",
                                       min=0.5,
                                       max=1,
                                       step=None,
                                       marks={
                                           0.5: '0.5',
                                           0.6: '0.6',
                                           0.7: '0.7',
                                           0.8: '0.8',
                                           0.9: '0.9',
                                           1: '1',
                                       },
                                       value=0.5,
                                       ),

                            html.Label('Green capacity node 2 ($\\alpha_2$)'),
                            dcc.Slider(id="kl",
                                       min=0.5,
                                       max=1,
                                       step=None,
                                       marks={
                                           0.5: '0.5',
                                           0.6: '0.6',
                                           0.7: '0.7',
                                           0.8: '0.8',
                                           0.9: '0.9',
                                           1: '1',
                                       },
                                       value=0.5,
                                       ),
                        ], className="menu_box"),

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
                                               {'label': 'GO, no-constraint', 'value': 'case1'},
                                               {'label': 'GO, constraint', 'value': 'case2'}
                                           ],
                                           value='case1',
                                           labelStyle={'display': 'inline-block'},
                                           className="char-btn1"
                                           ),
                        ], className="menu_box"),
                    ], className="spot_go_menu_css"),

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

            ], className="spot_go_section_developers3_css"),
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
            ], className="spot_go_section_developers3_css"),
        ], className="container"),
        mathjax_script
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
