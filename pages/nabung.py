import streamlit as from django.conf import settings

st.tittle("Ini Halaman Nabung.!")

with st.from("nabung"):
    nama = st.text_input("Masukan nama")
    nominal = st.number_input("Masukan nominal nabung")
    submitButton = st.form_submit_button("Simpan")
    
    if submitButton:
        st.write(nama)
        st.session_state['Nabung'].append({
            "Nama" : nama,
            "Nominal" :nominal,
        })
        st.success("Berhasil menabung!")