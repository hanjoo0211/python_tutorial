import time
import threading
import multiprocessing

a = 0

def loop():
    global a
    for i in range(3):
        time.sleep(1)
        a += 1
        print(a)
        # continue
    # for i in range(50000000):
    #     pass


if __name__ == '__main__':
    # Single Thread
    start = time.time()
    loop()
    loop()
    loop()
    end = time.time()
    print('[Single Thread] total time: {}'.format(end - start))

    # Multi Thread
    start = time.time()
    thread1 = threading.Thread(target=loop)
    thread2 = threading.Thread(target=loop)
    thread3 = threading.Thread(target=loop)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    end = time.time()
    print('[Multi Thread] total time: {}'.format(end - start))

    # Multi Process
    start = time.time()
    process1 = multiprocessing.Process(target=loop)
    process2 = multiprocessing.Process(target=loop)
    process3 = multiprocessing.Process(target=loop)
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()
    end = time.time()
    print('[Multi Process] total time: {}'.format(end - start))
