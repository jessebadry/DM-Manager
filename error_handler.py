from discord.errors import InvalidArgument
from exceptions import *
import traceback

def handle_errors(func):
    """Implements the error system by try-excepting `func` callback.

    :param func: any function that's first parameter is a Discord Context object
    :preconditi
    :precondition: `func.__name__` must be prefixed with '_com'


    :return: inner function containing try-catched version of `func`
    """

    async def inner(*args, **kwargs):
        print(args)
        context = args[0]
        try:
            await func(*args, **kwargs)

        except NotImplementedError:
            await context.send(f"🚧🚧 This command is still under development!! 🚧🚧")

        except NoCampaignSelectedError:
            await context.send("No campaign is selected! Use ` \`help camp ` for some help dumb dumbs :)")

        except InvalidKeyException as err:
            model_name = err.model_name
            key = err.key_name
            allowed_fields = err.allowed_fields
            fields = '\n'.join(allowed_fields)
            f"Allowed fields:\n       👇\n{fields}"
        except InvalidCommandException as e:
            await context.send("Invalid command!")
        except Exception as e:
            # Debug
            # TODO log instead of print?
            traceback.print_exc()
            await context.send(f"Unexpected error occured.. Error: {e}")

    return inner
