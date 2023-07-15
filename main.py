import streamlit as st
from dotenv import load_dotenv
from utils import *
from api_dialogflow import detect_intent_text
from streamlit_chat import message

load_dotenv()

st.header("BERTALANFFY.AI")

if 'responses' not in st.session_state:
    st.session_state['responses'] = ["Hola bienvenido soy BERTALANFFY.AI, en que puedo ayudarte?"]

if 'requests' not in st.session_state:
    st.session_state['requests'] = []

# container for chat history
response_container = st.container()
# container for text box
textcontainer = st.container()

with textcontainer:
    query = st.text_input("Query: ", key="input")
    if query:
        with st.spinner("typing..."):
            conversation_string = get_conversation_string()
            # st.code(conversation_string)
            refined_query = query_refiner(conversation_string, query)
            st.subheader("Refined Query:")
            st.write(refined_query)
            response = detect_intent_text(refined_query)

        st.session_state.requests.append(query)
        st.session_state.responses.append(response)

with response_container:
    if st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i], key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')
