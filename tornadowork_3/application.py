__author__ = 'umitunal'

import os.path
import tornado.web

#PROJECT CONSTANS
PROJECT_PATH  = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, "templates")
STATIC_PATH   = os.path.join(PROJECT_PATH, "static")

from handler import home

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home.IndexHandler),
            (r"/json", home.JsonOutputHandler),
            (r"/async", home.TestAsyncHandler),
            (r"/basicAsync", home.BasicAsyncHandler),
            (r"/ajax", home.AjaxJsonOutputHandler)
        ]

        settings = dict(
            template_path  = TEMPLATE_PATH,
            static_path    = STATIC_PATH,
            debug          = True
        )

        tornado.web.Application.__init__(self, handlers, **settings)
