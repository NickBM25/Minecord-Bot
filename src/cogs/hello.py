import discord
from discord.ext import commands

class Hello(commands.Cog): #puxa herança de commands.cog
    
    def __init__(self, bot): #construtor do bot para a cog
        self.bot = bot
        
    @discord.slash_command(name="hello", description="beep boop")
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond("Se você está lendo isso, saiba que o dev sofreu :skull_crossbones:", ephemeral=True) #
        
def setup(bot): # setup the cog
    bot.add_cog(Hello(bot)) # add the cog to the bot

        
    