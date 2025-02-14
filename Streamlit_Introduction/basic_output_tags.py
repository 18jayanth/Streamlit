import streamlit as st
#title
st.title("This is the Title")
#heading
st.header("This is the Heading")
#subheading
st.subheader("This is sub heading")
#text
st.text("This is the text")
#markdown
st.markdown("This is the HTML tags using markdown") #p tag
st.markdown('# GFG')#h1
st.markdown('## GFG')#h2
st.markdown('### GFG')#h3
st.markdown('#### GFG') #h4
st.markdown('##### GFG') #h5
st.markdown('###### GFG') #h6
st.markdown('**GFG** is a company') #bold
st.markdown('__GFG__ is a company')#bold

st.markdown('*GFG* is a company')#italic
st.markdown('_GFG_ is a company')#italic

st.markdown('***GFG*** is a company')#bold and italic
st.markdown('___GFG___ is a company')#bold and italic

st.markdown('- First Point') #. First Point
st.markdown('- second point')#. SEcond Point

st.write(range(1,10))
st.write('range(1,10)')