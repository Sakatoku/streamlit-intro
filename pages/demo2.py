import streamlit as st

with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)

# デモからスライドに戻る
if st.button("スライドに戻る"):
    st.switch_page("intro.py")
