import logging

LOGGER = 'my_desk'
APP_ID = 'amzn1.ask.skill.999f5e91-7264-4660-b397-5efc340a51f9'

def handle_event(event, context):
    logging.getLogger(LOGGER).warn(event)

    if event['session']['application']['applicationId'] != APP_ID:
        raise RuntimeError('Wrong applicationId')

    request = event['request']
    if 'intent' in request:
        intent = request['intent']['name']

        if intent == 'GoToPositionIntent':
            position = request['intent']['slots']['Position']['value']
            if position == 'sit':
                logging.getLogger(LOGGER).warn('sit')
            elif position == 'stand':
                logging.getLogger(LOGGER).warn('stand')
        elif intent == 'GoToHeightIntent':
            height = request['intent']['slots']['Height']['value']
            logging.getLogger(LOGGER).warn(height)
        elif intent == 'GoUpIntent':
            logging.getLogger(LOGGER).warn('up')
        elif intent == 'GoDownIntent':
            logging.getLogger(LOGGER).warn('down')
        elif intent == 'AMAZON.StopIntent':
            logging.getLogger(LOGGER).warn('stop')

    response = {
        "version": 1.0,
        "response": {
        }
    }

    logging.getLogger(LOGGER).warn(response)
    return response
