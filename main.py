#!/usr/bin/python 

"""
Creator: Raghul

"""

import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
import plotly.io as pio
import os
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output


USERNAME_PASSWORD_PAIRS = [['bobo','bobo'],['username','password']]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Launch the application:
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

server = app.server


app.css.append_css({'external_url': './assets/body.css'})

colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}



# Create a DataFrame from the .csv file:
df1 = pd.read_csv('file_path.csv')
df2 = pd.read_csv('file_path.csv')
df3 = pd.read_csv('file_path.csv')
df4 = pd.read_csv('file_path.csv')
df5 = pd.read_csv('file_path.csv')
df6 = pd.read_csv('file_path.csv')






valuesof410_Th_three = df3.columns[1:16]
valuesof410_Pl_three = df3.columns[16:31]
valuesof400_Th_three = df3.columns[32:47]
valuesof400_Pl_three = df3.columns[47:62]

valuesof410_Th_four = df4.columns[1:16]
valuesof400_Th_four = df4.columns[17:32]

valuesof410_Th_five = df5.columns[1:16]
valuesof410_Pl_five = df5.columns[16:31]
valuesof400_Th_five = df5.columns[32:47]
valuesof400_Pl_five = df5.columns[47:62]

valuesof410_Th_six = df6.columns[1:16]
valuesof400_Th_six = df6.columns[17:32]




traces = go.Scatter(
    x = df1["Date"],
    y = df1["wget_avg"],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df1["wget_avg"] - df1["400_wget_avg"])/df1["400_wget_avg"])*100)),
            ),
    mode = 'markers+lines',
    name = 'Latest',
    text = df1["410_version"],
    marker={
        'size': 15,
        'opacity': 0.5,
        'line': {'width': 1, 'color': 'white'}
        },
) 


traces2 = go.Scatter(
    x = df1["Date"],
    y = df1["400_wget_avg"],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df1["400_version"],
) 


traces3 = go.Scatter(
    x = df2["Date"],
    y = df2["wget_avg"],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df2["wget_avg"]- df2["400_wget_avg"])/df2["400_wget_avg"])*100)),
            ),    
    mode = 'markers+lines',
    name = 'Latest',
    text = df2["410_version"],
    marker={
        'size': 15,
        'opacity': 0.5,
        'line': {'width': 1, 'color': 'white'}
        },
) 


traces4 = go.Scatter(
    x = df2["Date"],
    y = df2["400_wget_avg"],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df2["400_version"],
) 




#####################################
#                                   #
#                                   #
#           Declaring tabs          #
#                                   #
#                                   #
#####################################

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[

##### Tab - 1 #####

        dcc.Tab(label='Wget L2', value='tab-1'),


##### Tab - 2 #####

        dcc.Tab(label='Wget L3', value='tab-2'),

##### Tab - 3 #####

        dcc.Tab(label='Iperf - UDP ', value='tab-3',
            children = html.Div([
                html.Div([

                    dcc.Dropdown(
                        id='Dropdown410_Throughput_three',
                        options=[{'label': i.title()+' - Latest 410 --> Throughput', 'value': i} for i in valuesof410_Th_three],
                        value='410Ths10bw50'
                    )
                ],
                style={'width': '48%', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown410_Percentloss_three',
                        options=[{'label': i.title()+' - Latest 410 --> Percentage loss', 'value': i} for i in valuesof410_Pl_three],
                        value='410s10b50'
                    )
                ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown400_Throughput_three',
                        options=[{'label': i.title()+' - Latest 400 --> Throughput', 'value': i} for i in valuesof400_Th_three],
                        value='400Ths10bw50'
                    )
                ],style={'width': '48%', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown400_Percentloss_three',
                        options=[{'label': i.title()+' - Latest 400 --> Percentage loss', 'value': i} for i in valuesof400_Pl_three],
                        value='400s10b50'
                    )
                ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),


            dcc.Graph(id='Thruput_graph_three'),
            dcc.Graph(id='Percentloss_graph_three')
            ], style={'padding':10,'textAlign': 'center','plot_bgcolor':colors['background'],'paper_bgcolor':colors['background']})),


##### Tab - 4 #####

        dcc.Tab(label='Iperf - TCP ', value='tab-4',
            children = html.Div([
                html.Div([

                    dcc.Dropdown(
                        id='Dropdown410_Throughput_four',
                        options=[{'label': i.title()+' - Latest 410 --> Throughput', 'value': i} for i in valuesof410_Th_four],
                        value='410Ths10bw50'
                    )
                ],
                style={'width': '48%', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown400_Throughput_four',
                        options=[{'label': i.title()+' - Latest 400 --> Throughput', 'value': i} for i in valuesof400_Th_four],
                        value='400Ths10bw50'
                    )
                ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

            dcc.Graph(id='Thruput_graph_four'),

            ], style={'padding':10,'textAlign': 'center','plot_bgcolor':colors['background'],'paper_bgcolor':colors['background']})),


##### Tab - 5 #####

        dcc.Tab(label='Iperf - UDP - L2', value='tab-5',
            children = html.Div([
                html.Div([
                    dcc.Dropdown(
                        id='Dropdown410_Throughput_five',
                        options=[{'label': i.title()+' - Latest 410 --> Throughput', 'value': i} for i in valuesof410_Th_five],
                        value='410Ths10bw50'
                    )
                ],
                style={'width': '48%', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown410_Percentloss_five',
                        options=[{'label': i.title()+' - Latest 410 --> Percentage loss', 'value': i} for i in valuesof410_Pl_five],
                        value='410s10b50'
                    )
                ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown400_Throughput_five',
                        options=[{'label': i.title()+' - Latest 400 --> Throughput', 'value': i} for i in valuesof400_Th_five],
                        value='400Ths10bw50'
                    )
                ],style={'width': '48%', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown400_Percentloss_five',
                        options=[{'label': i.title()+' - Latest 400 --> Percentage loss', 'value': i} for i in valuesof400_Pl_five],
                        value='400s10b50'
                    )
                ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),


            dcc.Graph(id='Thruput_graph_five'),
            dcc.Graph(id='Percentloss_graph_five')
            ], style={'padding':10,'textAlign': 'center','plot_bgcolor':colors['background'],'paper_bgcolor':colors['background']})),


##### Tab - 6 #####


        dcc.Tab(label='Iperf - TCP - L2', value='tab-6',
            children = html.Div([
                html.Div([

                    dcc.Dropdown(
                        id='Dropdown410_Throughput_six',
                        options=[{'label': i.title()+' - Latest 410 --> Throughput', 'value': i} for i in valuesof410_Th_six],
                        value='410Ths10bw50'
                    )
                ],
                style={'width': '48%', 'display': 'inline-block'}),

                html.Div([

                    dcc.Dropdown(
                        id='Dropdown400_Throughput_six',
                        options=[{'label': i.title()+' - Latest 400 --> Throughput', 'value': i} for i in valuesof400_Th_six],
                        value='400Ths10bw50'
                    )
                ],style={'width': '48%', 'float': 'right' ,'display': 'inline-block'}),

            dcc.Graph(id='Thruput_graph_six'),

            ], style={'padding':10,'textAlign': 'center','plot_bgcolor':colors['background'],'paper_bgcolor':colors['background']})

        ),



    ],colors={
        "border": "white",
        "primary": "#7FDBFF",
        "background": "#7FDBFF"
        
    }),
    html.Div(id='tabs-content')
],style={'backgroundColor':'#000000'})


#####################################
#                                   #
#                                   #
#            Wget - L3              #
#                                   #
#                                   #
#####################################


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])


def render_content(tab):
    if tab == 'tab-1':

        return html.Div([
            #importing TABLE to the Dash Board
            #dash_table.DataTable(
                #id='table',
                #columns=[{"name": i, "id": i} for i in df1.columns],
                #data=df1.to_dict('records'),
            #),
            dcc.Graph(
                id='Wget L3 Comparison',
                figure={
                    'data': [traces,traces2],


            'layout':go.Layout(
                title=go.layout.Title(
                    text='L3  -  Average Speed after performing wget on a 100mb file 10 times for Latest Old Version and Latest',
                    xref='paper',
                    font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
                plot_bgcolor=colors['background'],
                paper_bgcolor=colors['background'],
                #fontcolor=colors['text'],
                xaxis=go.layout.XAxis(
                    title=go.layout.xaxis.Title(
                        text='Date',
                        font=dict(
                            family='Courier New, monospace',
                            size=18,
                            color=colors['text']
                        )
                    ),
                    linecolor='#7FDBFF',
                    linewidth=1,
                    tickcolor='#7FDBFF',
                    tickfont=dict(
                        size=14,
                        color='#7FDBFF'
                    )
                ),
                yaxis=go.layout.YAxis(
                    title=go.layout.yaxis.Title(
                        text='Speed in Mb/s',
                        font=dict(
                            family='Courier New, monospace',
                            size=18,
                            color=colors['text']
                        )
                    ),
                    linecolor='#7FDBFF',
                    linewidth=1,
                    tickcolor='#7FDBFF',
                    tickfont=dict(
                        size=14,
                        color='#7FDBFF'
                        )
                ),
                legend=dict(
                    traceorder='normal',
                    font=dict(
                        family='sans-serif',
                        size=16,
                        color='#7FDBFF',
                    ),
                    bordercolor='#FFFFFF',
                    borderwidth=2
                )
            )
        }
    ),
])

#####################################
#                                   #
#                                   #
#            Wget - L2              #
#                                   #
#                                   #
#####################################   

    elif tab == 'tab-2':
        return html.Div([
                dcc.Graph(
                    id='Wget L2 Comparison',
                    figure={
                        'data': [traces3,traces4],
            

            'layout':go.Layout(
                title=go.layout.Title(
                    text='L2  -  Average Speed after performing wget on a 100mb file 10 times for Latest Old Version and Latest',
                    xref='paper',
                    font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
                plot_bgcolor=colors['background'],
                paper_bgcolor=colors['background'],
                #fontcolor=colors['text'],
                xaxis=go.layout.XAxis(
                    title=go.layout.xaxis.Title(
                        text='Date',
                        font=dict(
                            family='Courier New, monospace',
                            size=18,
                            color=colors['text']
                        )
                    ),
                    linecolor='#7FDBFF',
                    linewidth=1,
                    tickcolor='#7FDBFF',
                    tickfont=dict(
                        size=14,
                        color='#7FDBFF'
                    )
                ),
                yaxis=go.layout.YAxis(
                    title=go.layout.yaxis.Title(
                        text='Speed in Mb/s',
                        font=dict(
                            family='Courier New, monospace',
                            size=18,
                            color=colors['text']
                        )
                    ),
                    linecolor='#7FDBFF',
                    linewidth=1,
                    tickcolor='#7FDBFF',
                    tickfont=dict(
                        size=14,
                        color='#7FDBFF'
                        )
                ),
                legend=dict(
                    traceorder='normal',
                    font=dict(
                        family='sans-serif',
                        size=16,
                        color='#7FDBFF',
                    ),
                    bordercolor='#FFFFFF',
                    borderwidth=2
                )
            )
        }
    )    
])




#####################################
#                                   #
#                                   #
#      Iperf - L3    - UDP          #
#                                   #
#                                   #
#####################################


@app.callback(
    Output('Thruput_graph_three', 'figure'),
    [Input('Dropdown410_Throughput_three', 'value'),
     Input('Dropdown400_Throughput_three', 'value')])

def update_graph(Th410,Th400):

    traces = go.Scatter(
    x = df3["date"],
    y = df3[Th410],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df3[Th410] - df3[Th400])/df3[Th400])*100)),
            ),    
    mode = 'markers+lines',
    marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 1, 'color': 'white'}
            },
    name = 'Latest',
    text = df3["410version"],

    ) 

    traces2 = go.Scatter(
    x = df3["date"],
    y = df3[Th400],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df3["400version"],
    ) 

    return {
        'data': [traces,traces2],
        'layout':go.Layout(
            title=go.layout.Title(
                text='Throughput Comparison of All the Latest with Old Version versions',
                xref='paper',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            #fontcolor=colors['text'],
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Date',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                ),
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Throughput',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                )

            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=16,
                    color='#7FDBFF',
                ),
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )
    }


@app.callback(
    Output('Percentloss_graph_three', 'figure'),
    [Input('Dropdown410_Percentloss_three', 'value'),
     Input('Dropdown400_Percentloss_three', 'value')])

def update_graph(Pl410,Pl400):

    traces3 = go.Scatter(
    x = df3["date"],
    y = df3[Pl410],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df3[Pl410] - df3[Pl400])/df3[Pl400])*100)),
            ),    
    mode = 'markers+lines',
    marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            },
    name = 'Latest',
    text = df3["410version"],

    ) 

    traces4 = go.Scatter(
    x = df3["date"],
    y = df3[Pl400],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df3["400version"],
    ) 

    return {
        'data': [traces3,traces4],
        'layout':go.Layout(
            title=go.layout.Title(
                text='Percentage_loss Comparison of All the Latest with Old Version versions',
                xref='paper',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            #fontcolor=colors['text'],
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Date',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                    

                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                )

            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Percentage Loss',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),

                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                ),
                ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=16,
                    color='#7FDBFF'
                ),
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )
    }



#####################################
#                                   #
#                                   #
#      Iperf - L3    - TCP          #
#                                   #
#                                   #
#####################################

@app.callback(
    Output('Thruput_graph_four', 'figure'),
    [Input('Dropdown410_Throughput_four', 'value'),
     Input('Dropdown400_Throughput_four', 'value')])

def update_graph(Th410,Th400):

    traces = go.Scatter(
    x = df4["date"],
    y = df4[Th410],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df4[Th410] - df4[Th400])/df4[Th400])*100)),
            ),
    mode = 'markers+lines',
    marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 1, 'color': 'white'}
            },
    name = 'Latest',
    text = df4["410version"],

    ) 

    traces2 = go.Scatter(
    x = df4["date"],
    y = df4[Th400],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df4["400version"],
    ) 

    return {
        'data': [traces,traces2],
        'layout':go.Layout(
            title=go.layout.Title(
                text='Throughput Comparison of All the Latest with Old Version versions',
                xref='paper',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            #fontcolor=colors['text'],
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Date',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                ),
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Throughput',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                )

            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=16,
                    color='#7FDBFF',
                ),
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )
    }

#####################################
#                                   #
#                                   #
#      Iperf - L2    - UDP          #
#                                   #
#                                   #
#####################################

@app.callback(
    Output('Thruput_graph_five', 'figure'),
    [Input('Dropdown410_Throughput_five', 'value'),
     Input('Dropdown400_Throughput_five', 'value')])

def update_graph(Th410,Th400):

    traces = go.Scatter(
    x = df5["date"],
    y = df5[Th410],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df5[Th410] - df5[Th400])/df5[Th400])*100)),
            ),
    mode = 'markers+lines',
    marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 1, 'color': 'white'}
            },
    name = 'Latest',
    text = df5["410version"],

    ) 

    traces2 = go.Scatter(
    x = df5["date"],
    y = df5[Th400],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df5["400version"],
    ) 

    return {
        'data': [traces,traces2],
        'layout':go.Layout(
            title=go.layout.Title(
                text='Throughput Comparison of All the Latest with Old Version versions',
                xref='paper',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            #fontcolor=colors['text'],
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Date',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                ),
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Throughput',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                )

            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=16,
                    color='#7FDBFF',
                ),
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )
    }


@app.callback(
    Output('Percentloss_graph_five', 'figure'),
    [Input('Dropdown410_Percentloss_five', 'value'),
     Input('Dropdown400_Percentloss_five', 'value')])

def update_graph(Pl410,Pl400):

    traces3 = go.Scatter(
    x = df5["date"],
    y = df5[Pl410],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df5[Pl410] - df5[Pl400])/df5[Pl400])*100)),
            ),
    mode = 'markers+lines',
    marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            },
    name = 'Latest',
    text = df5["410version"],

    ) 

    traces4 = go.Scatter(
    x = df5["date"],
    y = df5[Pl400],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df5["400version"],
    ) 

    return {
        'data': [traces3,traces4],
        'layout':go.Layout(
            title=go.layout.Title(
                text='Percentage_loss Comparison of All the Latest with Old Version versions',
                xref='paper',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            #fontcolor=colors['text'],
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Date',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                    

                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                )

            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Percentage Loss',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),

                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                ),
                ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=16,
                    color='#7FDBFF'
                ),
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )
    }

#####################################
#                                   #
#                                   #
#      Iperf - L2    - TCP          #
#                                   #
#                                   #
#####################################
@app.callback(
    Output('Thruput_graph_six', 'figure'),
    [Input('Dropdown410_Throughput_six', 'value'),
     Input('Dropdown400_Throughput_six', 'value')])

def update_graph(Th410,Th400):

    traces = go.Scatter(
    x = df6["date"],
    y = df6[Th410],
    error_y=dict(
            type='data',
            symmetric=False,
            visible=True,
            array=(round(((df6[Th410] - df6[Th400])/df6[Th400])*100)),
            ),
    mode = 'markers+lines',
    marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 1, 'color': 'white'}
            },
    name = 'Latest',
    text = df6["410version"],

    ) 

    traces2 = go.Scatter(
    x = df6["date"],
    y = df6[Th400],
    mode = 'markers+lines',
    name = 'Old Version',
    text = df6["400version"],
    ) 

    return {
        'data': [traces,traces2],
        'layout':go.Layout(
            title=go.layout.Title(
                text='Throughput Comparison of All the Latest with Old Version versions',
                xref='paper',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color=colors['text'])),
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            #fontcolor=colors['text'],
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Date',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                ),
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Throughput',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color=colors['text']
                    )
                ),
                linecolor='#7FDBFF',
                linewidth=1,
                tickcolor='#7FDBFF',
                tickfont=dict(
                    size=14,
                    color='#7FDBFF'
                )

            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='sans-serif',
                    size=16,
                    color='#7FDBFF',
                ),
                bordercolor='#FFFFFF',
                borderwidth=2
            )
        )
    }



# Add the server clause:
if __name__ == '__main__':
    app.run_server(debug=True)
