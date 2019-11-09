import os
from .watcher import Watcher

# TODO: Add parameter to be passed here 
def bubble( path=os.getcwd(), patterns="*", ignore_patterns="", ignore_directories=False, case_sensitive=True ):
	return Watcher.create(path, patterns, ignore_patterns, ignore_directories, case_sensitive)