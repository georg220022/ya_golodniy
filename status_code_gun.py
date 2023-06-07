import asyncio
import aiohttp

timeout = aiohttp.ClientTimeout(total=5)
limit = asyncio.Semaphore(100)

async def check_status(session, host):
    async with limit:  
        try:
            async with session.get(host, timeout=timeout) as response:
                return response.status
        except asyncio.TimeoutError:
            return f'{host}: TimeoutError'
            
async def run(hosts): 
    async with aiohttp.ClientSession() as session:
        print(await asyncio.gather(*[check_status(session, host) for host in hosts], return_exceptions=True))
        
if __name__ == '__main__': 
    asyncio.run(run(hosts:=['https://www.google.com/', 'https://www.google.com/']))