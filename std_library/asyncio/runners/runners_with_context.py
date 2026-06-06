"""
Runners
=======

Runners are high level asyncio primitives built on top of the event loop
to simplify async code.
"""
import asyncio
import contextvars
from contextvars import ContextVar

user_details: ContextVar[dict] = contextvars.ContextVar("user_details")
user_details.set({"name": "Cosmo", "breed": "Ally-cat"})


async def main(time: int, order: int):
    print(f"Started coroutine #{order}")
    print(f"Context: {user_details.get()}")
    await asyncio.sleep(time)
    print("end")


if __name__ == "__main__":

    with asyncio.Runner() as runner:
        isolated_ctx = contextvars.copy_context()
        # If we pass the isolated context to run()'s context arg it will
        # pick up the updated scoped context values
        isolated_ctx.run(user_details.set, {"name": "Sumi", "breed": "Siberian"})
        # The run argument wraps the coroutine in a Task.
        runner.run(main(1, 1))
        runner.run(main(1, 2), context=isolated_ctx)
        print(f"Loop: {runner.get_loop()}")
        runner.close()
