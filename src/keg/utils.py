import os, argparse

class Environment:

	def __init__(self):

		parser = argparse.ArgumentParser(description='Serve some files the Jekyll way')
		parser.add_argument( '-p', '--port', type=str, default=8000, help='the port you would like to serve from')
		parser.add_argument('-d','--directory', type=str, default=os.getcwd(), help='the base directory to serve from')

		args = parser.parse_args()

		self.port = args.port
		self.directory = args.directory
		self.docroot = os.path.join( args.directory, '_site' )