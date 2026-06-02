from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    count = r.get("visits")
    if count is None:
        count = 0
    count = int(count) + 1
    r.set("visits", count)
    return f"Hello! Page visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
