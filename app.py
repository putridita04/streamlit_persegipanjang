import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('hitung luas bidang',
    ['hitung luas persegi panjang',
     'hitung luas segitiga'],
    default_index=0)

if (selected == 'hitung luas persegi panjang') :
    st.title('luas persegi panjang')

    panjang = st.number_input ("masukkan nilai panjang", 0)
    lebar = st.number_input ("masukkan nilai lebar", 0)
    hitung = st.button ('HITUNG')

    if hitung :
        luas = panjang * lebar
        st.write ("hasil luas persegi panjang adalah = ", luas)

if (selected == 'hitung luas segitiga') :
    st.title('hitung luas segitiga')

    alas = st.number_input ("masukkan nilai alas", 0)
    tinggi = st.number_input ("masukkan nilai tinggi", 0)
    hitung = st.button ('HITUNG')

    if hitung :
        luas = 0.5 * alas * tinggi
        st.write ("hasil luas segitiga adalah = ", luas)