import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

'''url = 'http://cwprod/CATSWebNET/main.aspx?WCI=Main&WCE=SubmitQry&WCU=s%3DTHL6LUP42EW96GZA7WNNXYIC675ZRXFQ%7C%2A%7Er%3DMonth%20Count%7C%2A%7Eq%3DCAQuery%7C%2A%7Ef%3D%252D1%7C%2A%7Eo%3D2'

df = pd.read_html(url)

data = [
				#{'x':[1,2,3,4,5], 'y':[5,6,7,2,1], 'type':'line', 'name':'boats'},
				{'x':[1,2,3,4,5], 'y':[8,9,6,2,7], 'type':'bar', 'name':'cars'}
]
'''

url = open('metrics.html')
#url = 'http://cwprod/CATSWebNET/main.aspx?WCI=Main&WCE=SubmitQry&WCU=%7c*%7eq%3d8%7c*%7er%3df4400a224e2e4ba2a5c17d3d4f9ee205%7c*%7ef%3d-1%7c*%7eo%3d3%7c*%7ep%3dComplaint%20Folder%7c*%7es%3dTHL6LUP42EW96GZA7WNNXYIC675ZRXFQ'
df_html = pd.read_html(url)
data_table = df_html[1]

col_names = list()

for index, row in data_table.iloc[[0]].iterrows():
	for i in range(len(data_table.columns)):
		col_names.append(row[i])


data_table.columns = col_names
data_table = data_table.drop(data_table.index[0])
data_table.index = range(len(data_table.index))

metric_data = list()

cf_count_table = data_table.pivot_table(index=['Primary Complaint Owner'], aggfunc='size')
for item in cf_count_table.iteritems():
	metric_data.append(item)

metric_data_df = pd.DataFrame(metric_data, columns=['Complaint owner', 'Count'])


metric_data = [go.Bar(x=metric_data_df['Complaint owner'], y=metric_data_df['Count'])]


layout = dict(title='Metrics Chart',
							showlegend=False)

fig = dict(data=metric_data, layout=layout)



app = dash.Dash(__name__)

app.layout = html.Div([
			html.Div(
				dcc.Graph(id='Metric_Chart',
									figure=fig))
			])


if __name__=="__main__":
    app.run_server(debug=True, port=5001)