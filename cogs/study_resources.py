import discord
import os
import requests
import json
import random

import constants

from discord.utils import get
from discord.ext import commands

# Category - General #
class study_resources(commands.Cog, name = "Study Resources"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('The Study Resources Module is Working')

    # Australian Psychological Society #
    @commands.command(name = "aps", help = "Provides a link to the Australian Psychological Society")
    async def embed(ctx: commands.Context):
        if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
            return

        embed = discord.Embed(title = "Australian Psychological Society", url = "https://www.psychology.org.au/", description = "Go to the Australian Pscyhological Society Website", color = 0x966e2c)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/815090739603570699/815095080234385478/appheader-logo-dt-1x.png")
    
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(study_resources(bot))