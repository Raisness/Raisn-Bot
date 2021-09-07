import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="r")


@bot.event
async def on_ready():
  print("Ready")
  
  
bot.run("YOUR_TOKEN_HERE")
