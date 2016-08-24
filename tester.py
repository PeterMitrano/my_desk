import logging
logging.basicConfig()

request = {
    "session": {
        "sessionId": "SessionId.36e5f071-3a93-4c00-bfbd-b8e9f2a3480b",
        "application": {
            "applicationId": "amzn1.ask.skill.999f5e91-7264-4660-b397-5efc340a51f9"
            },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMO2SFOS6X27SVULUA6HAAIOQODD5LV7SHXWHTXQCF7E6XF4235Q3YVQSZRWO3HJ2G23KP6OKKNG4WLH4LHGCOWCHTE5MJCSXVMTJJ7X2V5VB4JWJ3F5SBMAQWZXEM6K32ZMD2ABLWWAPDXDPOZSEJWNKLBRMZEWFITY5NAQMP7DROL2NRT7SA"
            },
        "new": True
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.db2f82c4-400e-48f3-9f58-efb84449d0d4",
        "locale": "en-US",
        "timestamp": "2016-08-24T07:01:02Z",
        "intent": {
            "name": "GoUpIntent",
            "slots": {}
            }
        },
    "version": "1.0"
}

import lambda_function


print lambda_function.handle_event(request, {})
