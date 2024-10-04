import time
import os
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def task():
    print(f"Executing task in process: {os.getpid()}")
    time.sleep(1)


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=100) as executor:
        for _ in range(100):
            executor.submit(task)

        # 현재 실행 중인 프로세스 확인
        while True:
            active_processes = len(multiprocessing.active_children())  # 실행 중인 프로세스 수
            print(f"Active processes: {active_processes}")
            time.sleep(0.5)
