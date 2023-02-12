import time
import celery


app = celery.Celery('tasks', backend='redis://127.0.0.1:6379/2', broker='redis://127.0.0.1:6379/1')


@app.task
def hard_function(arg):
    time.sleep(1)
    return 1
 