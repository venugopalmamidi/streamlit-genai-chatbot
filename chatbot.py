from dotenv import load_dotenv
import streamlit as st
from langchain_openai import AzureChatOpenAI
import os


load_dotenv()  # load the env variables from .env file

# setting up the page configuration for streamlit
st.set_page_config(page_title=" v Chatbot", page_icon=":robot_face:", layout="centered")
# adding a title to the streamlit app
st.title("Gen ai chatbot")

#initilizing the chat history 
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


llm=AzureChatOpenAI(
   
azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    deployment_name="gpt-4.1",
    model="gpt-4.1"


 )

user_input=st.chat_input("Ask chatbot ...")

if user_input:

    #append user message to chat history
    st.session_state.chat_history.append({"role":"user","content":user_input})

    #get response from the model
    response=llm.invoke(
        input=[{"role":"system","content":"You are a helpful assistant."},*st.session_state.chat_history]
        ) 
    
    #append assistant message to chat history
    st.session_state.chat_history.append({"role":"assistant","content":response.content})

    #show the assistant response in the chat interface
    with st.chat_message("assistant"):
        st.markdown(response.content)





