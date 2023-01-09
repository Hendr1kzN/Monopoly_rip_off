import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("Token")

intents=discord.Intents.all()
discord_bot = commands.Bot(command_prefix='!', intents=intents)
    
@discord_bot.command(name='senddata')
async def send_data(ctx):
    await ctx.send("hello there")

@discord_bot.command(name="join")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not ctx.guild.voice_client in discord_bot.voice_clients:
        await channel.connect()
    else:
        await ctx.send("I'm already connected!")

@discord_bot.command(name="dc")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if ctx.guild.voice_client in discord_bot.voice_clients:
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
    
@discord_bot.command(name="add")
async def add_player(ctx):
    
    
    
       
@discord_bot.command(name="play")#start game
async def start_game(ctx):
    pass

discord_bot.run(TOKEN)