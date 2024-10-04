import concurrent.futures
import math
import time
import sys
import os


def calc(val):
    return val, math.sqrt(float(val))


def use_threads(num, values):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num) as executor:
        tasks = [executor.submit(calc, val) for val in values]
        for task in concurrent.futures.as_completed(tasks):
            yield task.result()


def use_processes(num, values):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num) as executor:
        tasks = [executor.submit(calc, val) for val in values]
        for task in concurrent.futures.as_completed(tasks):
            yield task.result()


if __name__ == "__main__":
    workers = int(sys.argv[1])
    values = [i for i in range(1, 6)]
    threads = list(use_threads(workers, values))
    processes = list(use_processes(workers, values))
    for val, result in threads:
        print(f"Threads: {val} {result}")
    for val, result in processes:
        print(f"Processes: {val} {result}")
