import streamlit as st
import pandas as pd
import numpy as np

level = st.slider('Set level', 0, 50, 1)
chart_data = pd.DataFrame(np.random.randn(10, 3) + level, columns=["a", "b", "c"])

st.line_chart(chart_data)

# デモからスライドに戻る
if st.button("スライドに戻る"):
    st.switch_page("intro.py")
