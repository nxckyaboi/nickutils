import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "n!")

@client.event
async def on_ready():
    print('The bot is logged in.')
    await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} servers!"))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
   
client.run("OTc5NDIzMzI1MzA4NzIzMjcw.GO76yB.UwcTQ132f7w1ElfX_9zrMochDuyZIemr-lq-AA")