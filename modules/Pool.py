import threading as th
import time

class Pool():
    """
    is a queue in format [function , args]
    """
    running = 0
    queue = [] 
    stop = 0
    actived = False

    def __init__(self,threads = 4):
        self.threads = threads
        th.Thread(target = self.run).start()

    def execute(self,func,args):
        self.running += 1
        try:
            if args == None:
                func()
            func(*args)
        except Exception as e:
            raise f"Thread pool exception [{e}]"
        finally:
            self.running -= 1

    def _run(self):
        while True:
            if self.running < self.threads and len(self.queue) > 0:
                lock = th.Lock()
                with lock:
                    func,args = self.queue.pop(0)
                    th.Thread(target = self.execute,args = [func,args]).start()
            else:
                time.sleep(0.00001)
            if self.stop == 1:
                break;

    def run(self):
        if self.actived:
            return
        self.actived = True
        th.Thread(target=self._run,daemon=True).start()
    
    def destroy(self):
        self.stop = 1  

    def add(self,func,args:list):
        self.queue.append([func,args])