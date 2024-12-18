import pandas as pd
import plotly
import plotly.graph_objs as go




df = pd.read_csv('per ip filtered and excluded.csv')
ip_df = df['ip_filtered'].dropna()
ip_df = ip_df[ip_df.map(len) <= 15]

ip_df['1'] = ip_df.str.split('.', 1).str[0].dropna().astype(int)
# print(ip_df['1'])

ip_df['2'] = ip_df.str.split('.', 2).str[1].dropna()
# print(ip_df['2'])


ip_df['3'] = ip_df.str.split('.', 3).str[2].dropna()
# print(ip_df['3'])


ip_df['4'] = ip_df.str.split('.', 4).str[3].dropna()
# print(ip_df['4'])

#Make Plotly figure
fig1 = go.Scatter3d(x=ip_df['2'],
                    y=ip_df['3'],
                    z=ip_df['4'],
                    marker=dict(color=ip_df['1'],
                                opacity=1,
                                reversescale=True,
                                colorscale='greens',
                                size=5),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="2"),
                                yaxis=dict( title="3"),
                                zaxis=dict(title="4")),)

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("per_ip_4DPlot_trusted.html"))







ip_excluded_df = df['ip_excluded'].dropna()
ip_excluded_df = ip_excluded_df[ip_excluded_df.map(len) <= 15]

ip_excluded_df['1'] = ip_excluded_df.str.split('.', 1).str[0].dropna().astype(int)
# print(ip_excluded_df['1'])

ip_excluded_df['2'] = ip_excluded_df.str.split('.', 2).str[1].dropna()
# print(ip_excluded_df['2'])


ip_excluded_df['3'] = ip_excluded_df.str.split('.', 3).str[2].dropna()
# print(ip_excluded_df['3'])


ip_excluded_df['4'] = ip_excluded_df.str.split('.', 4).str[3].dropna()
# print(ip_excluded_df['4'])

#Make Plotly figure
fig2 = go.Scatter3d(x=ip_excluded_df['2'],
                    y=ip_excluded_df['3'],
                    z=ip_excluded_df['4'],
                    marker=dict(color=ip_excluded_df['1'],
                                opacity=1,
                                reversescale=True,
                                colorscale='rainbow',
                                size=5),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="2"),
                                yaxis=dict( title="3"),
                                zaxis=dict(title="4")),)

#Plot and save html
plotly.offline.plot({"data": [fig2],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("per_ip_4DPlot_excluded.html"))



fig = go.Figure(data = [fig1] + [fig2])
plotly.offline.plot({"data": fig,
                     "layout": mylayout},
                     auto_open=True,
                     filename=("per_ip_4DPlot_combined.html"))