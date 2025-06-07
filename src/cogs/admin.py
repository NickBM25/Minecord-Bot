import discord
import os
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="reload",
        description="Recarrega uma extensão do bot."
    )
    @commands.is_owner()
    async def reload(self, ctx: discord.ApplicationContext, extension: str):
        try:
            extension = f'cogs.{extension}'
            self.bot.reload_extension(extension)
            await ctx.respond(f":recycle: Cog `{extension}` recarregada com sucesso!", ephemeral=True)
        except Exception as e:
            await ctx.respond(f":x: Erro ao recarregar `{extension}`: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Admin(bot))