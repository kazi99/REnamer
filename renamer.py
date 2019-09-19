#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

dump_to_folder = "/Users/thrawn/Desktop/dump"
sorted_folder = "/Users/thrawn/Desktop/sorted"

def nice_counter(n):
    num_zeroes = 3 - len(str(n))
    return '-' + num_zeroes * '0' + str(n) 

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
    #spremeni path, odmakni extension, spremeni ime, vrni nazaj extension
        i = len(os.listdir(sorted_folder))
        for file_name in os.listdir(dump_to_folder):
            extension = ''
            name = file_name
            if str(str(os.path.splitext(file_name)[1])) != '':
                extension = str(os.path.splitext(file_name)[1])
                name = str(os.path.splitext(file_name)[0])
            
            name += nice_counter(i)
            name += extension
            i += 1
            os.rename(dump_to_folder + '/' + file_name, dump_to_folder + '/' + name)

            old_path = dump_to_folder + '/' + name
            new_path = sorted_folder + '/' + name
            os.rename(old_path, new_path)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, dump_to_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
