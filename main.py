"""

This is china's very own DnD bot ! :)

Author: 



"""


import commands as lib_commands
import discord
from discord.errors import *
from discord.ext import commands
import os
from commands.error_handler import handle_errors
from dm_manager import DMManager

import utils

manager = DMManager('data.json')
print('Manager loaded!')

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='`')


def dm_command(func):
    
    name = func.__name__
    func.__name__ = name+'1'

    @handle_errors
    async def inner(ctx):
        print('inner=', args[0])
        return func(*args, **kwargs)

    print('name=', name)
    inner.__name__ = name

    return inner


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}, id: {bot.user.id}")


@bot.command()
@dm_command
async def init_add(context, number_message: str):
    
    raise NotImplementedError()
    user_id = utils.get_user_id(context)
    current_campaign = dm_manager.get_campaign()

    dm_manager.add_init(int(number_message))


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
