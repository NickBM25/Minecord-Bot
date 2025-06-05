import discord
from discord.ext import commands

class Teams(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(name='create_team', description='Create a new team channel')
    async def create_team(self, ctx:discord.ApplicationContext, name: str):
        guild = ctx.guild
        await guild.create_role(name="")
