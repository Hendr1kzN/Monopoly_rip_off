import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("Token")

list_of_players = []
CHANNEL_NAME = 'testen-hier'


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


@discord_bot.command(name="do_poll")
async def ex(ctx):
    channel = ctx.message.channel

    vote = discord.Embed(title="**[Monopoly]**", description="It's time to join the lobby", color=0x00ff00)
    message = await ctx.send(embed=vote)
    reaction = await message.add_reaction("✅")

    async for user in reaction.users():
        await channel.send(f'{user} has reacted with {message.emoji}!')


@discord_bot.command(name="join_lobby")
async def join_lobby(ctx):
    id = ctx.message.author.mention
    if not id in list_of_players:
        list_of_players.append(id)
        await ctx.send(f"{id} entered the lobby")
    else:
        await ctx.send(f"{id} you're already in the lobby")

 
@discord_bot.command(name="leave_lobby")
async def leave_lobby(ctx):
    id = ctx.message.author.mention
    if id in list_of_players:
        list_of_players.remove(id)
        await ctx.send(f"{id} left the lobby")
    else:
        await ctx.send(f"{id} you're not in the lobby")


@discord_bot.command(name="lobby")
async def return_player_in_lobby(ctx):
    if len(list_of_players) > 0:
        await ctx.send("The players are:")
        for player in list_of_players:
            await ctx.send(player)
    else:
        await ctx.send("The lobby is empty.")


@discord_bot.command(name="play")#start game
async def start_game(ctx):
    pass

discord_bot.run(TOKEN)