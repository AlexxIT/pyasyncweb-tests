import asyncio
import time

from sanic import Sanic
from sanic.response import text

app = Sanic()


@app.route("/sync")
async def get_sync(request):
    if 'before' in request.args:
        await asyncio.sleep(float(request.args.get('before')))
    time.sleep(float(request.args.get('sleep', 5)))
    if 'after' in request.args:
        await asyncio.sleep(float(request.args.get('after')))
    return text('OK')


@app.route("/async")
async def get_async(request):
    await asyncio.sleep(5)
    return text('OK')


app.run(host="0.0.0.0", port=5000, access_log=False)
