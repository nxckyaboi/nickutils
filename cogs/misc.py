import discord
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Misc commands are working!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "Error!",
                description = "Please specify a number!",
                colour = discord.Colour.blurple()
            )
            await ctx.send(embed=embed)

    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("I don't recognise that command!")

    @commands.command()
    async def socials(self, ctx):
        embed = discord.Embed (
            title = "Socials by the bot developer",
            description = "Nickamite doesn't have any socials at the moment, but maybe soon",
            colour = discord.Colour.blurple()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def servers(self, ctx):
        embed = discord.Embed (
            description = (f"Nick's Utilities is in {len(self.client.guilds)} servers!"),
            colour = discord.Colour.blurple()
        )
        await ctx.send(embed=embed) 

def setup(client):
    client.add_cog(Misc(client))
