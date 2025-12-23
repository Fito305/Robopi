#!/usr/bin/env python3

# The Tornado IOLoop is needed to run the web server.
# The RequestHandler and Application object will help us
# define the behavior of our web application.
from datetime import datetime
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


# Define the MainHandler object that will handle incoming requests.
# We define one method called get to handle incoming HTTP GET requests.
# Each time it is called it will save the current time as a string
# and then call the write method with the time stamp in a dictionary.
# In the Tornado framework, whenever you provide the write method with
# a dictionary object it will automatically convert the output to JSON
# format and set the appropriate HTTP response headers to indicate the
# content type is JSON.

class MainHandler(RequestHandler):
    def get(self):
        stamp = datetime.now().isoformat()
        self.write(dict(stamp=stamp))


# We then create a Tornado Application which will route incoming
# requests for the root path to MainHandler. After that we set the
# web server to listen on port 8888 and start the main event loop
# which will kick off the web server and handle incoming web requests.

app = Application([('/', MainHandler)])
app.listen(8888)
IOLoop.current().start()
