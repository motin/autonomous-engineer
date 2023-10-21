import discord
from discord.ext import commands
from pydantic import BaseSettings

from discord import Intents

class Config(BaseSettings):
    TOKEN: str

    class Config:
        env_file = ".env"

config = Config()

intents = Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run(config.TOKEN)
