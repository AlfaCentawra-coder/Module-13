import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    Pasha = asyncio.create_task(start_strongman('Паша', 3))
    Denis = asyncio.create_task(start_strongman('Денис', 4))
    Apollon = asyncio.create_task(start_strongman('Аполлон', 5))
    await asyncio.gather(Pasha, Denis, Apollon)

start = time.time()
asyncio.run(start_tournament())
end = time.time()
print(f"Время выполнения программы {round((end - start), 2)}")

