from .threaded import ThreadedServer


def get( config ):
	return ThreadedServer.create( config )

