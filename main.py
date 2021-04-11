import discord
import os
import requests
import random

from secrets import DISCORD_TOKEN

from discord.utils import DISCORD_EPOCH, get
from discord.ext import commands

initial_extensions = ['cogs.remind','cogs.UNE_Links','cogs.forscience_Links','cogs.study_resources']

client = discord.Client()
bot = commands.Bot(command_prefix = '!', description = "Pavlov here, happy to help. Use '!' as a prefix for any command.")
member = client.user

if __name__ == '__main__': 
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "the dogs"))
    print("Pavlov here, happy to help. Use '!' as a prefix for any command.")



# The bot says hello #
@bot.command(name = "hi", help = "Greetings from Pavlov")
async def hello(ctx: commands.Context):
    await ctx.channel.send("Hello!")





bot.run(DISCORD_TOKEN)
