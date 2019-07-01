import pandas as pd

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
print(metric_data_df)




