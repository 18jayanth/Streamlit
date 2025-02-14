import streamlit as st
#Radio Button
st.subheader("1.Radio Button")
gender=st.radio('Select Your Gender:',options=('Male','Female','Other'),
                help="Choose One",horizontal=True)
st.write("Your Gender:",gender)

#Select Box
st.subheader("2.Select Box")
option=st.selectbox('Select Your Subject:',options=('Physics','Chemistry','Biology'),
                help="Choose One")
st.write("Your Choosen Subject:",option)

#Multi Select Box
st.subheader("3.Multi Select Box")
options=st.multiselect('Select Your Subject:',options=('Physics','Chemistry','Biology'),
                help="Choose One",default='Physics')

#Button
st.subheader("4.Button")
if st.button("Hello"):
    st.write("HI")
else:
    st.write("Hello")

if st.checkbox('I Agree to terms and condtions',help='You Must agree to proceed'):
    st.write("Thank You!!")

#Color Picker
st.subheader("6.Color Picker:")
st.color_picker("Select Your Favourite Color:",'#1111DC')

st.button("Submit Your Response!!")
               