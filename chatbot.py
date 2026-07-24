import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=st.secrets["AQ.Ab8RN6Kvzis-9JYhzBXQb6aZNM4v2IYj5Yt8bwaFbX-1hjeQdg"],  # or your API key string
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

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

st.title("Tamil Meme Chatbot")

user_prompt = st.chat_input("Type your message...")

if user_prompt:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    st.write(response.choices[0].message.content)
