import discord
from discord.ext import commands

class Greetings(commands.Cog):
    
    # instantiate the bot for the cog 
    def __init__(self, bot):
        self.bot = bot
    
    # /hello command
    @discord.slash_command(name="hello", description="beep boop")
    async def hello(self, ctx: discord.ApplicationContext):
        await ctx.respond("Se você está lendo isso, saiba que o dev sofreu :skull_crossbones:", ephemeral=True) #
        
    # welcome message
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="general")
        if channel:
            await channel.send(f'Bem-vindo ao servidor, {member.mention}!')

    # goodbye message
    
# setup the cog and add it to the bot
def setup(bot): 
    bot.add_cog(Greetings(bot))

        
    