import discord
import youtube_dl
import os
import random
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
@client.event
async def on_message(message):
    c=message.author.id
    if c==695717308286500885:
        a=random.randint(0,3)
        tomb=["Kussolj Danika","Dani kaki","senkit nem érdekel Danika"]
        channel=message.channel
        if a==3:
            await msg.delete()
        else:
            await channel.send(tomb[a])
    await client.process_commands(message)
@client.command()
async def ping(ctx):
    """mutatom a pinged"""
    await ctx.send(f" A pinged: {round(client.latency * 1000)}ms")
@client.command(pass_context=True)
async def mitigyak(ctx):
    """Segít eldönteni mit igyál."""
    italok=[":wine_glass:Bort:wine_glass:",":sake:Pálinkát:sake:",":beer:Sört:beers:",":heart_eyes:Kevertet:heart_eyes:",":man_gesturing_no:Vodkát ne:man_gesturing_no:",":deer:Jégert:deer:",":sake:Tátrateát:sake:",":champagne:Pezsgőt:champagne_glass:",":whisky:Whiskyt:whisky:"]
    await ctx.send(random.choice(italok))
@client.command()
async def hajrabernatom(ctx):
    """megmutatja, hogy egy 10-es skálán mennyire szar a 25-ik"""
    await ctx.send("433!")
@client.command(pass_context=True)
async def gyerebe(ctx):
    """feljövök a hangra"""
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
    await ctx.send(f"Csatlakoztam a következőhöz: '{channel}' ")
@client.command(pass_context=True)
async def menjinnen(ctx):
    """lemegyek a hangról"""
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)


    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("Lecsatlakoztam...")
        if os.path.exists("song.mp3"):
            await os.remove("song.mp3")
    else:
        await ctx.send("Miről csatlakozzak le bazdmeg?!")
@client.command(pass_context=True)
async def muzsikat(ctx, url: str):
    """lejátszok valami szép zenét"""
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
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print('done',e))
    voice.volume = 100

@client.command(pass_context=True)
async def alljameg(ctx):
    """megállítom a zenét"""
    print('blablabla')
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        if voice and voice.is_playing():
            voice.pause()
        else:
            await ctx.send(f"Mit állitsak meg bazmeg")
    else:
        await ctx.send(f'Nem vagyok csatlakozva he')
@client.command(pass_context=True)
async def mehet(ctx):
    """folytatom a zenét"""
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        if voice and voice.is_playing():
            await ctx.send("Ne legyél gizda")
        else:
            voice.resume()
    else:
        await ctx.send('Nem vagyok csatlakozva he')

@client.command(pass_context=True)
async def vege(ctx):
    """kinyomom a számot"""
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        voice.stop()
        if os.path.exists("song.mp3"):
            os.remove("song.mp3")
    else:
        await ctx.send(f'Nem vagyok csatlakozva he')

client.run(TOKEN)
