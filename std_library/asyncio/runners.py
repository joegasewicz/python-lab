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
    asyncio.run(main(), debug=True)
