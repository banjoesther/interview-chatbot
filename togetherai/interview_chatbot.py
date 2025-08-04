import streamlit as st
from together import Together

# Set up the API client
client = Together(api_key="664d308305210af2183d1065be50756fb64122d403c0e05db360e1e1fffdedcd")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """Act as an experienced hiring manager. Ask me five interview questions
                          one by one. After I respond, provide constructive feedback on my answer,
                          including strengths and areas for improvement. If my response is incomplete,
                          guide me toward a better answer."""
        },
        {
            "role": "user",
            "content": "I am preparing for a Data Scientist interview. Can you ask me five basic questions and evaluate my response?"
        }
    ]
    # Get the first question from the assistant
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=st.session_state.messages
    )
    first_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": first_reply})

# Display chat history
st.title("🤖 Data Scientist Interview Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user reply
user_input = st.chat_input("Your answer...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call model with updated messages
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=st.session_state.messages
    )
    assistant_reply = response.choices[0].message.content

    # Show assistant message
    st.chat_message("assistant").markdown(assistant_reply)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
