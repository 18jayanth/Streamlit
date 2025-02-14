import streamlit as st
from PIL import Image
#images two ways
st.title('1.Image From path')
#direct from adress
img=Image.open('assets/9.jpg')
st.image(img,width=300,caption='Simple Image')
#2)from link on internet
st.title('2.Image From Link')
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Mahesh_Babu_in_Spyder.jpg/1200px-Mahesh_Babu_in_Spyder.jpg",width=300,caption='Mahesh Babu')
# 3)From Video
st.title('3.Video From Path')
videofile=open('assets/video1.mp4','rb',)
st.video(videofile,start_time=20)

# 3)From Audio
st.title('4.AudioFrom Path')
audiofile=open('assests/videoplayback.mp3','rb',)
st.audio(audiofile,start_time=20)