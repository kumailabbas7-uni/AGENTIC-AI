import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown("# 🤖 Agentic AI")
        st.caption("YOUR INTELLIGENT AI WORKSPACE")

        st.divider()

        st.markdown("### ⚡ Select Your Agent")

        selected_agent = st.selectbox(
            "Choose an agent",
            [
                "S4 - Web Search Agent",
                "S5 - Tool Agent"
            ],
            label_visibility="collapsed"
        )

        st.divider()

        st.markdown("### 🛠️ Available Tools")

        tools = [
            ("🌐", "Web Search"),
            ("🌤️", "Weather"),
            ("🧮", "Calculator"),
            ("📚", "Wikipedia"),
            ("📄", "PDF Reader"),
            ("🐍", "Python Assistant"),
            ("🌍", "Translator"),
            ("🕒", "Date & Time")
        ]

        for emoji, name in tools:
            st.markdown(
                f"""
                <div style="
                    background:#191e30;
                    padding:10px;
                    margin:6px 0;
                    border-radius:9px;
                    border:1px solid #292f48;
                ">
                    {emoji} &nbsp; {name}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        if st.button("🗑️ Clear Current Chat", use_container_width=True):
            st.session_state.chat_histories[selected_agent] = []
            st.session_state.messages = []
            st.rerun()

        st.markdown("---")
        st.caption("Agentic AI Studio V2")
        st.caption("Powered by OpenAI Agents SDK")

    return selected_agent