import discord
from discord.ext import commands
import requests

host = "hypixel.net"
curseforgeID = '925200'

class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="servidor_status", description="Verifica se o servidor está online ou não.")
    async def servidor_status(self, ctx: discord.ApplicationContext):
        response = requests.get(f'https://api.mcstatus.io/v2/status/java/{host}')
        data = response.json()
        status = data['online']
        if status:
            await ctx.respond('Servidor online!', ephemeral=True)
        else:
            await ctx.respond('Servidor offline!', ephemeral=True)

    @discord.slash_command(name="players_online", description="Verifica quantos players tem online.")
    async def players_online(self, ctx: discord.ApplicationContext):
        response = requests.get(f'https://api.mcstatus.io/v2/status/java/{host}')
        data = response.json()
        player_count = data['players']['online']
        await ctx.respond(f'Players online: {player_count}', ephemeral=True)
    
    @discord.slash_command(name='modpack', description='Retorna informações da última versão da modpack do servidor.')
    async def get_modpack(self, ctx: discord.ApplicationContext):
        response = requests.get('https://api.cfwidget.com/925200')
        data = response.json()
        name = data['title']
        url = data['urls']['curseforge']
        await ctx.respond(f'Nome {name} \nURL: {url}', ephemeral=True)

def setup(bot):
    bot.add_cog(Utilities(bot))