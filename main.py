import discord
from discord.errors import *
from discord.ext import commands
import os
from dm_data import DMManager

import utils

manager = DMManager('data.json')


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='`')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}, id: {bot.user.id}")


@bot.command()
async def init_add(ctx, message):
    """Adds another user to this DM-Users initiative order list. """
    user_id = utils.get_user_id(ctx)
    
    



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
