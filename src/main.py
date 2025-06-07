import os
import discord
from dotenv import load_dotenv

#token, thats it.
load_dotenv()
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError('No Discord bot token found. Please set the TOKEN environment variable.')

#setup intents and instantiate the bot
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

#print in console when the bot is ready.
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

bot.run(TOKEN) #runs the bot, hopefully.