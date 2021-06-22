import discord
from discord.errors import *
from discord.ext import commands
import os
import asyncio
from dm_data import DMManager

import utils

manager = DMManager('data.json')

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='`')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}, id: {bot.user.id}")

"""Adds another user to this DM-Users initiative order list. """
@bot.command()
async def init_add(ctx, message):
    usr_id = utils.get_usr_id(ctx)
    print(message, 'from', usr_id)


"""Drives the main program.

:raises ValueError: if the DM_BOT key is missing from the system environment variables. 
 """
def main():

    TOKEN = os.getenv('dm_bot')

    # Exception checks
    if not TOKEN:
        raise ValueError(
            "Token is missing! Please add 'DM_BOT'={YOUR SECRET KEY} to your environment variables. ")

   
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure as e:
        print(f"The token provided, '{TOKEN}' is invalid."
              "Please provide a login/access token under DM_BOT in your environment vars.")


if __name__ == '__main__':
    main()
