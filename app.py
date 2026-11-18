from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ChitJar — The Lucky Draw Experience", page_icon="🫙", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"] {visibility:hidden;}
.block-container {padding:0 !important; max-width:100% !important;}
.stApp {background:#f7f4ee;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "chitjar.html"
html = html_path.read_text(encoding="utf-8")
components.html(html, height=1500, scrolling=True)
