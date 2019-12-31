# FlaskRedisTaskQueue
Task Queue experimentation with docker


## redis docker instance
``` docker run --name some-redis -d redis ```

## celery worker
``` celery -A <tasks> worker --loglevel=info ```
	add ```-P gevent ``` keyword to the end of worker command