# The Timeline Page
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from app import app, artworkSet

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import io
import numpy as np

print("Getting the timeline ready:")
df = artworkSet
df[['Ayear', 'Amonth', 'Aday']] = df['DateAcquired'].str.split('-', expand=True)
#df['nDate'].describe()
ref = pd.pivot_table(df, index = 'Department', aggfunc = 'count')
ref = ref.to_records()
ref = pd.DataFrame(ref)
slist = list(ref['Department'])

C = 'Ayear'

def pivtodf(dfx,cat):
    dfx = df[df['Department'] == slist[cat]]
    dfx = pd.pivot_table(dfx,index = C,aggfunc = 'count')
    dfx = dfx.to_records()
    dfx = pd.DataFrame(dfx)
    dfx = dfx[[C,'ConstituentID_x']]
    dfx = dfx.rename(index = str, columns = {'ConstituentID_x':slist[cat]})
    return dfx

ArcD = pivtodf(df,1)
ArcP = pivtodf(df,2)
Drw = pivtodf(df,3)
Flm = pivtodf(df,4)
Flx = pivtodf(df,5)
MP = pivtodf(df,6)
PS = pivtodf(df,7)
Ptg = pivtodf(df,8)
PI = pivtodf(df,9)

clump = pd.merge(ArcD,Drw, how = 'left', on = C)
clump = pd.merge(clump,Flm, how = 'left', on = C)
clump = pd.merge(clump,Flx, how = 'left', on = C)
clump = pd.merge(clump,MP, how = 'left', on = C)
clump = pd.merge(clump,Ptg, how = 'left', on = C)
clump = pd.merge(clump,PI, how = 'left', on = C)
clump = pd.merge(clump,PS, how = 'left', on = C)

MD = 'lines'

trace1 = go.Scatter(
    x=ArcD[C],
    y=ArcD[slist[1]],
    name=slist[1],
    mode = MD
)
trace2 = go.Scatter(
    x=Drw[C],
    y=Drw[slist[3]],
    name=slist[3],
    mode = MD
)
trace3 = go.Scatter(
    x=Flm[C],
    y=Flm[slist[4]],
    name=slist[4],
    mode = MD
)
trace4 = go.Scatter(
    x=Flx[C],
    y=Flx[slist[5]],
    name=slist[5],
    mode = MD
)
trace5 = go.Scatter(
    x=MP[C],
    y=MP[slist[6]],
    name=slist[6],
    mode = MD
)
trace6 = go.Scatter(
    x=Ptg[C],
    y=Ptg[slist[8]],
    name=slist[8],
    mode = MD
)
trace7 = go.Scatter(
    x=PI[C],
    y=PI[slist[9]],
    name=slist[9],
    mode = MD
)
trace8 = go.Scatter(
    x=PS[C],
    y=PS[slist[7]],
    name=slist[7],
    mode = MD

)



finalData = [trace1, trace2,trace3,trace4,trace5,trace7,trace8]
finalLayout = go.Layout(
    barmode='stack',
    autosize=False,
    width=900,
    height=900,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
)

# please change this variable name
page_2_layout = html.Div([
    html.H1('Timeline of Acquired Works'),
    dcc.Graph(
        id='timeline1',
        figure={
            'data': finalData,
            'layout': finalLayout
        }
    ),
    html.Div(id='timeline-content'),
    html.Br()
])

@app.callback(dash.dependencies.Output('timeline-content', 'children'),
              [dash.dependencies.Input('timeline-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)
