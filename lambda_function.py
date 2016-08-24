import logging
import requests

LOGGER = 'my_desk'
APP_ID = 'amzn1.ask.skill.999f5e91-7264-4660-b397-5efc340a51f9'

def handle_event(event, context):
    logging.getLogger(LOGGER).warn(event)

    if event['session']['application']['applicationId'] != APP_ID:
        raise RuntimeError('Wrong applicationId')

    request = event['request']
    command_endpoint = None
    if 'intent' in request:
        intent = request['intent']['name']

        if intent == 'GoToPositionIntent':
            position = request['intent']['slots']['Position']['value']
            if position == 'sit' or position == 'sitting':
                logging.getLogger(LOGGER).warn('sit')
                command_endpoint = 'position/sit'
            elif position == 'stand' or position == 'standing':
                logging.getLogger(LOGGER).warn('stand')
                command_endpoint = 'position/stand'
        elif intent == 'GoToHeightIntent':
            height = request['intent']['slots']['Height']['value']
            logging.getLogger(LOGGER).warn(height)
            command_endpoint = 'height/' + height
        elif intent == 'GoUpIntent':
            logging.getLogger(LOGGER).warn('up')
            command_endpoint = 'up'
        elif intent == 'GoDownIntent':
            logging.getLogger(LOGGER).warn('down')
            command_endpoint = 'down'
        elif intent == 'AMAZON.StopIntent':
            logging.getLogger(LOGGER).warn('stop')
            command_endpoint = 'stop'

    if command_endpoint and requests.get('http://66.189.43.74:3776/' + command_endpoint).ok:
        response = { "version": 1.0, "response": { } }
    else:
        response = {
            "version": 1.0,
            "response": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "I'm sorry dave, I'm afraid I can't do that."
                }
            }
        }

    logging.getLogger(LOGGER).warn(response)
    return response
