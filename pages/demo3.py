import streamlit as st

st.page_link("intro.py", label="Home", icon="🏠")
st.page_link("pages/demo1.py", label="Other demo (1)", icon="1️⃣")
st.page_link("pages/demo2.py", label="Other demo (2)", icon="2️⃣")

# デモからスライドに戻る
if st.button("スライドに戻る"):
    st.switch_page("intro.py")
