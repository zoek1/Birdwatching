from sanic import Sanic
from sanic.response import json
from common.tasks import run_task

app = Sanic()

@app.route("/")
async def test(request):
    run_task.delay("delay")
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
