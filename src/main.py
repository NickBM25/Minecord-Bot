import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = discord.Bot()

@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f"Bot {bot.user} ligado - BEEP BOOP")

base_path = os.path.dirname(os.path.abspath(__file__))
cogs_folder = os.path.join(base_path, 'cogs')
for filename in os.listdir(cogs_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        extension_name = f"cogs.{filename[:-3]}"
        bot.load_extension(extension_name)

bot.run(TOKEN)