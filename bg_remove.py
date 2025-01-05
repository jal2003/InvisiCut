import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import time

# Set page configuration
st.set_page_config(layout="wide", page_title="InvisiCut - Background Remover")

# Title with emojis
st.title(":blue[InvisiCut] :scissors: :sparkles:")

st.write("## :sparkling_heart: Remove background from your image with style!")

st.sidebar.write("## :gear: Upload and Download")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB


# Function to convert image to downloadable format
def convert_img(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


# Function to process and display the image
def fix_img(upload):
    with st.spinner("Processing your image... :hourglass_flowing_sand:"):
        time.sleep(1.5)  # Simulate loading time for better animation
        image = Image.open(upload)
        
        # Display original image in the first column
        col1.write("### :camera: Original Image")
        col1.image(image, use_container_width=True)

        # Remove background and display fixed image in the second column
        fixed = remove(image)
        col2.write("### :sparkles: Fixed Image")
        col2.image(fixed, use_container_width=True)

        # Add download button with custom icon
        st.sidebar.markdown("\n")
        st.sidebar.download_button(
            "Download Fixed Image :arrow_down:",
            convert_img(fixed),
            "fixed.png",
            "image/png"
        )


# Layout with two columns for original and fixed images
col1, col2 = st.columns(2)

# Sidebar file uploader
my_upload = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.sidebar.error("File size exceeded 5MB! Please upload a smaller image.")
    else:
        fix_img(upload=my_upload)
else:
    # Display placeholder image when no image is uploaded
    placeholder_img = "lion.jpg"  # Replace with a real path to your placeholder image
    st.info("No image uploaded yet. Showing a sample image...")
    fix_img(upload=placeholder_img)

# Footer section
st.write("---")
st.write("### :heart: :rocket:  | Made by Jal Desai")
