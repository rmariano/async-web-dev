import asyncio
import aiohttp

url = "http://localhost:2001"


@asyncio.coroutine
def request_greetings():
    resp = yield from aiohttp.get(url)
    text = yield from resp.text()
    return text


loop = asyncio.get_event_loop()
greetings = loop.run_until_complete(request_greetings())
print(greetings)
loop.close()
