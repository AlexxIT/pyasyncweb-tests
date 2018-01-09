import asyncio
import time

import aiohttp


async def get(session, url):
    t = time.time()
    await session.get(url)
    print(time.time() - t)


async def run():
    async with aiohttp.ClientSession() as session:
        tasks = [get(session, 'http://localhost:5000/sync')
                 for i in range(4)]
        await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
