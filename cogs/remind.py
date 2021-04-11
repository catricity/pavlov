import discord
import os
import requests
import json
import random

import constants # not needed #

from discord.utils import get
from discord.ext import commands

# # Category - Remind #
class remind(commands.Cog, name = "Remind"):
     def __init__(self, bot):
         self.bot = bot

     @commands.Cog.listener()
     async def on_ready(self):
         print('Remind cog is Working')

     # Remind Function #
     @commands.command(name = "remind", help = "Set a custom, subscribable reminder")
     async def remind_embed(self, ctx: commands.Context):
        # if ctx.channel.id == constants.CHANNEL_UNIT_JOIN:
        #      return
        
        var = None

        if var is None:
            embed = discord.Embed(description = "Please try again. You need to tell me what you want me to remind you about.")
        await ctx.send(embed = embed)

        

def setup(bot):
     bot.add_cog(remind(bot))


