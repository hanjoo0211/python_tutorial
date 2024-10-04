import multiprocessing as mp
import time
import os

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def washer(dishes, output):
    for dish in dishes:
        whoami(dish)
        print('Washing', dish, 'dish')
        time.sleep(1)
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        whoami(dish)
        print('Drying', dish, 'dish')
        time.sleep(1)
        input.task_done()

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()  # block until all dishes are done
    print('All done')