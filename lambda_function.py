import logging

LOGGER = 'my_desk'
APP_ID = 'amzn1.ask.skill.999f5e91-7264-4660-b397-5efc340a51f9'

def handle_event(event, context):
    logging.getLogger(LOGGER).warn(event)

    if event['session']['application']['applicationId'] != APP_ID:
        raise RuntimeError('Wrong applicationId')

    response = {
        "version": 1.0,
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "hello world"
            }
        }
    }

    logging.getLogger(LOGGER).warn(response)
    return response
