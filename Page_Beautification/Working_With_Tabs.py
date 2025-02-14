import streamlit as st
import pandas as pd
import numpy as np
#static
s1,s2=st.tabs(['Cat','Owl'])
s1.image("https://plus.unsplash.com/premium_photo-1673967831980-1d377baaded2?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2F0c3xlbnwwfHwwfHx8MA%3D%3D",width=200)
s2.image("https://images.pexels.com/photos/53977/eagle-owl-raptor-falconry-owl-53977.jpeg?cs=srgb&dl=pexels-pixabay-53977.jpg&fm=jpg",width=200)
#Dynamic
imgs=pd.read_csv('imgs.csv')['img_link']
tabs=st.tabs(["ID"]*30)
#st.subheader(imgs)
for tab in tabs:
    img=imgs[np.random.randint(1,1000)]
    tab.image(img,width=400)
