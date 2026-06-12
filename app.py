import streamlit as st
from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6LYPHzB7KvkTQ47-Ijqvgch25xwolu_s0GdryPrvK0eng"
)

st.set_page_config(
    page_title="Mukesh AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Mukesh AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

for role, message in st.session_state.history:
    with st.chat_message(role):
        st.write(message)

user_input = st.chat_input("Ask me anything...")

if user_input:

    st.session_state.history.append(("user", user_input))

    with st.chat_message("user"):
        st.write(user_input)

    conversation = ""

    for role, msg in st.session_state.history:
        if role == "user":
            conversation += f"User: {msg}\n"
        else:
            conversation += f"Assistant: {msg}\n"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        bot_reply = response.text

    except Exception as e:
        bot_reply = f"Error: {e}"

    st.session_state.history.append(("assistant", bot_reply))

    with st.chat_message("assistant"):
        st.write(bot_reply)

    with open("chat_history.txt", "w", encoding="utf-8") as file:
        for role, msg in st.session_state.history:
            file.write(f"{role}: {msg}\n")
