import cherrypy
import os
import random
import ttt

class index(object):
	@cherrypy.expose
	def index(self):
		try:
			count = int(open('count','r').read()) + 1
		except:
			count = 1
		open('count', 'w').write(str(count))
	    return open("index.html").read()

	@cherrypy.expose
	def rules(self):
		return open("rules.html").read()

class computerBidder(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def GET(self):
		return ""

	def POST(self, **args):
		p1 = int(args['p1'])
		p2 = int(args['p2'])
		pos = list(args['pos'])
		if p2 == 0:
			response = 0
		elif ttt.squaresRemainingQ(pos) == 1: 	# last square = bet it all
			response = min(p1,p2)
		elif ttt.evenGameQ(pos): 				# next move wins = bet it all
			response = min(p1,p2)
		elif ttt.tieGameQ(pos): 				# game will end tie = random bids
			response = random.randint(0, p1)
		else:									# OTHER CASES = TO DO
			strat = ttt.getStrategy(pos, p1, p2)
			r = random.random()
			count = 0
			while r > 0:
				r -= strat[count]
				count += 1
			response = count-1
		return str(response)

class computerMover(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def POST(self, **args):
		p1 = int(args['p1'])
		p2 = int(args['p2'])
		pos = list(args['pos'])
		print(p1, p2, pos)
		if p2 == 0:
			response = random.randint(0,8)
			while pos[response] != 'n':
				response = random.randint(0,8)
		elif ttt.tieGameQ(pos): 
			response = random.randint(0,8)
			while pos[response] != 'n':
				response = random.randint(0,8)
		elif ttt.winningSquareQ(pos) >= 0:
			print("WINNING SQUARE FOUND!!")
			response = ttt.winningSquareQ(pos)
		else:
			response = ttt.getMove(pos,p1,p2)
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
	cherrypy.config.update({'server.socket_host': '0.0.0.0',})
	cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
	cherrypy.quickstart(webapp,'/',conf)
##