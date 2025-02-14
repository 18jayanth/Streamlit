import streamlit as st
import pandas as pd

df=pd.read_csv('assets/restaurants1.csv')

#Displaying  Whole Data Frame
st.subheader('Displaying  Whole Data Frame')
st.dataframe(df)

#Displaying  Head Of  Data Frame
st.subheader('Displaying  Head Of  Data Frame')
st.dataframe(df.head())

#Displaying  Tail Data Frame
st.subheader('Displaying  Tail Data Frame')
st.dataframe(df.tail())

#Displaying in a Table
st.subheader('Displaying  in a Table')
st.table(df) 

#Dsiplaying in JSON
js=[{"pid":1,"name":'Mahesh',"age":25},
    {"pid":2,"name":'Ramesh',"age":26},
    {"pid":3,"name":'Suresh',"age":27},
    {"pid":4,"name":'Naresh',"age":28}]
st.subheader('Displaying  in JSON')
st.json(js)

#Description of Data Frame
st.table(df.describe())

