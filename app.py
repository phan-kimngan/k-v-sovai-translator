import streamlit as st
from gtts import gTTS
import pandas as pd
from datetime import datetime

def translate_kor_to_vie(text):
    return text
def translate_vie_to_kor(text):
    return text

# ==============================
# 1. PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="K-V SovAI Translator",
    page_icon="🇰🇷🇻🇳",
    layout="wide"
)

# ==============================
# CSS FIX — GIỮ 2 CỘT NGANG TRÊN MOBILE
# ==============================
st.markdown("""
<style>
/* Ép Streamlit giữ layout 2 cột trên mobile */
@media (max-width: 600px) {
    .stColumns {
        display: flex !important;
        flex-direction: row !important;
        gap: 8px !important;
    }
    .stColumn {
        flex: 1 !important;
        max-width: 50% !important;
        min-width: 50% !important;
        display: flex !important;
        flex-direction: column !important;
    }
    .block-container {
        padding-left: 5px !important;
        padding-right: 5px !important;
    }
}
textarea {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# 2. SESSION STATE
# ==============================
if "mode" not in st.session_state:
    st.session_state.mode = "vi_to_kr"

# ==============================
# 3. HEADER
# ==============================
st.markdown(
    """
    <h2 style='text-align:center; color:#1E3A8A;'>
        🇰🇷 K-V SovAI Translator 🇻🇳
    </h2>
    """,
    unsafe_allow_html=True
)

# ==============================
# 4. LANGUAGE MODE
# ==============================
mode = st.session_state.mode
if mode == "vi_to_kr":
    left_label = "Vietnamese"
    right_label = "Korean"
    src_tts_lang = "vi"
    tgt_tts_lang = "ko"
    translate_func = translate_vie_to_kor
else:
    left_label = "Korean"
    right_label = "Vietnamese"
    src_tts_lang = "ko"
    tgt_tts_lang = "vi"
    translate_func = translate_kor_to_vie

# ==============================
# 5. NEW UI — 2 CỘT + SWAP NẰM CHUNG
# ==============================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"<div style='font-size:22px; font-weight:600;'>{left_label}</div>", unsafe_allow_html=True)

with col2:
    st.markdown(
        f"""
        <div style='display:flex; justify-content:center; margin-bottom:5px;'>
            <button style="
                font-size:22px;
                background:#ffffff55;
                border-radius:10px;
                border:1px solid #999;
                padding:3px 10px;
            " 
            onclick="window.location.href = window.location.href">
                ↔️
            </button>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:22px; font-weight:600;'>{right_label}</div>", unsafe_allow_html=True)

# ==============================
# 6. TEXT AREA 2 BÊN
# ==============================
with col1:
    input_text = st.text_area("", key="input_text", height=200)

with col2:
    st.text_area("", st.session_state.get("translation", ""), height=200, key="output_box")

# ==============================
# 7. TRANSLATE BUTTON
# ==============================
if st.button("🌐 Translate", use_container_width=True):
    text = st.session_state.input_text.strip()
    if text:
        result = translate_func(text)
        st.session_state.translation = result
        st.experimental_rerun()

# ==============================
# 8. FOOTER
# ==============================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>© 2025 K-V SovAI Translator</p>", unsafe_allow_html=True)
