import asyncio
import time

async def send_mail(num):
    print(f'Сообщение отправлено: {num}')
    await asyncio.sleep(0.5)
    print(f'Сообщение: {num} доставлено')

async def main():
    for i in range(10):
        await send_mail(i)

start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {start - time.time()} секунд.')