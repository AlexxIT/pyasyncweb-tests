import asyncio
import time

import aiohttp


async def get(session, url, sleep=0):
    t = time.time()
    await asyncio.sleep(sleep)
    await session.get(url)
    print(time.time() - t)


async def run():
    async with aiohttp.ClientSession() as session:
        tasks = [get(session, 'http://localhost:5000/sync?after=.1')
                 for i in range(4)]
        await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
