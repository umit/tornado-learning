__author__ = 'umitunal'

from tornado.options import parse_command_line
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from application import Application
from tornado.options import define, options

define("port", default=5000, help="port number", type=int)

def main():
    parse_command_line()
    httpServer = HTTPServer(Application())
    httpServer.listen(options.port)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()