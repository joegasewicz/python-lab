"""
Coroutines #2
Using create_task() to run coroutines concurrently as asyncio Tasks.
"""
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"Started at {time.strftime('%X')}")
    task1 = asyncio.create_task(say_after(2, "Finish"))
    task2 = asyncio.create_task(say_after(1, "Start"))

    # Wait until both tasks are completed
    await task1
    await task2 # Will print out first as only 1 sec delay

    #  The event loop keeps track of which tasks have completed.

    print(f"Completed at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())
