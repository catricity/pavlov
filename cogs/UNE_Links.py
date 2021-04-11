import discord
import os
import requests
import json
import random

import constants

from discord.utils import get
from discord.ext import commands

# Category - UNE Links #
class UNE_Links(commands.Cog, name = "UNE Links"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('UNE Links is Working')

    # UNE Principal Dates #
    @commands.command(name = "dates", help = "Provides a link to UNE Principal Dates")
    async def dates_embed(self, ctx: commands.Context):
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "UNE Principal Dates", url = "https://www.une.edu.au/about-une/principal-dates", description = "View important dates on the UNE Calendar for the year.\n\nThis link opens to the UNE website.", color = 0x43B02A)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/815090806423158784/une-logo.png")

        await ctx.send(embed = embed)

    # Moodle Home Page #
    @commands.command(name = "moodle", help = "Provides a link to UNE Moodle Home Page")
    async def moodle_embed(self, ctx: commands.Context):
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "UNE Moodle", url = "https://moodle.une.edu.au/", description = "A direct link to the UNE Moodle Home Page", color = 0x43B02A)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/815096545619869706/unknown.png")

        await ctx.send(embed = embed)

    # myUNE Home Page #
    @commands.command(name = "myune", help = "A direct link to the myUNE Home Page")
    async def myune_embed(self, ctx: commands.Context):
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "myUNE", url = "https://my.une.edu.au/", description = "A direct link to the myUNE Home Page", color = 0x43B02A)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/815090806423158784/une-logo.png")

        await ctx.send(embed = embed)

    # UNE Library #
    @commands.command(name = "library", help = "A direct link to the UNE Library")
    async def library_embed(self, ctx: commands.Context):
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "UNE Library", url = "https://www.une.edu.au/library", description = "A direct link to the UNE Library home page", color = 0x43B02A)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/815090806423158784/une-logo.png")

        await ctx.send(embed = embed)    

def setup(bot):
    bot.add_cog(UNE_Links(bot))
