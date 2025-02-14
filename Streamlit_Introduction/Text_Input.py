import streamlit as st
from  datetime import datetime
#for name
st.subheader('1.Text Input:')
name=st.text_input('Enter Your Name:',value='Jayanth')
st.write('Hello',name)

#for password
st.subheader('2.Password Input:')
password=st.text_input('Enter Your Name:',type='password',help='atleast 8 characters including special characters')

#for text area
st.subheader('3.Text Area')
st.text_area("Enter Your Text in 500 characters",height=200,max_chars=500,help='Max 500 characters allowed')

#for numbers
st.subheader('4.Number Input')
st.number_input("Enter Your age:",min_value=1,max_value=110,value=23,step=1)

#for date
st.subheader('5.Date Input')
today=datetime.now().date()
date=st.date_input("Enter The Date:",value=today,min_value=today,max_value=today.replace(year=today.year+1))
st.write("You have selected:",datetime.strftime(date,'%m/%d/%y'))