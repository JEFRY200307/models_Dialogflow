import os
from google.api_core.exceptions import InvalidArgument
from google.cloud import dialogflow
from dotenv import load_dotenv

load_dotenv()

# credenciales

project_id = os.getenv("DIALOGFLOW_PROJECT_ID")
session_id = "my_session_id"
language_code = "en"
def detect_intent_text(text):

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    request_response = response.query_result.fulfillment_text
    return request_response