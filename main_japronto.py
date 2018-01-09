import asyncio
import time

from japronto import Application


async def get_sync(request):
    time.sleep(5)
    return request.Response(text='OK')


async def get_async(request):
    await asyncio.sleep(5)
    return request.Response(text='OK')


app = Application()
app.router.add_route('/sync', get_sync)
app.router.add_route('/async', get_async)
app.run(port=5000)
