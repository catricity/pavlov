import discord
import os
import requests
import json
import random

import constants

from discord.utils import get
from discord.ext import commands

# Category - For Science #
class forscience_Links(commands.Cog, name = "For Science"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('For Science Module is Working')

    # Open Science Framework #
    @commands.command(name = "osf", help = "Provides a link to the Open Science Framework")
    async def osf_embed(self, ctx: commands.Context):
       
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "Open Science Framework", url = "https://osf.io/", description = "Go to the Open Science Framework", color = 0x00a9df)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/827877707424464937/unknown.png")
        
        await ctx.send(embed = embed)

    # ORCID iD #
    @commands.command(name = "orcid", help = "Provides a link to ORCiD")
    async def embed(self, ctx: commands.Context):
        
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "ORCiD", url = "https://www.orcid.org/", description = "Go to ORCiD", color = 0xb857d0)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/827876455227981854/unknown.png")
    
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(forscience_Links(bot))