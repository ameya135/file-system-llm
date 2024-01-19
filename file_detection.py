import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from file_description import describe, update_json

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_modified = (None,None)
    
    def on_created(self, event):
        if event.is_directory:
            return
        # Add your custom action here for when a file is created
        file = os.path.abspath(event.src_path)
        print(file)
        # agent,assistant = describe(file)
        # res = agent.last_message(assistant)['content']
        # # res is a string, show me the sam,e string but remove the work TERMINATE from it,
        # res = res.replace("TERMINATE", "")
        # print("New file added!")
        # update_json(file, res)
        # time.sleep(1000)
    
    def on_modified(self, event):
        if event.is_directory:
            return
        file = os.path.abspath(event.src_path)
        filename = os.path.basename(file)
        now = time.time()
        if (filename, now) != self.last_modified:
            self.last_modified = (filename, now)
            print(f"File modified: {filename}")
                    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = MyHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1000)
            break
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
