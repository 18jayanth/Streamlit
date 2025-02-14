import streamlit as st
import numpy as np
import pandas as pd
import time
import random
print(np.__name__)  # Should output 'numpy'


'''
a=0
for i in range(36):
    random.randint(1,7)
    
    cases.append(a)

np.random.seed(int(time.time()))
cases = [np.random.randint(0, 7) for _ in range(36)]
'''
if 'cases' not in st.session_state:
    np.random.seed(int(time.time()))  # Dynamic seed for randomness
    st.session_state.cases = [np.random.randint(0, 7) for _ in range(36)]



st.write(st.session_state.cases)