from flask import Flask, request
import redis
from rq import Queue
import time, datetime

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)


def background_task(n):
    delay = 2
    print("task is running")
    print(len(n))
    with open("oke.txt", "a+") as f:
        f.writelines(f'[{datetime.datetime.now().strftime("%c")}] - {n}\n')
    print("task is finished")

    return len(n)


@app.route("/")
def index():
    return "Hello world! "


@app.route("/task")
def add_task():
    if request.args.get("n"):
        job = q.enqueue(background_task, request.args.get("n"))
        q_len = len(q)  # length of antrian in the celery

        return f"Task {job.id} added to queue at {job.enqueued_at}. {q_len} task in the queue\n{request.args.get('n')}"

    else:
        return "No value for n"


if __name__ == "__main__":
    app.run(debug=True)
