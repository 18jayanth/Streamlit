import streamlit as st
from PIL import Image
st.title('Image Convertor')
def convert(img_path,new_format):
    with Image.open(img_path) as img:
        new_name=img_path.name.split('.')[0]+'.'+new_format
        final_path='D:/Python Full Tutorial/streamlit-GFG/Working_With_Data/assets/'+new_name
        img = img.convert('RGB')#because original is RGB(color code) the new format should be be RGB

        st.subheader(final_path)
        img.save(final_path)
        st.success('Image Saved at ' + final_path   )

        

        
    
img_path=st.file_uploader('Upload Image',type=['jpg','png','jpeg'])
st.write(img_path)
new_format=st.selectbox('Select the format',['jpg','png','jpeg'])
if st.button('Convert'):
    if img_path is not None:
        convert(img_path,new_format)
        
    else:
        st.error('Please Upload Image First')