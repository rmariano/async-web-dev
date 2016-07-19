import time
import asyncio
import aiohttp

url = "http://localhost:2001?q={}"

ingredients = [
    "spam",
    "salt",
]

shelves = [url.format(ing) for ing in ingredients]


@asyncio.coroutine
def request_fridge():
    response_tasks = yield from asyncio.wait([aiohttp.get(shelf) for shelf in shelves])
    txt_tasks = yield from asyncio.wait([task.result().text() for task in response_tasks[0]])
    return [task.result() for task in txt_tasks[0]]


t0 = time.time()

loop = asyncio.get_event_loop()
tasks = loop.run_until_complete(request_fridge())
print(time.time() - t0, " seconds passed")
print(''.join(tasks))
loop.close()
