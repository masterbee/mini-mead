import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Handler(PatternMatchingEventHandler):
    def __init__(self, patterns, ignore_patterns, ignore_directories, case_sensitive):
        PatternMatchingEventHandler.__init__(self, patterns, ignore_patterns, ignore_directories, case_sensitive )

    def on_deleted(self,event):
    	print('.:.  need to delete {}'.format( event.src_path ) )
    def on_modified(self, event):
    	print('.:.  need to run build {}'.format( event.src_path ) )
        # if event.src_path.lower().endswith('.less'):
        #     try: less(event.src_path, event.src_path[:-5] + '.css')
        #     except sh.ErrorReturnCode_1 as e: print e.stderr
        # if event.src_path.lower().endswith('.coffee'):
        #     try: coffee(event.src_path)
        #     except sh.ErrorReturnCode_1 as e: print e.stderr
    on_moved = on_modified
    on_created = on_modified

class Watcher:

	@staticmethod
	def create( path, patterns, ignore_patterns, ignore_directories, case_sensitive ):

		handler = Handler( patterns, ignore_patterns, ignore_directories, case_sensitive )
		observer = Observer()
		observer.schedule(handler, path, recursive=True)

		return observer;


	# @staticmethod
	# def console(level, message ):
	# 	stamp = datetime.now()
	# 	print("{} | {} | {} | {} | {}".format( stamp.strftime('%Y-%m-%d'), stamp.strftime('%H:%M:%S'), Logger.label, Logger.severity[level], message ))