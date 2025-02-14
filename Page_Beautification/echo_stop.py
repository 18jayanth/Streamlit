import streamlit as st
import time
st.write('This is statements under write ')
#to write st.write as it is
st.code("st.write('This is statements under write ')")

def get_username():
    return 'Jayanth'
with st.echo():
    def get_punc():
        return '!!!'
    greeting='hi '
    name=get_username()
    punc=get_punc()
    st.write(greeting,name,punc)

first_name = st.text_input('First Name : ')
if not first_name:
    #it stop is used ,if u enter something u enter then it proceed to next
    st.warning('Please enter your first name.')
    st.stop()

last_name = st.text_input('Last Name : ')
if not last_name:
    st.warning('Please enter your last name.')
    #it stop is used ,if u enter something u enter then it proceed to next
    #statement 'thanks for writing your name'
    st.stop()

st.success('Thank you for writing your name')
