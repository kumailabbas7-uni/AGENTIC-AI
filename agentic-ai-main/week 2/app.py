
import streamlit as st

from agents import Runner
from s4_agent import agent as s4_agent
from s5_tool import agent as s5_agent

from components.styles import apply_styles
from components.sidebar import render_sidebar


# Page configuration
st.set_page_config(
    page_title="Agentic AI Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom design
apply_styles()

# Sidebar
selected_agent = render_sidebar()

# Select agent
if selected_agent.startswith("S4"):
    current_agent = s4_agent
    agent_name = "Web Search Agent"
else:
    current_agent = s5_agent
    agent_name = "Tool Agent"


# Separate chat histories
if "chat_histories" not in st.session_state:
    st.session_state.chat_histories = {
        "S4 - Web Search Agent": [],
        "S5 - Tool Agent": []
    }

if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.messages = (
    st.session_state.chat_histories[selected_agent]
)


# Header
st.markdown(
    '<div class="main-title">🤖 Agentic AI Studio</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent AI workspace. One assistant, multiple tools.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

# Agent status
st.markdown(
    f"""
    <div style="
        background:#171d32;
        border:1px solid #343b60;
        padding:15px;
        border-radius:12px;
        margin-bottom:20px;
    ">
        🟢 <b>Agent Online</b>
        <span style="color:#a5b4fc;">
            &nbsp; | &nbsp; {agent_name}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)


# Welcome screen
if not st.session_state.messages:
    st.markdown("## 👋 Welcome to your AI workspace!")
    st.markdown(
        "Ask questions, search the web, explore information "
        "and interact with your AI agent."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("🌐 Search the internet for information")

    with col2:
        st.info("🌤️ Ask about weather in any city")


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_input = st.chat_input("Message your AI assistant...")


if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Agent is thinking..."):

            try:
                result = Runner.run_sync(
                    current_agent,
                    user_input
                )

                response = result.final_output

                if not isinstance(response, str):
                    response = str(response)

                st.markdown(response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:

                st.error("Something went wrong.")

                st.code(str(e))

    st.session_state.chat_histories[selected_agent] = (
        st.session_state.messages
    )
