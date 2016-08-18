from ask import alexa
from random import randint

def lambda_handler(request_obj, context={}):
    return alexa.route_request(request_obj)

@alexa.default_handler()
def default_handler(request):
    return alexa.create_response(message="Just say Alexa compliment me!")

@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to Compliment Me! On your way out to conquer the day "
                                 "or just need a pick me up? Boost yourself with a compliment!",
                                 reprompt_message='Would you like a compliment? '
                                 'Say, Alexa Compliment Me.')

@alexa.request_handler(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Bye!")

@alexa.intent_handler("GetComplimentIntent")
def get_compliment_intent_handler(request):
    linesOfCompliments = [line.rstrip('\n') for line in open('compliments.txt')]

    randCompliment = (randint(0,len(linesOfCompliments)-1))
    compliment = linesOfCompliments[randCompliment]

    return alexa.create_response(message=compliment, end_session=False)

@alexa.intent_handler("AMAZON.HelpIntent")
def help_intent_handler(request):
    return alexa.create_response(message="This skill compliments you when you say alexa compliment me!")

@alexa.intent_handler("AMAZON.StopIntent")
def stop_intent_handler(request):
    return alexa.create_response(message="Bye!")
