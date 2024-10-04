import threading
import time
import os

def whoami(what):
    print("Process %s, Thread %s says: %s" % (os.getpid(), threading.current_thread(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=whoami, args=("I'm function %s" % n,))
        p.start()
