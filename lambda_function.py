from ask import alexa
from random import randint

def lambda_handler(request_obj, context={}):
    ''' All requests start here '''
    return alexa.route_request(request_obj)

@alexa.default
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return alexa.create_response(message="Just say Alexa compliment me!")

@alexa.request("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to Compliment Me! On your way out to conquer the day "
                                 "or just need a pick me up? Boost yourself with a compliment!",
                                 reprompt_message='Would you like a compliment?'
                                 'Say, Alexa Compliment Me.')

@alexa.request(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Bye!")

@alexa.intent('GetComplimentIntent')
def get_compliments(request):
    linesOfCompliments = [line.rstrip('\n') for line in open('compliments.txt')]

    randCompliment = (randint(0,len(linesOfCompliments)-1))
    compliment = linesOfCompliments[randCompliment]

    return alexa.create_response(message=compliment, end_session=True)

@alexa.intent('AMAZON.HelpIntent')
def help_intent_handler(request):
    return alexa.create_response(message="You can ask for a compliment by saying alexa compliment me!")

@alexa.intent('AMAZON.StopIntent')
def stop_intent_handler(request):
    return alexa.create_response(message="Bye!")
