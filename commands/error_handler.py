from exceptions import *


def handle_errors(func):
    async def inner(*args, **kwargs):
        context = args[0]
        try:
            await func(*args, **kwargs)

        except NotImplementedError:
            await context.send(f"🚧🚧 This command is still under development!! 🚧🚧")
        except InvalidKeyException as err:
            model_name = err.model_name
            key = err.key_name
            allowed_fields = err.allowed_fields
            fields = '\n'.join(allowed_fields)
            f"Allowed fields:\n       👇\n{fields}"

    return inner
