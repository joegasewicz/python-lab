"""
Coroutines #3
Modern approach using TaskGroup() context manager

"""
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(2, "Finish"))
        task2 = tg.create_task(say_after(1, "Start"))

        print(f"Started at {time.strftime('%X')}")
    print(f"Completed at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
