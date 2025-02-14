import streamlit as st
import pandas as pd
from PIL import Image
st.title('File Uploading')


#1.Image
st.subheader("Image Uploading")
img_file=st.file_uploader('Upload Image',type=['jpg','png','jpeg'])
if img_file is not None:
    #st.image(img_file,width=300,caption='Uploaded Image')
    #st.write(type(img_file))
    file_details={"FileName":img_file.name,"FileType":img_file.type,"FileSize":img_file.size}
    st.write(file_details)
    #to see the image
    st.image(Image.open(img_file),width=300,caption='Uploaded Image')

#2.Audio
st.subheader("Audio Uploading")
audio_file=st.file_uploader('Upload Audio',type=['wav','mp3'])
if audio_file is not None:
    
    file_details={"FileName":audio_file.name,"FileType":audio_file.type,"FileSize":audio_file.size}
    st.write(file_details)
    #to listen to audio

    st.audio(audio_file,format='audio/wav')


#3.Video
st.subheader("Video Uploading")
Video_file=st.file_uploader('Upload Video',type=['mp4','avi'])
if Video_file is not None:
    #st.image(img_file,width=300,caption='Uploaded Image')
    #st.write(type(img_file))
    file_details={"FileName":Video_file.name,"FileType":Video_file.type,"FileSize":Video_file.size}
    st.write(file_details)
    #to see the image
    st.video(Video_file)

#4.CSV
st.subheader("CSV Uploading")
CSV_file=st.file_uploader('Upload CSV',type=['csv'])
if CSV_file is not None:
    #st.image(img_file,width=300,caption='Uploaded Image')
    #st.write(type(img_file))
    file_details={"FileName":CSV_file.name,"FileType":CSV_file.type,"FileSize":CSV_file.size}
    st.write(file_details)
    #to see the image
    st.dataframe(CSV_file)
