import time
class clock:
    def __init__(self):
        self.start = time.time()
    def reset(self):
        self.start = time.time()
    def time_passed(self):
        return time.time() - self.start