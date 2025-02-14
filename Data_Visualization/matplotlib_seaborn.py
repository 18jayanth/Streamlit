import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.subheader("Data Visualization Using Matplotlib and Seaborn")

st.write("1.Displaying The Data Set")
df=pd.read_csv("iris.csv")
st.dataframe(df)

st.text("2.Bar Plot Using matplotlib")
fig=plt.figure(figsize=(15,8))
#value_counts() returns the count of unique values
#  like no of versicolor, no of setosa, no of virginica
df['variety'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.text("3.Pie Chart Using Matplotlib")
fig=plt.figure(figsize=(15,8))
df['variety'].value_counts().plot(kind='pie')
st.pyplot(fig)

st.text("4.Hist Chart using Seaborn")
fig=plt.figure(figsize=(15,8))
sns.distplot(df['sepal.length'])
st.pyplot(fig)

st.text("5.Display multiple graphs")
col1,col2=st.columns(2)
with col1:
    col1.header('KDE=False')
    col1.write('KDE=False')
    fig1=plt.figure()
    sns.distplot(df['sepal.length'],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header('KDE=Hist')
    col2.write('KDE=Hist')
    fig2=plt.figure()
    sns.distplot(df['sepal.length'],hist=False)
    st.pyplot(fig2)

st.text("6.Changing The Style Of Graph")
col1,col2=st.columns(2)
with col1:
    
    fig1=plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal.length'],hist=False)
    st.pyplot(fig1)
with col2:
    
    fig2=plt.figure()
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['sepal.length'],hist=False)
    st.pyplot(fig2)

st.text("7.Scatter Plot")
fig,ax=plt.subplots(figsize=(25,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.text("8.Count Plot")
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x = 'variety')
st.pyplot(fig)

st.text('9. Box Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'variety', y = 'petal.length')
st.pyplot(fig)


st.text('10. Violin Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'variety', y = 'petal.length')
st.pyplot(fig)


