# this module is used to house any code that deals with the oobabooga backend
# this includes the code to contact the model, and the code to parse the results
# it also includes the code to format the database specifically for the model
# oobabooga has multiple models, so this module is used to connect to oobabooga so that it can handle the different models
# this is literally a copy paste of the kobold module. they appear to be the same thing. but just in case they arent, i will keep separate modules for them



import datetime
from datetime import datetime
import json
import importlib
import ai_database
import requests




def load_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

config = load_config()


def construct_chat_memory(self, input_text, combined_messages):
        # this function is used to construct the chat memory for the model
        return input_text


def get_response(self, chat_memory):
        # this function is used to get the response from the model
        # use the oobabooga api to get the response
        # sent a post request to the oobabooga api at the generate 
        # the address is http://127.0.0.1:5000/api/v1/generate
        # the data is {"prompt": chat_memory}
        # it should be in json format
        # the response is the response from the model
        # return the response

        # send the post request to the oobabooga api using the requests library and wait for the response
        response = requests.post("http://127.0.0.1:5000/api/v1/generate", json={"prompt": chat_memory}).json()
        # the response is a json object, so we need to parse it
        response = response["results"]
        # we need to clean it up so that it is in the correct format
        # its in the form of [{'text': ", TEXT HERE"}] we just want the part labeled TEXT HERE
        response = response[0]["text"]
        # remove the ", " from the beginning of the response
        response = response[2:]
        


        
        # return the response
        print(response)

        
        
        
    

        
        return response 

def get_summary(prompt_messages):
        # this function is used to get the summary from the model

        return ""



def _get_history(full_history):
    return []


def prepare_user_message(self, input_text):
        user_message = {
            "sender": "user",
            "text": input_text,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        return user_message


def prepare_model_message(self, response):
    # use a dummy response for now
    model_message = {
        "sender": "assistant",
        "text": response,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    return model_message


