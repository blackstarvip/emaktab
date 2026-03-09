from queue import Queue
from threading import Thread
from worker import login_student

task_queue = Queue()

print("QUEUE MANAGER LOADED", flush=True)
def worker():

    while True:

        login,password = task_queue.get()

        login_student(login,password)

        task_queue.task_done()

for i in range(3):

    t = Thread(target=worker)

    t.daemon = True

    t.start()


def add_task(login,password):

    task_queue.put((login,password))
