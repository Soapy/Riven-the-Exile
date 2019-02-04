import random
import time
import discord
from discord.ext.commands import Bot
from bs4 import BeautifulSoup
import SecretToken

token = SecretToken.get_token()
client = Bot(description='description', command_prefix='r!')
client.remove_command("help")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("Discord.py API version:", discord.__version__)


@client.command(pass_context=True)
async def ping(ctx):
    pingtime = time.time()
    pingms = await client.say("This is why I spend so much time sheath shopping.\nPinging...")
    ping = (time.time() - pingtime) * 1000
    await client.edit_message(pingms, "Pong! It took `%dms`" % ping)


@client.command(pass_context=True)
async def map(ctx):
    author = ctx.message.author.name
    maps = [1, 10, 11, 12]
    map_id = random.choice(maps)
    embed = discord.Embed(title=f"Who needs a map? {author} does.",
                          color=0x099706)
    embed.set_image(url=f"http://ddragon.leagueoflegends.com/cdn/6.8.1/img/map/map{map_id}.png")
    await client.say(embed=embed)


@client.command(pass_context=True, aliases=['say'])
async def echo(ctx, *msg):
    say = ' '.join(msg)
    await client.delete_message(ctx.message)
    return await client.say(say)


'''
commands todo: insult, randomability, randomchampion, champion, championability, championstats 
'''


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Commands:",
                          description=
                          "r!ping: Pings the bot.\n"
                          "r!insult: A random champion will taunt you back.\n"
                          "r!random: Prints a random command.\n"
                          "r!insult: Insults you back.\n"
                          "r!randomability: Prints a randomn ability\n"
                          "randomchampion:\n"
                          "champion:\n"
                          "championability:\n"
                          "championstats:\n"
                          "There's hidden commands too~~\n")
    await client.say(embed=embed)


client.run(token)
