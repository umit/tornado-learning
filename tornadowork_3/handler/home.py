__author__ = 'umitunal'

import tornado
import tornado.httpclient
import tornado.ioloop
import tornado.web

import json
import pprint
from pprint import pformat

class IndexHandler(tornado.web.RequestHandler):
    """
    Index Page Handler
    """

    def get(self):
        """
        Index Page Handler "/"
        """
        #self.write("umitunal")
        self.render("index.html",title = "Tornado Index Page",
                                 hello = "Hello World Tornado")


class JsonOutputHandler(tornado.web.RequestHandler):

    def get(self):
        phoneNumbers  = {"phone1":"123456","phone2":"123456"}
        personalInfo  = {"name": "umit", "lastname":"unal", "phoneNumbers":phoneNumbers }
        self.write(personalInfo)


class BasicAsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write("Hello, world")
        self.finish()

class TestAsyncHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://search.twitter.com/search.json?q=istanbul&rpp=5&include_entities=true&result_type=mixed",
            callback=self.on_response)


    def on_response(self, response):
        if response.error:
            raise tornado.web.HTTPError(500)

        entries = tornado.escape.json_decode(response.body)

        self.render("twitter_result.html",entriesList = entries["results"], jsonEntries = pformat(entries["results"]))


class AjaxJsonOutputHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("ajax.html", message = None)


    def post(self):
        jsonObj = json.loads(self.request.body)

        for key, value in jsonObj.iteritems():
            print key,value

        response_to_send = {}
        response_to_send['newkey'] = jsonObj['key1']

        print 'Response to return'

        pprint.pprint(response_to_send)

        self.write(json.dumps(response_to_send))




