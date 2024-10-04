import time
import threading
from concurrent.futures import ThreadPoolExecutor

def task():
    print(f"Executing task in thread: {threading.current_thread().name}")
    time.sleep(1)

with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(100):
        executor.submit(task)
    
    # 현재 실행 중인 스레드 확인
    while True:
        active_threads = threading.active_count()  # 실행 중인 전체 스레드 수
        print(f"Active threads: {active_threads}")
        time.sleep(0.5)
