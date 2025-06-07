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
        try:
            response = requests.get(f'https://api.mcstatus.io/v2/status/java/{host}')
            data = response.json()
            
            # Validate the API response has the expected structure
            if not isinstance(data, dict):
                await ctx.respond('Erro: Resposta da API inválida.', ephemeral=True)
                return
                
            # Use .get() method with a default value to avoid KeyError
            status = data.get('online', False)
            
            if status:
                await ctx.respond('Servidor online!', ephemeral=True)
            else:
                await ctx.respond('Servidor offline!', ephemeral=True)
        except Exception as e:
            await ctx.respond(f'Erro ao verificar status do servidor: {str(e)}', ephemeral=True)

    @discord.slash_command(name="players_online", description="Verifica quantos players tem online.")
    async def players_online(self, ctx: discord.ApplicationContext):
        try:
            response = requests.get(f'https://api.mcstatus.io/v2/status/java/{host}')
            data = response.json()
            
            # Validate the API response has the expected structure
            if not isinstance(data, dict):
                await ctx.respond('Erro: Resposta da API inválida.', ephemeral=True)
                return
                
            # Check if 'players' key exists and is a dictionary
            players_data = data.get('players')
            if not isinstance(players_data, dict):
                await ctx.respond('Erro: Dados de jogadores não disponíveis.', ephemeral=True)
                return
                
            # Use .get() with default value to avoid KeyError
            player_count = players_data.get('online', 0)
            await ctx.respond(f'Players online: {player_count}', ephemeral=True)
        except Exception as e:
            await ctx.respond(f'Erro ao verificar jogadores online: {str(e)}', ephemeral=True)
    
    @discord.slash_command(name='modpack', description='Retorna informações da última versão da modpack do servidor.')
    async def get_modpack(self, ctx: discord.ApplicationContext):
        try:
            response = requests.get('https://api.cfwidget.com/925200')
            data = response.json()
            
            # Validate the API response has the expected structure
            if not isinstance(data, dict):
                await ctx.respond('Erro: Resposta da API inválida.', ephemeral=True)
                return
                
            # Use .get() with default values to avoid KeyError
            name = data.get('title', 'Nome não disponível')
            
            # Check if 'urls' key exists and is a dictionary
            urls_data = data.get('urls')
            if not isinstance(urls_data, dict):
                await ctx.respond(f'Nome: {name}\nURL: Não disponível', ephemeral=True)
                return
                
            # Get the curseforge URL with a default value
            url = urls_data.get('curseforge', 'URL não disponível')
            
            await ctx.respond(f'Nome: {name}\nURL: {url}', ephemeral=True)
        except Exception as e:
            await ctx.respond(f'Erro ao obter informações da modpack: {str(e)}', ephemeral=True)

def setup(bot):
    bot.add_cog(Utilities(bot))