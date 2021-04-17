from discord import Message
from discord.ext import commands
from discord.ext.commands import Bot, context
import discord
import os
import re
import json
import requests
import constants

from discord.utils import get
from discord.ext import commands

def define(message: str):
    with open('cogs\psychology.json', "r") as fp:
        json_data: dict = json.load(fp)

        filteredMessage = message.lower()
        filteredMessage = re.sub(r"['\".,?!;:-]", "", filteredMessage)

        return json_data.get(filteredMessage)
    
class definition(commands.Cog, name="Psychology Definitions"):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name = "define", help = "Look up a psychological term or concept")
    async def define(self, ctx: commands.Context, *, term: str):
        # Don't allow responses in unit-join channel #
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return
        # Skip messages from this bot #
        if ctx.author.id == self.bot.user.id:
            return

        # Skip messages from all bots #
        if ctx.author.bot:
            return

        # Calls define function #
        result = define(term)

        if result is None:
            embed = discord.Embed(description = "Definition or concept not found.")
            await ctx.send(embed = embed)
            return

        embed = discord.Embed(description = result)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(definition(bot))