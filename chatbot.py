import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(
    api_key="AQ.Ab8RN6Kvzis-9JYhzBXQb6aZNM4v2IYj5Yt8bwaFbX-1hjeQdg",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
SYSTEM_PROMPT=""" You are an ai meme chatbot. For any input i am giving you should reply with any meme sentence 
related to the input. You should be funny everytime and use tanglish language also. Use the funny diaalogues from 
the tamil movies.  

# Output Format:
# <Display only the Output from LLM with no other information >



Examples:

Input: Vanakkam
Output: Vanakkam da mapla.

Input: it's boring 
Output: Seri adhuku enna ippa.

"""
user_prompt=input

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

print(response.choices[0].message)
