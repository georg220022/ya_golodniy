import asyncio
import aiohttp
import time
from functools import wraps


URL = "http://httpbin.org/delay/3"
TIMEOUT = aiohttp.ClientTimeout(total=8)
LIMIT = asyncio.Semaphore(100)
TOTAL_REQUEST = 100
count = [1]


def my_decors(func):
    @wraps(func)
    async def wrap(*args, **kwargs):
        start = time.perf_counter()
        res = await func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\nВремя выполнения 100 запросов: {end-start:.7f}")
        return res

    return wrap


async def check_status(session, host):
    async with LIMIT:
        try:
            async with session.get(host, timeout=TIMEOUT) as response:
                return f"Запрос {count[0]}: {response.status}"
        except asyncio.TimeoutError:
            return f"Запрос {count[0]}: TimeoutError"
        finally:
            count[0] += 1


@my_decors
async def run(url):
    async with aiohttp.ClientSession() as session:
        # Впендюрил сюда еще таймаут(wait_for) который по хорошему отлавливать бы ... :)
        print(
            await asyncio.gather(
                *[
                    asyncio.wait_for(task, timeout=10)
                    for task in [
                        asyncio.create_task(check_status(session, url))
                        for _ in range(TOTAL_REQUEST)
                    ]
                ],
                return_exceptions=True,
            )
        )


if __name__ == "__main__":
    asyncio.run(run(URL))
