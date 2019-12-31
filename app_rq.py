from flask import Flask, request
import redis
from rq import Queue
import dill
import time

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
q = Queue(connection=r)

def background_task(n):
	delay = 2
	print("Task Running...")
	print(f'Simulating {delay} second delay')
	time.sleep(delay)
	print(len(n))
	print("Task Complete")

	return(len(n))
def count_words_at_url(url):
    """Just an example function that's called async."""
    resp = requests.get(url)
    return len(resp.text.split())
@app.route("/task")
def add_task():
	if request.args.get("n"):
		#job = q.enqueue(background_task, request.args.get("n"))
		job = q.enqueue(count_words_at_url, 'http://nvie.com')
		q_len = len(q)

		return f'Task {job.id} added to queue at {job.enqueued_at}. {q_len} tasks in the queue'
	return "No value for n"

if (__name__ == '__main__'):
	app.run()