import discord
from discord.ext import commands
import requests
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("Token")

list_of_players = []
CHANNEL_NAME = 'testen-hier'


intents=discord.Intents.all()
intents.message_content = True
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


async def lobby_join_helper(ctx, user):
    if len(list_of_players)>=6:
        await ctx.send(f"Sorry, {user.mention}. The lobby is full.")
    elif not user.mention in list_of_players:
        list_of_players.append(user.mention)
        await ctx.send(f'{user.mention} joined lobby')
        img_data = requests.get(user.avatar.url).content
        filename = (f"{user}_avatar.jpg")
        path = f"Avatars/{filename}"
        with open(path, 'wb') as localFile:
            localFile.write(img_data)
    else:
        await ctx.send(f"{user.mention} you're already in the lobby")


async def lobby_leave_helper(ctx, user):
    if user.mention in list_of_players:
        list_of_players.remove(user.mention)
        await ctx.send(f"{user.mention} left the lobby")
        filename = (f"{user}_avatar.jpg")
        path = f"Avatars/{filename}"
        os.remove(path=path)
    else: 
        await ctx.send(f"{user.mention} you're not in the lobby")
        

@discord_bot.command(name="open_lobby")
async def open_lobby(ctx):
    vote = discord.Embed(title="**[Monopoly]**", description="It's time to join the lobby", color=0x00ff00)
    message = await ctx.send(embed=vote)
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    
    def check_for_reaction(reaction, user):
        return str(reaction.emoji) in ['✅', '❌']
    
    stopped = False
    while not stopped:
        try:
            reaction, user = await discord_bot.wait_for("reaction_add", timeout=60, check=check_for_reaction)

            if str(reaction.emoji) == "✅":
                await lobby_join_helper(ctx, user)
                await message.remove_reaction(reaction, user)
                    
            elif str(reaction.emoji) == "❌":
                await lobby_leave_helper(ctx, user)
                await message.remove_reaction(reaction, user)
            else:
                await message.remove_reaction(reaction, user)
                
        except asyncio.TimeoutError:
            await message.delete()
            break


@discord_bot.command(name="join_lobby")
async def join_lobby(ctx):
    user = ctx.message.author
    await lobby_join_helper(ctx, user)

 
@discord_bot.command(name="leave_lobby")
async def leave_lobby(ctx):
    user = ctx.message.author
    await lobby_leave_helper(ctx, user)


@discord_bot.command(name="lobby")
async def return_player_in_lobby(ctx):
    if len(list_of_players) > 0:
        await ctx.send("The players are:")
        for player in list_of_players:
            await ctx.send(player)
    else:
        await ctx.send("The lobby is empty.")


@discord_bot.command(name="start")#start game
async def start_game(ctx):
    pass

discord_bot.run(TOKEN)