import concurrent.futures
import math
import time
import sys
import os


def calc(val):
    time.sleep(1)
    return math.sqrt(float(val))


def use_threads(num, values):
    t1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num) as executor:
        results = executor.map(calc, values)
        print("workers: ", executor._max_workers)
    t2 = time.time()
    print("Threads: {} Time: {}".format(num, t2 - t1))


def use_processes(num, values):
    t1 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=num) as executor:
        results = executor.map(calc, values)
        print("workers: ", executor._max_workers)
    t2 = time.time()
    print("Processes: {} Time: {}".format(num, t2 - t1))


if __name__ == "__main__":
    print("CPUs: ", os.cpu_count())
    workers = int(sys.argv[1])
    if workers < 1:
        workers = None
    values = [i for i in range(1, 11)]
    use_threads(workers, values)
    use_processes(workers, values)
