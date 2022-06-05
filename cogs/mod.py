from shutil import register_unpack_format
import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod commands are working!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("I don't recognise that command!")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title = "Error!",
                description = "Please specify the necessary arguments!",
                colour = discord.Colour.blurple()
            )
            await ctx.send(embed=embed)

    @commands.command() #Purge
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            description = (f'Cleared {amount} messages.'),
            colour = discord.Colour.blurple()
        )
        await ctx.send(embed=embed)



    @commands.command() #Kick
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            description = (f'{member.mention} was kicked for {reason}.'),
            colour = discord.Colour.blurple()
        )
        await ctx.send(embed=embed)

    @commands.command() #Ban
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            description = (f'{member.mention} was banned for {reason}.'),
            colour = discord.Colour.blurple()
        )
        await ctx.send(embed=embed)

    @commands.command() #Unban
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
            description = (f'{member.mention} was unbanned.'),
            colour = discord.Colour.blurple()
        )
        await ctx.send(embed=embed)

    @commands.command() #Mute
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        if reason == None:
            await ctx.send("Please state a reason!")
            return
        guild = ctx.guild
        muteRole = discord.utils.get(guild.roles, name = "Muted")

        if not muteRole:
            await ctx.send("No mute role found! Creating one...")
            muteRole = await guild.create_role(name = "Muted")

            for channel in guild.channels:
                await channel.set_permissions(muteRole, speak = False, send_messages = False, read_messages = True, read_message_history = True)
                await member.add_roles(muteRole)
                await ctx.send(f'{member.mention} has been muted in {ctx.guild} ')

def setup(client):
    client.add_cog(Mod(client))

