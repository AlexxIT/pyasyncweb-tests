import asyncio
import time

from sanic import Sanic
from sanic.response import text
from sanic.server import serve

app = Sanic()


@app.route("/sync")
async def get_sync(request):
    time.sleep(5)
    return text('OK')


@app.route("/async")
async def get_async(request):
    await asyncio.sleep(5)
    return text('OK')


loop = asyncio.get_event_loop()
server_settings = app._helper(host="0.0.0.0", port=5000, access_log=False,
                              loop=loop, run_async=True)
loop.run_until_complete(serve(**server_settings))
try:
    loop.run_forever()
finally:
    loop.close()
