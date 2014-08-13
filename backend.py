import cherrypy
import os
import random
import ttt


class index(object):
	@cherrypy.expose
	def index(self):
	    return open("index.html").read()

class computerBidder(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def GET(self):
		return ""

	def POST(self, **args):
		p1 = int(args['p1'])
		p2 = int(args['p2'])
		pos = list(args['pos'])
		if ttt.evenGameQ(pos):
			if p1 > p2:
				response = p1
			else:
				response = random.randint(0, int(p1/2))
		elif ttt.tieGameQ(pos):
			response = random.randint(0, p1)
		else:
			response = random.randint(0, p1)
		return str(response)

class computerMover(object):
	exposed = True
	
	@cherrypy.tools.accept(media='text/plain')
	def POST(self, **args):
		p1 = int(args['p1'])
		p2 = int(args['p2'])
		pos = list(args['pos'])
		if ttt.winningSquareQ(pos) >= 0:
			response = ttt.winningSquareQ(pos)
		else:
			response = random.randint(0, 8)
			while pos[response] != 'n':
				response = random.randint(0,8)
		return str(response)

if __name__ == '__main__':
	conf = {
         '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
         },
         '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'css'
         },
         '/computeBid':{
         	'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
         },
         '/computeMove':{
         	'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
         }
    }
	webapp = index()
	webapp.computeBid = computerBidder()
	webapp.computeMove = computerMover()
	cherrypy.quickstart(webapp,'/',conf)