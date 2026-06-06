"""
Runners
=======

Runners are high level asyncio primitives built on top of the event loop
to simplify async code.
"""
import asyncio


async def main():
    print("start")
    await asyncio.sleep(1)
    print("end")


if __name__ == "__main__":
    # asyncio.run() wraps the main() coroutine in a Task to get scheduled to run
    # on the event loop.
    asyncio.run(main(), debug=True)
