import flask,os
import json
from flask import request, jsonify
from flask import Flask, render_template, send_from_directory
from twilio.rest import Client
from twilio.rest import TwilioRestClient
from twilio.twiml.voice_response import VoiceResponse, Say



app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome ,Go to the below link...</h1><p>/api/v1/contact/<int:contact_no></p>'''
    #message = "Hello, World"
    #return render_template('voice.xml')

PATH = os.path.dirname(os.path.abspath(__file__))
app=Flask("Locals",template_folder=os.path.join(PATH, 
'templates'),static_folder='.')

@app.route('/voice1.xml', methods=['GET'])
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


account_sid = 'AC85b5779859d9ab875'
auth_token = '43ee46ac40f418dc8028'
client = Client(account_sid, auth_token)

@app.route('/api/v1/contact/', methods=['GET'])
def get_caller():
    data = {}
    call = client.calls.create(
                        
                        url='http://593479bb.ngrok.io/voice1.xml',
                        to='+917911',
                        from_='+193607',
                        status_callback='http://593479bb.ngrok.io/events',
                        status_callback_event=['initiated', 'answered', 'completed'],
                        status_callback_method='POST',
                        method='GET'
                        )

                
        
    # response = VoiceResponse()
    # response.gather()

    # print(response)
    #data['date_created'] = call.date_created
    #data['date_updated'] = call.date_updated
    data['duration'] = call.duration
    data['end_time'] = call.end_time
    data['sid'] = call.sid
    data['start_time'] = call.start_time
    data['status'] = call.status
   
    
    json_data = json.dumps(data)
   
    return json_data

@app.route('/api/v1/contact/', methods=['POST'])
def gether_data():
    #print(request.json)
    print
    print(request.values)
    choice = request.values['Digits']
    print("you have entered "+choice+"=========")

    #resp = VoiceResponse()resp.redirect('/api/v1/contact/') return  #str(resp)
    response = "<Response><!-- hi --></Response>"
    return response
   

@app.route('/events', methods=['GET', 'POST'])
def event_data():
    
    called = request.values.get("Called")
    callStatus = request.values.get("CallStatus")

    print("==============================")
    print(callStatus)
    print("==============================")

    response = "<Response><!-- hi --></Response>"
    return response



host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 5000))
app.run(host=host, port=port)
