import streamlit as st

st.title("AI Document Q&A Chatbot")

st.write("This is a demo Streamlit app.")

question = st.text_input("Ask a question:")

if question:
    st.write("You asked:", question)
    st.write("AI answer will appear here.")
