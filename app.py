import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server

app.layout = html.Div([
   html.Button("Download Text", id="btn-download"),
   dcc.Download(id="download-text")
])
 
@app.callback(
   Output("download-text", "data"),
   Input("btn-download", "n_clicks"),
   prevent_initial_call=True,
)
def func(n_clicks):
   return dict(content="Hello world!", filename="hello.txt")
 
 
if __name__ == "__main__":
   app.run_server(debug=True)
