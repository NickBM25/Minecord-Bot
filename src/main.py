import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ligado - BEEP BOOP")

bot.load_extension('cogs.hello')

bot.run(TOKEN)