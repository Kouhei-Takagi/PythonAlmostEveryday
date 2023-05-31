import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())

import asyncio

async def my_async_function():
    # 非同期な処理を実行
    await asyncio.sleep(1)
    print("非同期処理完了")

async def main():
    # 非同期処理のタスクを作成
    task = asyncio.create_task(my_async_function())

    # 他の処理を実行
    print("他の処理")

    # 非同期処理の完了を待つ
    await task

asyncio.run(main())

import asyncio
import httpx

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def scrape_websites(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_data(url))
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    return results

# メイン関数
async def main():
    urls = [
        "https://www.yahoo.com",
        "https://www.google.com",
        "https://openai.com"
    ]
    
    scraped_data = await scrape_websites(urls)
    for url, data in zip(urls, scraped_data):
        print(f"Data from {url}:")
        print(data)
        print()

# メインループ
if __name__ == "__main__":
    asyncio.run(main())
