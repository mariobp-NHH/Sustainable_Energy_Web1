# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:51:20 2021

@author: s14761
"""
import plotly.graph_objects as go

colors = {
    "c": "rgb(38, 70, 83)",  # "charcoal"
    "p-g": "rgb(42, 157, 143)",  # "persian-green"
    "o-y-c": "rgb(233, 196, 106)",  # "orange-yellow-crayola"
    "s-b": "rgb(244, 162, 97)",  # "sandy-brown"
    "b-s": "rgb(231, 111, 81)"  # "burnt-sienna"
}


def graph_in(plot, ah, al, ah_go, al_go,
             kh, kl,
             pgo1, F1go1, F1go2, E1go1, E1go2,
             pgo2, F2go1, F2go2, E2go1, E2go2,
             psgo, F1sgo, F2sgo, E1sgo, E2sgo,
             ps, F1s, F2s, E1s, E2s,
             pmaxgo, pmaxs, a2_lst, E1go1_lst, E1go2_lst,
             Esgo1_lst, Esgo2_lst,
             Es1_lst, Es2_lst,
             E2go1_lst, E2go2_lst):
    # Fig area:
    fig_demand = fig_area_function(ah, al, ah_go, al_go)
    # Fig kapital:
    fig_kapital = fig_kapital_function(kh, kl)
    # Figures 1-3:
    if plot == 'strategies':
        fig1, fig2, fig3 = fig_strategies(pgo1, F1go1, F1go2, E1go1, E1go2,
                                          pgo2, F2go1, F2go2, E2go1, E2go2,
                                          psgo, F1sgo, F2sgo, E1sgo, E2sgo,
                                          ps, F1s, F2s, E1s, E2s)
    else:
        fig1, fig2, fig3 = fig_prices(al, pmaxgo, pmaxs, a2_lst, E1go1_lst, E1go2_lst,
                                      Esgo1_lst, Esgo2_lst,
                                      Es1_lst, Es2_lst,
                                      E2go1_lst, E2go2_lst)
    return fig_demand, fig_kapital, fig1, fig2, fig3

def fig_area_function(ah, al, ah_go, al_go):
    fig_demand = go.Figure()
    fig_demand.update_layout(title={
        'text': "Demands",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    fig_demand.update_yaxes(range=[2.5, 9.5])
    fig_demand.update_xaxes(range=[0, 16])
    fig_demand.update_yaxes(tickvals=[3, 4, 5, 6, 7, 8, 9])
    fig_demand.update_xaxes(tickangle=0, tickvals=[2, 6, 10, 14], ticktext=['ah-s', 'al-s', 'ah-go', 'al-go'])
    fig_demand.update_yaxes(showgrid=False)
    fig_demand.update_xaxes(showgrid=False)

    # ah bar
    fig_demand.add_trace(go.Scatter(
        x=[1, 3], y=[0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))
    fig_demand.add_trace(go.Scatter(
        x=[1, 3], y=[ah, ah],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))

    # al bar
    fig_demand.add_trace(go.Scatter(
        x=[5, 7], y=[0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["o-y-c"]), ))
    fig_demand.add_trace(go.Scatter(
        x=[5, 7], y=[al, al],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["o-y-c"]), ))

    # ah_go bar
    fig_demand.add_trace(go.Scatter(
        x=[9, 11], y=[0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["c"]), ))
    fig_demand.add_trace(go.Scatter(
        x=[9, 11], y=[ah_go, ah_go],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["c"]), ))

    # al_go bar
    fig_demand.add_trace(go.Scatter(
        x=[13, 15], y=[0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["s-b"]), ))
    fig_demand.add_trace(go.Scatter(
        x=[13, 15], y=[al_go, al_go],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["s-b"]), ))

    return fig_demand


def fig_kapital_function(kh, kl):
    fig_kapital = go.Figure()
    fig_kapital.update_layout(title={
        'text': "Green capacity",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    fig_kapital.update_yaxes(range=[2.5, 11.5])
    fig_kapital.update_xaxes(range=[0, 16])
    fig_kapital.update_yaxes(tickvals=[3, 4, 5, 6, 7, 8, 9, 10, 11])
    fig_kapital.update_xaxes(tickangle=0, tickvals=[4, 12], ticktext=['kh', 'kl'])
    fig_kapital.update_yaxes(showgrid=False)
    fig_kapital.update_xaxes(showgrid=False)

    # kh bar
    fig_kapital.add_trace(go.Scatter(
        x=[1, 7], y=[0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))
    fig_kapital.add_trace(go.Scatter(
        x=[1, 7], y=[kh, kh],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["p-g"]), ))

    # kl bar
    fig_kapital.add_trace(go.Scatter(
        x=[9, 15], y=[0, 0],
        showlegend=False,
        fill=None,
        mode='lines',
        line=dict(width=0.5, color=colors["o-y-c"]), ))
    fig_kapital.add_trace(go.Scatter(
        x=[9, 15], y=[kl, kl],
        showlegend=False,
        fill='tonexty',
        mode='lines',
        line=dict(width=0.5, color=colors["o-y-c"]), ))

    return fig_kapital


def fig_strategies(pgo1, F1go1, F1go2, E1go1, E1go2,
                   pgo2, F2go1, F2go2, E2go1, E2go2,
                   psgo, F1sgo, F2sgo, E1sgo, E2sgo,
                   ps, F1s, F2s, E1s, E2s):
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=pgo1, y=F1go1,
                              mode='lines',
                              name='Fh (GO1)',
                              line=dict(color=colors["c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=pgo1, y=F1go2,
                              mode='lines',
                              name='Fl (GO1)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[E1go1, E1go1], y=[0, 1],
                              mode='lines',
                              name='Eh (GO1)',
                              line=dict(color=colors["c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[E1go2, E1go2], y=[0, 1],
                              mode='lines',
                              name='El (GO1)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig1.update_layout(title={
        'text': "GO1 (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig1.update_yaxes(range=[0, 1.1])
    fig1.update_xaxes(range=[0, 2.1])
    fig1.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=psgo, y=F1sgo,
                              mode='lines',
                              name='Fh (S-GO)',
                              line=dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=psgo, y=F2sgo,
                              mode='lines',
                              name='Fl (S-GO)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E1sgo, E1sgo], y=[0, 1],
                              mode='lines',
                              name='Eh (S-GO)',
                              line=dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E2sgo, E2sgo], y=[0, 1],
                              mode='lines',
                              name='El (S-GO)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=ps, y=F1s,
                              mode='lines',
                              opacity=0.4,
                              name='Fh (S)',
                              line=dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=ps, y=F2s,
                              mode='lines',
                              opacity=0.4,
                              name='Fl (S)',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E1s, E1s], y=[0, 1],
                              mode='lines',
                              opacity=0.4,
                              name='Eh (S)',
                              line=dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[E2s, E2s], y=[0, 1],
                              mode='lines',
                              opacity=0.4,
                              name='El (S)',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig2.update_layout(title={
        'text': "Spot-GO (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig2.update_yaxes(range=[0, 1.1])
    fig2.update_xaxes(range=[2, 7.1])
    fig2.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=pgo2, y=F2go1,
                              mode='lines',
                              name='Fh (GO2)',
                              line=dict(color=colors["c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=pgo2, y=F2go2,
                              mode='lines',
                              name='Fl (GO2)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[E2go1, E2go1], y=[0, 1],
                              mode='lines',
                              name='Eh (GO2)',
                              line=dict(color=colors["c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[E2go2, E2go2], y=[0, 1],
                              mode='lines',
                              name='El (GO2)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig3.update_layout(title={
        'text': "GO2 (strategies)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='Price',
        yaxis_title='CDF')
    fig3.update_yaxes(range=[0, 1.1])
    fig3.update_xaxes(range=[0, 2.1])
    fig3.update_xaxes(tickangle=0, tickvals=[0, 1, 2, 3, 4, 5, 6, 7])

    return fig1, fig2, fig3


def fig_prices(al, pmaxgo, pmaxs, a2_lst, E1go1_lst, E1go2_lst,
               Esgo1_lst, Esgo2_lst,
               Es1_lst, Es2_lst,
               E2go1_lst, E2go2_lst):
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=a2_lst, y=E1go1_lst,
                              mode='lines',
                              name='ph (GO1)',
                              line=dict(color=colors["c"], width=1.5)))
    fig1.add_trace(go.Scatter(x=a2_lst, y=E1go2_lst,
                              mode='lines',
                              name='pl (GO1)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig1.add_trace(go.Scatter(x=[al, al], y=[0, pmaxgo],
                              mode='lines',
                              name='al (S)',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig1.update_layout(title={
        'text': "GO1 (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='al (spot)',
        yaxis_title='Price')
    fig1.update_yaxes(range=[0, pmaxgo])
    fig1.update_xaxes(range=[6, 9.1])
    fig1.update_xaxes(tickangle=0, tickvals=[6.1, 6.5, 7, 7.5, 8, 8.5, 9])

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=a2_lst, y=Esgo1_lst,
                              mode='lines',
                              name='ph (S-GO)',
                              line=dict(color=colors["c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=a2_lst, y=Esgo2_lst,
                              mode='lines',
                              name='pl (S-GO)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig2.add_trace(go.Scatter(x=a2_lst, y=Es1_lst,
                              mode='lines',
                              opacity=0.4,
                              name='ph (S)',
                              line=dict(color=colors["p-g"], width=1.5)))
    fig2.add_trace(go.Scatter(x=a2_lst, y=Es2_lst,
                              mode='lines',
                              opacity=0.4,
                              name='pl (S)',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig2.add_trace(go.Scatter(x=[al, al], y=[3, pmaxs],
                              mode='lines',
                              name='al (S)',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig2.update_layout(title={
        'text': "Spot-GO (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='al (spot)',
        yaxis_title='Price')
    fig2.update_yaxes(range=[3, pmaxs])
    fig2.update_xaxes(range=[6, 9.1])
    fig2.update_xaxes(tickangle=0, tickvals=[6.1, 6.5, 7, 7.5, 8, 8.5, 9])

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=a2_lst, y=E2go1_lst,
                              mode='lines',
                              name='ph (GO2)',
                              line=dict(color=colors["c"], width=1.5)))
    fig3.add_trace(go.Scatter(x=a2_lst, y=E2go2_lst,
                              mode='lines',
                              name='pl (GO2)',
                              line=dict(color=colors["s-b"], width=1.5)))
    fig3.add_trace(go.Scatter(x=[al, al], y=[0, pmaxgo],
                              mode='lines',
                              name='al (S)',
                              line=dict(color=colors["o-y-c"], width=1.5)))
    fig3.update_layout(title={
        'text': "GO2 (prices)",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title='al (spot)',
        yaxis_title='Price')
    fig3.update_yaxes(range=[0, pmaxgo])
    fig3.update_xaxes(range=[6, 9.1])
    fig3.update_xaxes(tickangle=0, tickvals=[6.1, 6.5, 7, 7.5, 8, 8.5, 9])

    return fig1, fig2, fig3

