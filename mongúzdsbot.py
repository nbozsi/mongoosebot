import discord
import youtube_dl
from discord.utils import get
from discord.ext import commands
import random
import os
client= commands.Bot(command_prefix = '?')
TOKEN='Njk1NTgwODMxNDk4MTA4OTc5.XoclgQ.zgqOsqxYqNfkI_tpF334npjMmJ8'

players = {}

@client.event
async def on_ready():
    print('Bejelentkezve {0.user} néven!'.format(client))
    print('Hali Simon')
    print('|---------------------------|')
    print()
@client.event
async def on_message(msg):
     c=msg.author.id
     if c==695717308286500885:
         a=random.randint(0,3)
         tomb=['Kussolj Danika','Dani kaki','senkit nem érdekel Danika']
         channel=msg.channel
         if a==3:
            await msg.delete()
         else:
             await channel.send(tomb[a])
    await bot.process_commands(message)

@client.command(pass_context=True)
async def mitigyak(ctx):
    """Segít eldönteni mit igyál."""
    italok=[":wine_glass:Bort:wine_glass:",":sake:Pálinkát:sake:",":beer:Sört:beers:",":heart_eyes:Kevertet:heart_eyes:",":man_gesturing_no:Vodkát ne:man_gesturing_no:",":deer:Jégert:deer:",":sake:Tátrateát:sake:",":champagne:Pezsgőt:champagne_glass:",":whisky:Whiskyt:whisky:"]
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
        await ctx.send(f"Már fent vagyok bazdmeg")
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
        await ctx.send(f"Le vagyok csatlakozva he")

@client.command(pass_context=True)
async def alljameg(ctx):
    """megállítom a zenét"""
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
        await ctx.send(f'Nem vagyok csatlakozva he')

client.run(TOKEN)
