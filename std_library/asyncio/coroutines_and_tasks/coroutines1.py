"""
Coroutines #1
"""
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    """
    All coroutines will be called synchronously
    """
    await say_after(1, "Start")
    await say_after(2, "End")

    print("Finished all coroutines")


if __name__ == "__main__":
    asyncio.run(main())
