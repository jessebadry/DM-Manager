"""

This is china's very own DnD bot ! :)

Author: 



"""


from exceptions import InvalidCommandException
import discord
from discord.errors import *
from discord.ext import commands
import os

from dm_manager import DMManager
from error_handler import handle_errors
import utils
from argparse import ArgumentParser
manager = DMManager('data.json')
print('Manager loaded!')

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='`')


def add_arguments(parser, args):

    for parser_arg in args:

        arg_name = parser_arg[0]

        if len(parser_arg) == 2:
            arg_kwargs = parser_arg[1]

        parser.add_argument(arg_name, **arg_kwargs)


def dm_command(*args, **kwargs):
    """Decorates func with handle_errors decorator and bot.command decorator.

    :param func: an asynchronous function with a single paramater (discord context)
    :precondition: func takes a single parameter (discord context)

     """

    parser = ArgumentParser()

    add_arguments(parser, args)

    def decorator(func):

        @handle_errors
        async def inner(context):
            # Skip command name from msg_content
            msg_content = context.message.content.split()[1:]

            try:
                args = parser.parse_args(msg_content)
            except SystemExit:
                raise InvalidCommandException()


            return await func(context, args)

        name = func.__name__
        func.__name__ = ''
        inner.__name__ = name
        return bot.command()(inner)

    return decorator


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}, id: {bot.user.id}")


@dm_command()
async def init_add(context, args):
    raise NotImplementedError()
    user_id = utils.get_user_id(context)
    current_campaign = dm_manager.get_campaign()

    dm_manager.add_init(int(number_message))


@dm_command(("key", {}), ("--value", {'nargs': '*'}))
async def camp(ctx, args):
    value = ' '.join(args.value) if args.value else args.value
    result = manager.camp(args.key, value)
    if result:
        await ctx.send(result)


def main():
    """Drives the main program.

    :raises ValueError: if the DM_BOT key is missing from the system environment variables. 
    """

    TOKEN = os.getenv('dm_bot')

    # Exception checks
    if not TOKEN:
        raise ValueError(
            "Token is missing! Please add 'DM_BOT'={YOUR SECRET KEY} to your environment variables. ")

    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure as e:
        print(f"The token provided, '{TOKEN}' is invalid. Please provide"
              "a login/access token under DM_BOT in your environment vars.")


if __name__ == '__main__':
    main()
