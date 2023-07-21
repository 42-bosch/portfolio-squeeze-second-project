import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from filldata import ExcelToDatabase


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".xlsx"):
            print(f"File created: {event.src_path}")
            excel_to_database = ExcelToDatabase(event.src_path)
            excel_to_database.import_to_database()
            try:
                os.remove(self.data.file_path)
                (f"File {self.data.file_path} has been deleted after import.")
            except Exception as e:
                print(f"Error deleting the file: {e}")

    def on_deleted(self, event):
        pass


def start_observer(directory, timeout=1):
    observer = Observer()
    try:
        observer.schedule(MyHandler(), directory,recursive=False)
        observer.start()
        while True:
            time.sleep(timeout)

    except KeyboardInterrupt:
        print("Stopping observer...")
    except FileNotFoundError:
        print("Directory not found or path is incorrect.")
    except PermissionError:
        print("Permission denied. Try running the script as an administrator.")
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    directory_to_watch = "/cache"
    start_observer(directory_to_watch)
