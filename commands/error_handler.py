def handle_errors(func):
    async def inner(*args, **kwargs):
        context = args[0]
        try:
            await func(*args, **kwargs)

        except NotImplementedError:
            await context.send(f"🚧🚧 This command is still under development!! 🚧🚧")
        except Exception as e:
            print(e)
            await context.send(f"An unexpected error occurred : 👇\n {e} ")
    return inner