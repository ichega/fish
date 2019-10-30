import time
import threading


class BackgroundTask(threading.Thread):
    def __init__(self, task=None, interval=1, **kwargs):
        super().__init__()
        self.task = task
        self.interval = interval
        self.stop = False
        self.task_kwargs = kwargs


    def run(self):
        if self.task is None:
            return
        while not self.stop:
            self.task(**self.task_kwargs)
            time.sleep(self.interval)
