import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
#import dash
from jupyter_dash import JupyterDash
import plotly.express as px
import pandas as pd
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi'],['tejas', 'tejas']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server
 
#code 7
#external hosting -- plot a geoplot generated using plotly  -- additional stuff

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
 
url="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
import pandas as pd
data=pd.read_csv(url)                                #import external data
d1=data.groupby("iso_code",as_index=False)['total_cases'].max()
d1 = d1.dropna(subset=['total_cases'])
d1
#geographical plots of covid data -- adding color

fig = px.scatter_geo(d1, locations="iso_code",
                    size="total_cases", # size of markers, "total_cases" is one of the columns of covid data
                    color="iso_code", # which column to use to set the color of markers
                    hover_name="iso_code", # column added to hover information
                     )
fig.update_layout(
   plot_bgcolor=colors['background'],
   paper_bgcolor=colors['background'],
   font_color=colors['text']
)
 
colors = {
   'background': '#4FE377',
   'text': '#111111'
}
 
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

 
app.layout = html.Div(children=[
   html.H1(children='Hello ! Welcome to Covid Dashbord',
           style={
           'textAlign': 'center',
           'color': colors['text']
       }),
 
   html.Div(children='''
       You can view the total number of cases for a desired country by just moving the pointer at particular country.
   ''',
   style={
           'textAlign': 'center',
           'color': colors['text']
       }),
 
   dcc.Graph(
       id='example-graph',
       figure=fig
   )
])
  app.run_server(mode="external")
 
if __name__ == '__main__':
    app.run_server(debug=True)
