import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send('Ciao da Lemon! 🍋')

# Avvia il bot utilizzando il token
bot.run(os.getenv('DISCORD_TOKEN'))
