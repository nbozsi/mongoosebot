import discord
import youtube_dl
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system
from discord.ext import commands

queuelist = []

TOKEN = 'Njk1NTgwODMxNDk4MTA4OTc5.XoclgQ.zgqOsqxYqNfkI_tpF334npjMmJ8'
client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("another one"))
    print("Hi Mr.Torok!")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ilyen niiiincs!")
@client.command(brief="Check yo ping!")
async def ping(ctx):
    await ctx.send(f" Megpingeltél, a pingem: {round(client.latency * 1000)}ms")
@client.command()
async def hajrabernatom(ctx):
    await ctx.send("433!")
@client.command(pass_context=True)
async def gyerebe(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Okéj, de valamiért nem megy...")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"Igenis mesterem! Csaztalkoztam a következőhöz: '{channel}' ")
@client.command(pass_context=True)
async def menjinnen(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("Lecsatlakoztam...")
    else:
        await ctx.send("Miről csatlakozzak le bazdmeg?!")
@client.command(pass_context=True)
async def muzsikat(ctx, url: str):
    #queue? make a list!
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except Exception:
        await ctx.send("Valamit elbasztál, de csúnyán!")
        return
    await ctx.send("Most játszott: " + url)
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()



client.run(TOKEN)
