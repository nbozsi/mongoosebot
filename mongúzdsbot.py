import discord
from discord.utils import get
from discord.ext import commands
import random
import os
client= commands.Bot(command_prefix = '?')
TOKEN='Njk1NTgwODMxNDk4MTA4OTc5.XoclgQ.zgqOsqxYqNfkI_tpF334npjMmJ8'
@client.event
async def on_ready():
    print('Bejelentkezve {0.user} néven!'.format(client))
    print('Hali Simon')
    print('|---------------------------|')
    print()
@client.command(pass_context=True)
async def mitigyak(ctx):
    """Segít eldönteni mit igyál."""
    italok=[":wine_glass:Bort:wine_glass:",":sake:Pálinkát:sake:",":beer:Sört:beers:",":heart_eyes:Kevertet:heart_eyes:",":man_gesturing_no:Lackó kannásborát ne!:man_gesturing_no:",":deer:Jégert:deer:",":sake:Tátrateát:sake:",":champagne:Pezsgőt:champagne_glass:",":whisky:Whiskyt:whisky:"]
    await ctx.send(random.choice(italok))
@client.command(pass_context=True)
async def gyerebe(ctx):
    """feljövök a hangra"""
    global voice
    cc=ctx.message.author.voice
    if cc==None:
        channel=get(ctx.message.guild.channels, id=695576958133600269)
    else:
        channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.send("Már fent vagyok bazdmeg")
    else:
        voice = await channel.connect()
        await ctx.send(f"Csatlakoztam a(z) {channel}-hoz")
        print(f"Csatlakozva a(z) {channel}-ra")
@client.command(pass_context=True)
async def menjinnen(ctx):
    """lemegyek a hangról"""
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Lecsatlakoztam")
        print(f"Lecsatlakozva")
    else:
        ("Le vagyok csatlakozva he")
@client.command(pass_context=True)
async def kinalat(ctx):
    tomb=os.listdir()
    for i in range (0,len(tomb)):
        if tomb[i][-4:]=='.mp3':
            await ctx.send(tomb[i][:-4])
    print('Átnéztem a fájlokat.')
@client.command(pass_context=True)
async def muzsikat(ctx, *a):
    """lejátszok valami szép zenét"""
    if voice and voice.is_connected():
        if not a:
            await ctx.send("Nem írtál semmit he")
        else:
            if voice.is_playing():
                voice.pause()
                voice.stop()
            a=''.join(a)
            a=a.lower()
            tomb=os.listdir()
            szamok=[]
            for i in range (0,len(tomb)):
                if tomb[i][-4:]=='.mp3':
                    szamok.append(tomb[i][:-4])
            if len(szamok)==0:
                await ctx.send('Nincs semmi zeném he')
            if a=='bármit':
                a=random.choice(szamok)
            if a in szamok:
                b=a+'.mp3'
                voice.play(discord.FFmpegPCMAudio(b), after=lambda e: print('done',e))
            else:
                await ctx.send('Ilyen niiincs')
    else:
        await ctx.send('Nem vagyok csatlakozva he')
@client.command(pass_context=True)
async def alljameg(ctx):
    """megállítom a zenét"""
    if voice and voice.is_connected():
        if voice and voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Mit állitsak meg bazmeg")
    else:
        await ctx.send('Nem vagyok csatlakozva he')
@client.command(pass_context=True)
async def mehet(ctx):
    """folytatom a zenét"""
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
    if voice and voice.is_connected():
        voice.stop()
    else:
        await ctx.send('Nem vagyok csatlakozva he')
client.run(TOKEN)

