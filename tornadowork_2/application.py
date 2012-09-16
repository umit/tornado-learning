
__author__ = 'umitunal'

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

todoList = []

from handler import home

PROJECT_PATH  = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH   = os.path.join(PROJECT_PATH, 'static')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home.IndexHandler),
            (r"/add", home.AddHandler)
        ]
        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH
        )
        tornado.web.Application.__init__(self, handlers, **settings)