import sys, os, socket
from termcolor import colored
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer


##
## @brief      Class for threading simple server.
##
class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
	allow_reuse_address = True
	prg_lbl = colored('mini-mead','green', attrs=['bold'])

	def greetings(self):
		host = str(self.server_address[0]) if str(self.server_address[0]) != '0.0.0.0' else '127.0.0.1'
		port = self.server_address[1]
		print("\n[{}] .:. now serving your content @ {}".format( self.prg_lbl, colored( "http://{}:{}".format( host, port ),'yellow', attrs=['bold'] )))

	def goodbye(self):
		print("\n[{}] .:. shut'n her down captian ..hic..".format( self.prg_lbl ))


	def server_close(self):
		super().server_close()
		self.goodbye()
	
	def server_activate(self):
		super().server_activate()
		self.greetings()
		

class ThreadedServer:
	@staticmethod
	def create( config ):
		return ThreadingSimpleServer(('0.0.0.0', config.port), SimpleHTTPRequestHandler)
