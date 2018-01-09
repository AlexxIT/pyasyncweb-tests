import asyncio
import logging
import time

import aiohttp

_LOGGER = logging.getLogger(__name__)


async def get(session, url, sleep=0):
    t = time.time()
    await asyncio.sleep(sleep)
    await session.get(url)
    _LOGGER.info(time.time() - t)


async def run():
    async with aiohttp.ClientSession() as session:
        tasks = [get(session, 'http://localhost:5000/sync?after=.1', i)
                 for i in range(4)]
        await asyncio.wait(tasks)


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s [%(name)s] %(message)s")

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
