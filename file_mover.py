from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install for these packages to work

import os
import json
import time
import shutil

class Myhandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith('.png'):
                src_file = folder_to_track + "/" + filename
                shutil.move(src_file, folder_destination)
               

folder_to_track = "/Users/"
folder_destination = "/Users/"
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
