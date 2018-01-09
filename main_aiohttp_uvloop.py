import asyncio
import time

import uvloop
from aiohttp import web


async def get_sync(request):
    time.sleep(5)
    return web.Response(text='OK')


async def get_async(request):
    await asyncio.sleep(5)
    return web.Response(text='OK')


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = web.Application()
app.router.add_get('/sync', get_sync)
app.router.add_get('/async', get_async)
web.run_app(app, port=5000)
