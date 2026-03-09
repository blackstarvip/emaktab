from queue import Queue
from threading import Thread
from worker import login_student

task_queue = Queue()

print("QUEUE MANAGER LOADED", flush=True)
def worker():
    print("WORKER STARTED", flush=True)

    while True:
        login,password = task_queue.get()

        print("QUEUE RECEIVED:", login, flush=True)

        result = login_student(login,password)

        print("LOGIN RESULT:", result, flush=True)

        task_queue.task_done()

for i in range(3):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

print("WORKERS INITIALIZED", flush=True)


def add_task(login,password):

    task_queue.put((login,password))
