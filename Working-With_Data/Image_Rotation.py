import streamlit as st
from PIL import Image
import cv2 as cv
import numpy as np

def rotated_image(image,degrees):
    img=np.array(image)
    height,width=img.shape[:2]
    M=cv.getRotationMatrix2D((width/2,height/2),degrees,1)
    rotated_image=cv.warpAffine(img,M,(width,height))
    return rotated_image


st.title('Image Rotation')
st.subheader('Please Upload Image')
img_file=st.file_uploader('Upload Image',type=['jpg','png','jpeg'])
st.subheader('Please Select the degrees to rotate')
degrees=st.slider('Select the degrees to rotate',-180,180,0,1)
if img_file is not None:
    img=Image.open(img_file)
    rotated_img=rotated_image(img,degrees)
    st.image(rotated_img)
    st.button('Download',cv.imwrite('assets/rotated_image.jpg',rotated_img))
else:
    st.error('Please Upload Image First')