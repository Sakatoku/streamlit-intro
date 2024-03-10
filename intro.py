import streamlit as st
import reveal_slides as rs

# ページ設定で"wide"を指定する
_page_title = "Streamlitの紹介"
st.set_page_config(page_title=_page_title, layout="wide")

# スライド番号をセッションに保存
if "slide_number" not in st.session_state:
    st.session_state.slide_number = 0

# Markdownファイルを読み込む
def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Reveal.jsでスライドを表示する
content_markdown = read_markdown_file("slides.md")
config = {
    "width": 1280,
    "height": 768,
    "center": True,
    "margin": 0.05
}
initial_state={
    "indexh": st.session_state.slide_number
}
state = rs.slides(content_markdown,
            theme="white",
            css="b { font-weight:bold; color:#FF0000; }",
            config=config,
            initial_state=initial_state,
            markdown_props={ "data-separator-vertical":"^--$" })

# スライド番号で挙動を変える
slide_number = state["indexh"]
if slide_number == 3:
    if st.button("Demo"):
        # スライド番号をセッションに保存してページ遷移
        st.session_state.slide_number = slide_number
        st.switch_page("pages/demo1.py")
elif slide_number == 5:
    if st.button("Demo"):
        # スライド番号をセッションに保存してページ遷移
        st.session_state.slide_number = slide_number
        st.switch_page("pages/demo2.py")
elif slide_number == 6:
    if st.button("Demo"):
        # スライド番号をセッションに保存してページ遷移
        st.session_state.slide_number = slide_number
        st.switch_page("pages/demo3.py")
elif slide_number == 7:
    if st.button("Demo"):
        # スライド番号をセッションに保存してページ遷移
        st.session_state.slide_number = slide_number
        st.switch_page("pages/demo4.py")
