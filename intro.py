import streamlit as st
import reveal_slides as rs

# ページ設定で"wide"を指定する
_page_title = "Streamlitの紹介"
st.set_page_config(page_title=_page_title, layout="wide")

# Markdownを読み込んでReveal.jsに流し込む
with open('slides.md', 'r', encoding='utf-8') as f:
    content_markdown = f.read()
    config = {
        "width": 1280,
        "height": 768,
        "center": True,
        "margin": 0.05
    }
    rs.slides(content_markdown,
              theme="white",
              css="b { font-weight:bold; color:#FF0000; }",
              config=config,
              markdown_props={ "data-separator-vertical":"^--$" })

# # 画面切り替え
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("1"):
#         st.switch_page("pages/page1.py")
# with col2:
#     if st.button("2"):
#         st.switch_page("pages/page2.py")
