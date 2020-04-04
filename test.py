import discord
import youtube_dl
from discord.utils import get
from discord.ext import commands
import random
client= commands.Bot(command_prefix = '?')
TOKEN='Njk1NTgwODMxNDk4MTA4OTc5.XoclgQ.zgqOsqxYqNfkI_tpF334npjMmJ8'

players = {}

@client.event
async def on_ready():
    print('Bejelentkezve {0.user} néven!'.format(client))
    print('Hi Mr. Török!')
    print('|---------------------------|')
    print()

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

class VoiceState:
    def init(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        # self.skip_votes = set()
        # # a set of user_ids that voted
        # self.audio_player = self.bot.loop.create_task(self.audio_player_task())

def is_playing(self):
    if self.voice is None or self.current is None:
        return False

    player = self.current.player
    return not player.is_done()

@property
def player(self):
    return self.current.player

def skip(self):
    self.skip_votes.clear()
    if self.is_playing():
        self.player.stop()

def toggle_next(self):
    self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

async def audio_player_task(self):
    while True:
        self.play_next_song.clear()
        self.current = await self.songs.get()
        await self.bot.send_message(self.current.channel, 'Now playing' + str(self.current))
        self.current.player.start()
        await self.play_next_song.wait()

@client.command(pass_context=True, no_pm=True)
async def muzsikat(self, ctx, *, song:str):
      """Lejátszik egy zenét.
      """
      state = self.get_voice_state(ctx.message.guild)
      print (' state ')
        opts = {
          'default_search': 'auto',
          'quiet': True,
      }

      if state.voice is None:
          success = await ctx.invoke(self.summon)
          await self.bot.say("Loading the song please be patient..")
          if not success:
              return

      try:
          player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
      except Exception as e:
          fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
          await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
      else:
          player.volume = 0.6
          entry = VoiceEntry(ctx.message, player)
          await self.bot.say('Enqueued ' + str(entry))
          await state.songs.put(entry)

@commands.command(pass_context=True, no_pm=True)
async def playing(self, ctx):
    """Kiírja a éppen játszott számokat."""

    state = self.get_voice_state(ctx.message.server)
    if state.current is None:
        await self.bot.say('Not playing anything.')
    else:
        skip_count = len(state.skip_votes)
        await self.bot.say('Now playing {} [skips: {}/3]'.format(state.current, skip_count))

client.run(TOKEN)
