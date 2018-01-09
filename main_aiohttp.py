import asyncio
import time

from aiohttp import web


async def get_sync(request):
    if 'before' in request.query:
        await asyncio.sleep(float(request.query.get('before')))
    time.sleep(float(request.query.get('sleep', 5)))
    if 'after' in request.query:
        await asyncio.sleep(float(request.query.get('after')))
    return web.Response(text='OK')


async def get_async(request):
    await asyncio.sleep(5)
    return web.Response(text='OK')


app = web.Application()
app.router.add_get('/sync', get_sync)
app.router.add_get('/async', get_async)
web.run_app(app, port=5000)
