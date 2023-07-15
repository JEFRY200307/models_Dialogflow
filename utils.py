import openai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# Obtén la clave de API del archivo .env
api_key = os.getenv("OPENAI_API_KEY")

# Asigna la clave de API a openai.api_key
openai.api_key = api_key

def query_refiner(conversation, query):
    if "TGS" in query:
        refined_query = query.replace("TGS", "Teoría General de los Sistemas")
    else:
        refined_query = query

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Given the following user query and conversation log, generate a question that is most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {refined_query}\n\nRefined Query:",
        temperature=0.4,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    refined_question = response.choices[0].text.strip().replace("Question:", "")
    return refined_question


def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses']) - 1):
        conversation_string += "Human: " + st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + st.session_state['responses'][i + 1] + "\n"
    return conversation_string
