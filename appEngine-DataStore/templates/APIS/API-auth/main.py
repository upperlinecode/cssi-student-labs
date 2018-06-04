#main.py
import webapp2
import os
from random import randint 
from google.appengine.api import urlfetch 
import json 
import twilio


class MainPage(webapp2.RequestHandler):
    def get(self):

        
        # Your Account Sid and Auth Token from twilio.com/user/account
        account_sid = os.environ['TWILIO_SID']
        auth_token = os.environ['TWILIO_TOKEN']
        client = twilio.rest.Client(account_sid, auth_token)
        
        send_to_phone_num = "+2243921935" 
        # Get a trial Twilio number at 
        # https://www.twilio.com/console/sms/getting-started/build
        message = client.messages.create(
            send_to_phone_num,
            body="Hello from Chicago",
            from_=os.environ['TWILIO_PHONE'], 
            media_url="https://www.publicdomainpictures.net/pictures/170000/velka/chicago-skyline-dusk-view.jpg"
        )

        self.response.write("Your message has been sent to " + send_to_phone_num + " with an id of " +  message.sid)



app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)