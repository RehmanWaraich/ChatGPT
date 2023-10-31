import streamlit as st
from st_paywall import add_auth
import openai
import pandas as pd
import numpy as np
import math
import random

st.set_page_config(layout="wide")
st.title("ChatGPT-3")

add_auth(required=True)

# only the user can see use the chagpt after the subscription 
st.set_page_config(
    page_title="ChatGPT",
    page_icon="icon/favicon.png",
)

st.markdown("<h1 style='text-align: center;'>ChatGPT</h1>", unsafe_allow_html=True)

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})