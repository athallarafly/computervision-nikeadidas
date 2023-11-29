import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Exploratory Data Analysis (EDA)')

# Open the images
    image1 = Image.open('img-eda/Adidas (21).JPG')
    image2 = Image.open('img-eda/image_258.jpg')

    # Create two columns
    col1, col2 = st.columns(2)

    # Display images in separate columns
    col1.image(image1, caption='Adidas', use_column_width=True)
    col2.image(image2, caption='Nike', use_column_width=True)


    st.title('Data Visualization')
# start
    with st.expander('Random Shoes'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;"></div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img-eda/output.png')
        st.image(image)

        st.caption(
        f"""
        <div style="font-size: 21.5px;"></div>
        """,
        unsafe_allow_html=True)

# end 

# start
    with st.expander('Image Dimensions'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Image Dimensions</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img-eda/1.png')
        st.image(image)

        st.caption(
        f"""
        <div style="font-size: 21.5px;">Width dan Height paling banyak ada di angka 250 pada sepatu adidas dan width, height tertinggi ada di angka > 2000</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Height Distribution'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Height Distribution</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img-eda/output1.png')
        st.image(image)

        st.caption(
        f"""
        <div style="font-size: 21.5px;">Dari distribusi tersebut dapat dilihat bahwa distribusi paling banyak ada di angka > 200, dapat disimpulkan bahwa rata - rata Tinggi gambar ada di angka 200</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Width Distribution'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Width Distribution</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img-eda/output2.png')
        st.image(image)

        st.caption(
        f"""
        <div style="font-size: 21.5px;">Dari distribusi tersebut dapat dilihat bahwa distribusi Width gambar ada di angka > 200 yang berarti rata - rata Width gambar ada di angka 200</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Channel Distribution'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Channel Distribution</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img-eda/output3.png')
        st.image(image)

        st.caption(
        f"""
        <div style="font-size: 21.5px;">Dari visualisasi tersebut dapat dilihat bahwa rata - rata gambar menggunakan RGB dibanding RGBA karena distribusi A (Alpha) lebih sedikit jika dibanding dengan RGB</div>
        """,
        unsafe_allow_html=True)

# end