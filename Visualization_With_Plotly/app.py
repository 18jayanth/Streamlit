import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff


st.title('Visualizations with Plotly')
df = pd.read_csv('tips.csv')
st.dataframe(df.head())

st.text('1.Pie Chart ')
fig=px.pie(df,values='total_bill',names='day')
st.plotly_chart(fig)

st.text('2.Pie Chart With Hole')
fig=px.pie(df,values='total_bill',names='day',opacity=0.7,hole=0.5,color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)


st.title('Interactive Graphs With Plotly')
x1=np.random.randn(200)
y1=np.random.randn(200)
z1=np.random.randn(200)
hist_data=[x1,y1,z1]
group_lbs=['G1','G2','G3']
fig=ff.create_distplot(hist_data,group_lbs)
st.plotly_chart(fig)
'''
st.text('3. Multiple Dist_plots')
x1 = np.random.randn(200) + 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) - 2
hist_data = [x1,x2,x3]
'''

st.text('3. Multiple Dist_plots')
x1 = np.random.randn(200) + 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) - 2
hist_data = [x1,x2,x3]

group_lbls = ['G1','G2','G3']
fig = ff.create_distplot(hist_data, group_lbls, bin_size = [.1, .1,.1])
st.plotly_chart(fig, use_container_width = True)

fig = ff.create_distplot(hist_data, group_lbls, bin_size = [.2, .2,.2])
st.plotly_chart(fig, use_container_width = True)

# matplotlib<seaborn(better visuailzation)<Plotly(interaction)