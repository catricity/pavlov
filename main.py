import discord
import os
import requests
import json
import random
import constants
from secrets import DISCORD_TOKEN

from discord.utils import DISCORD_EPOCH, get
from discord.ext import commands

initial_extensions = ['cogs.remind','cogs.UNE_Links','cogs.forscience_Links','cogs.study_resources','cogs.definition']

client = discord.Client()
bot = commands.Bot(command_prefix = '!', description = "Pavlov here, happy to help. Use '!' as a prefix for any command.")
member = client.user

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

if __name__ == '__main__': #load modules defined in initial_extensions
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "the dogs"))
    print("Pavlov here, happy to help. Use '!' as a prefix for any command.")

# Gosh, you're breathtaking #
@bot.command(name = "keanu", help = "Tell someone they're breathtaking.")
async def keanu(ctx: commands.Context):
    await ctx.channel.send("You're breathtaking.")

# The bot says hello #
@bot.command(name = "hello", help = "Greetings from Pavlov")
async def hello(ctx: commands.Context):
    await ctx.channel.send("Hello!")

# Be Inspiring #
@bot.command(name = "inspire", help = "Receive an inspirational quote")
async def inspire(ctx):
    quote = get_quote()
    await ctx.channel.send(quote)

# User can request access to new role #
@bot.command(name = "join", help = "Request access to new area")
async def addrole(ctx: commands.Context, *, course: str):
    # exit command if not the desired channel.
    if ctx.channel.id != constants.CHANNEL_UNIT_JOIN:
        return

    # Get role that matches argument.
    role = next(filter(lambda r: r.name.lower() == course.lower(), ctx.guild.roles[4:-5]), None)

    # role not found
    if role is None:
        return

    # role already assigned
    if role in ctx.author.roles:
        await ctx.channel.send(f"You've already joined {role.name}, {ctx.author.mention}")
        return

    # Assign role
    try:
        await ctx.author.add_roles(role)
        await ctx.channel.send(f"{ctx.author.mention} has joined {role.name}")
    except discord.errors.Forbidden:
        return

# User can request to leave role #
@bot.command(name = "leave", help = "Remove access to area")
async def removerole(ctx: commands.Context, *, course: str):
    # exit command if not the desired channel.
    if ctx.channel.id != constants.CHANNEL_UNIT_JOIN:
        return

    # Get role that matches argument.
    role = next(filter(lambda r: r.name.lower() == course.lower(), ctx.guild.roles[4:-5]), None)

    # role not found
    if role is None:
        return

    # role not assigned
    if role not in ctx.author.roles:
        await ctx.channel.send(f"You're not in {role.name}, {ctx.author.mention}")
        return

    # Remove role
    try:
        await ctx.author.remove_roles(role)
        await ctx.channel.send(f"{ctx.author.mention} has left {role.name}")
    except discord.errors.Forbidden:
        return

# Show list of available roles #
@bot.command(name = "rolecall", aliases = ["roles","listroles","rolelist","showroles"], help = "Shows a list of available access areas")
async def rolecall(ctx: commands.Context):
    # exit command if not the desired channel.
    if ctx.channel.id != constants.CHANNEL_UNIT_JOIN:
        return

    roles = ', '.join(map(lambda r: f"`{r.name}`", ctx.guild.roles[4:-5]))

    await ctx.channel.send(roles)

bot.run(DISCORD_TOKEN)
