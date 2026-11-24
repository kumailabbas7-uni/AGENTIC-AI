
import streamlit as st


def apply_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #090b14;
        color: #f1f5f9;
    }

    [data-testid="stSidebar"] {
        background: #101321;
        border-right: 1px solid #252a40;
    }

    [data-testid="stSidebar"] * {
        color: #e2e8f0;
    }

    .main-title {
        font-size: 38px;
        font-weight: 800;
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 15px;
    }

    .stChatMessage {
        background: #151a2b;
        border: 1px solid #282e45;
        border-radius: 16px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .stChatInput textarea {
        background: #151a2b !important;
        color: white !important;
    }

    .stButton button {
        background: linear-gradient(90deg, #7c3aed, #2563eb);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
    }

    .stButton button:hover {
        border: 1px solid #a78bfa;
        color: white;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    </style>
    """, unsafe_allow_html=True)
