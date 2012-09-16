import tornado.web

__author__ = 'umitunal'


todoList = []

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', list=todoList)


class AddHandler(tornado.web.RequestHandler):
    def post(self):
        listitem = self.get_argument('listitem')
        todoList.append(listitem)
        self.write(str(todoList))