import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv("https://nickharbeck.com/wp-content/uploads/2019/10/StatesHFC.csv")
for col in df.columns:
  df[col] = df[col].astype(str)
for col in df.columns[1:9]:
  df[col] = df[col].astype(str)+'<br>'
df = df.replace('nan<br>', '')
df = df.replace('nan', 'None')
df['CaliforniaSNAP'][47] = "This state has a labeling requirement in effect starting Dec. 31, 2019 <br>"
df['GeneralHFCEmissionPhasedown'][19] = "26-28% reduction vs 2005 by 2025 <br>"
df['text'] = df['state'] + '<br>' + df['ClimateAlliance']  + df['HFCCommitment']  + df['GeneralHFCEmissionPhasedown'] +  'Has regulation to adopt SNAP 20/21 been proposed?: ' + df['SNAPRule20&21'] + df['CaliforniaSNAP'] +  df['CRLimit'] + df['ACLimit'] + df['EPA608'] + 'Other Requirements: ' + df['LabelingOthers']
df['SUM'] = df['SUM'].astype(int)
Check = []
for i in df['SUM']:
  if i < 1:
      Check.append('skip')
  else: 
      Check.append('text')
       
fig = go.Figure(data=go.Choropleth(locations =df['state'], z=df['SUM'].astype(float),locationmode='USA-states',colorscale='Blues',autocolorscale=False,text=df['text'], hoverinfo = Check, showscale = False))
fig.update_layout(title_text='HFC Regulations in the U.S.', geo = dict(scope = 'usa', projection=go.layout.geo.Projection(type = 'albers usa'), showlakes = True, lakecolor = 'rgb(255,255,255)'),)
fig.show()
import plotly as py

py.offline.plot(fig, filename='myplot.html')

