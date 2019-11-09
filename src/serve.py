#!/usr/bin/env python3
import sys, flask, keg, time, froth


config = keg.tap()
server = flask.get( config )
observer = froth.bubble()

observer.start()
 	# endless loop while waiting for CTRL-C to
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
        # say goodbye nicely (and potentially end any running threads)
        server.server_close()
        observer.stop()
        observer.join()
        