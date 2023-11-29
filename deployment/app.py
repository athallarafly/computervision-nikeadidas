import streamlit as st
import eda
import predictions


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis (EDA)', 'Prediction Model'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Graded Challenge 7')
    st.write('Nama      : Athalla Noegroho')
    st.write('Batch     : HCK - 009')
    st.write('Objective : ')
    st.write(
        f"""
        <div style="text-align: justify;">
        Mampu memahami, dan mengimplementasikan konsep Computer Vision, Melakukan persiapan pada data untuk digunakan dalam pembuatan model Computer Vision dan dapat melakukan analisis dan menjelaskan performa dari model yang sudah dibuat.</div>""", unsafe_allow_html=True)
    st.write(
        f"""
        <br></br>""", unsafe_allow_html=True)
    
    st.write('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Background"):
            st.caption(
            f"""
            <div style="font-size: 21.5px; text-align: justify;">
            Nike dan Adidas berhadapan dengan tantangan signifikan dalam pasar sepatu olahraga yang sangat kompetitif. Keduanya perlu terus berinovasi, memahami tren konsumen, dan merespons perubahan budaya. Dalam fokus keberlanjutan, kenyamanan, dan gaya, mereka harus mengembangkan produk yang tidak hanya unggul dalam kinerja tetapi juga ramah lingkungan. Pertumbuhan e-commerce dan peran penting media sosial menambah kompleksitas, mendorong perluasan strategi digital untuk menjaga keterlibatan konsumen dan membangun loyalitas merek di era perubahan yang cepat.
            </div>
            """,
            unsafe_allow_html=True)

    with st.expander("Problem Statement"):
            st.caption(
            f"""
            <div style="font-size: 21.5px; text-align: justify;">
            Dalam menghadapi pasar sepatu olahraga yang kompetitif, tantangan bagi Nike dan Adidas terletak pada kemampuan mereka untuk terus berinovasi, memahami tren konsumen, dan merespons perubahan budaya, dengan prediksi kesuksesan ditentukan oleh kemampuan adaptasi terhadap aspek keberlanjutan, kenyamanan, dan gaya, serta efektivitas dalam strategi digital untuk menjaga keterlibatan konsumen dan membangun loyalitas merek di era perubahan yang cepat.
            </div>
            """,
            unsafe_allow_html=True)
    with st.expander("Conclusions"):
        st.caption(
        f"""
        <div style="font-size: 21.5px; text-align: justify;"> 
        <ul>
            <li>Dari data image nikeadidas, dibuat 3 model yang dilakukan improvement menggunakan Flatten dan Transfer Learning DenseNet201.</li>   
            <li>Dari ketiga model yang dibuat hasil yang paling maksimal adalah dengan menggunakan Transfer Learning DenseNet201 dengan accuracy 80% - 90%</li>  
            <li>Model pertama yang dibuat saat melakukan prediksi tidak selalu tepat</li>   
            <li>Model menggunakan Flatten saat melakukan prediksi masih ada salahnya tetapi tidak separah jika dibanding model sebelumnya</li>   
            <li>Model menggunakan Transfer Learning DenseNet201 sudah dapat memprediksi sepatu adidas atau nike dengan benar.</li>
            <li>Model Transfer Learning tetap perlu dilakukan improvement lagi seperti melakukan trial error pada Neuoron, Hidden Layer dan lainnya untuk menghasilkan model yang maksimal</li>
            <li>Model akan bekerja lebih maksimal jika data image memiliki latar belakang putih</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
elif page == 'Exploratory Data Analysis (EDA)':
    eda.run()
else:
     predictions.run()