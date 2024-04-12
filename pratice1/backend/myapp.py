from flask import Flask, Response, render_template
from redis import Redis

app = Flask(__name__)
redis_client = Redis(host='redisdb', port=6379, decode_responses=True)

@app.route("/")
def index():
	student = redis_client.get('student') 
	return Response(render_template('index.html', student=student)), 200

if __name__ == "__main__":
	app(environs, start_response)
