import webapp2
import random
import jinja2

class MainPage(webapp2.RequestHandler):
    def get(self): 
        self.response.write('Hello, World!') #response for the MainPage handler
        
class EmotionHandler(webapp2.RequestHandler):
    def get(self): #responds to a GET request
        emotions = ["witty", "edgy", "hangry", "excited", "on-point"]
        self.response.write("I feel so " + random.choice(emotions) + "!")
    

app = webapp2.WSGIApplication([
    ('/', MainPage), 
    ('/feelings', EmotionHandler)
], debug=True)