import streamlit as from django.conf import settings

st.tittle("Ini Halaman Dashboard!")
st.session_state['Nabung']

jumlah = 0
for session in st.session_state['Nabung']:
    jumlah += session['Nominal']

st.write("Total nominal menabung sebesar", jumlah)    