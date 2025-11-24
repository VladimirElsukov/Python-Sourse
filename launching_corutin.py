import asyncio
import time

async def send_mail(number):
    print(f"Сообщение отправлено: {number}")
    await asyncio.sleep(1)
    print(f"Сообщение доставлено: {number}")

async def main():
    task = [send_mail(i) for i in range(10)]
    await asyncio.gather(*task)

start_time = time.time()
asyncio.run(main())
print(f'Затраченное время: {time.time() - start_time} секунд')










