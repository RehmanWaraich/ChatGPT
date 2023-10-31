import streamlit as st
from st_paywall import add_auth

st.set_page_config(layout="wide")
st.title("ChatGPT-3")

add_auth(required=True)

# only the user can see use the chagpt after the subscription 

st.write(f"Subscription Status: {st.session_state.user_subscribed}")
st.write("You all set the subscription!")
st.write(f"But the way, your email is: {st.session_state.email}")
