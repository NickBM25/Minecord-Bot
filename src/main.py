import os
import discord
from dotenv import load_dotenv

#token, thats it.
load_dotenv()
TOKEN = os.getenv('TOKEN')

#setup intents and instantiate the bot
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

#print in console when the bot is ready.
@bot.event
async def on_ready():
    print(f"Bot {bot.user} ligado - BEEP BOOP")

#load cogs
bot.load_extension('cogs.greetings')


bot.run(TOKEN) #runs the bot, hopefully.