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
client = commands.Bot(command_prefix = '.')
queue=[]
a=1
b=1
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("At your service!"))
    print(" /$$   /$$ /$$       /$$      /$$                 /$$$$$$$$ /$ /$               /$ /$   /$$      ")
    print("| $$  | $$|__/      | $$$    /$$$                |__  $$__/|_/|_/              |_/|_/  | $$      ")
    print("| $$  | $$ /$$      | $$$$  /$$$$  /$$$$$$          | $$   /$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$")
    print("| $$$$$$$$| $$      | $$ $$/$$ $$ /$$__  $$         | $$  /$$__  $$ /$$__  $$ /$$__  $$| $$  /$$/")
    print("| $$__  $$| $$      | $$  $$$| $$| $$  \__/         | $$ | $$  \ $$| $$  \__/| $$  \ $$| $$$$$$/ ")
    print("| $$  | $$| $$      | $$\  $ | $$| $$               | $$ | $$  | $$| $$      | $$  | $$| $$_  $$ ")
    print("| $$  | $$| $$      | $$ \/  | $$| $$ /$$           | $$ |  $$$$$$/| $$      |  $$$$$$/| $$ \  $$")
    print("|__/  |__/|__/      |__/     |__/|__/|__/           |__/  \______/ |__/       \______/ |__/  \__/")
    print()
def sor(a):
    os.remove(queue[0]+".mp3")
    queue.pop(0)
    print(queue)
    print("Elindítottam a kövi számot")
    if len(queue)>0:
        y=queue[0]+'.mp3'
        voice.play(discord.FFmpegPCMAudio(y), after=sor)
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
    """mutatom a pingem"""
    await ctx.send(f" A pingem: {round(client.latency * 1000)}ms")
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
    global voice
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
    global queue
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        if not url:
            await ctx.send("Nem írtál semmit he")
        else:
            if "&" in url:
                url=url.split('&')[0]
            if "youtu.be" in url:
                url="https://www.youtube.com/watch?v="+url[-11:]
            queue.append(url[-11:])
            print(queue)
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
            a=url[-11:]+".mp3"
            for file in os.listdir("./"):
                if file.endswith(a):
                    os.rename(file, file[-15:])
        if voice.is_playing():
            await ctx.send("Hozzáadtam a lejátszási sorhoz.")
        else:
            await ctx.send("Most játszott: " + url)
            voice.play(discord.FFmpegPCMAudio(a), after=sor)
            voice.source=discord.PCMVolumeTransformer(vc.source)
            voice.source.volume = 0.1

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
async def tekerdat(ctx):
    """kinyomom a számot"""
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        voice.stop()
        if os.path.exists("song.mp3"):
            await os.remove("song.mp3")
    else:
        await ctx.send(f'Nem vagyok csatlakozva he')

client.run(TOKEN)
