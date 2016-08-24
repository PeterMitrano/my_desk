import logging
logging.basicConfig()

request ={
  "session": {
    "sessionId": "SessionId.20551a11-a1d7-472c-ab79-4f7fee97e278",
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
    "requestId": "EdwRequestId.4598de8a-a3cd-4e95-a19a-d882855d89dc",
    "locale": "en-US",
    "timestamp": "2016-08-24T22:43:50Z",
    "intent": {
      "name": "GoToHeightIntent",
      "slots": {
        "Height": {
          "name": "Height",
          "value": "3000"
        }
      }
    }
  },
  "version": "1.0"
}

import lambda_function


print lambda_function.handle_event(request, {})
