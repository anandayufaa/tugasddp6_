import streamlit as from st

#st.write('hello world!')
if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []

dashboard = st.Page("./pages/dashboard.py", tittle="Dashboard")
nabung = st.Page("./pages/nabung.py", tittle="Nabung")

pg = st.navigation({
    "Dashboard" : [dashboard],
    "Nabung" : [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung
                     ']= []

pg.run()