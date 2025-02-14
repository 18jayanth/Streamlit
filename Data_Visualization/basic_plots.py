import numpy as np
import pandas as pd
import streamlit as st
#Defining Dataset
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['L-1','L-2','L-3'])

#Line Chart
st.title('1.Line Chart')
st.line_chart(chart_data)

#Area Chart
st.title('2.Area Chart')
st.area_chart(chart_data)

#Bar Chart
st.title('3.Bar Chart')
st.bar_chart(chart_data)

#Map
st.title('4.Map')
map_data=pd.DataFrame(np.random.randn(1000,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])