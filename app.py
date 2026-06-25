import streamlit as st

st.set_page_config(page_title="AI Database Agent")

st.title("🤖 AI Database Agent")

st.success("Hackathon Project is Running!")

question = st.text_input("Ask a question")

if question:
    st.write("You asked:", question)