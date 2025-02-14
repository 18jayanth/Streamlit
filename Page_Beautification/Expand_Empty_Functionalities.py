import streamlit as st
import numpy as np
import pandas as pd
import time
cases=[]
for i in range(100):
    cases.append(np.random.randint(1,7))
st.write(cases)
#this will tell how many times 1 2,3 4 5 6 appears
data=[]
for i in range(1,7):
    data.append(cases.count(i))

st.bar_chart({'data':data})

with st.expander('see explanation'):
     st.write(
         '''
     The chart shows some numbers I got from rolling a dice 100 times and its
        basically about how many times each face appears
        ''')
st.image("https://static.streamlit.io/examples/dice.jpg")

with st.empty():
    st.write('You Need to write 10 seconds')
    for seconds in range(0,11):
        st.write('⏳ ' + str(seconds) + ' seconds remained')
        time.sleep(1)
    st.write('10 seconds completed')
