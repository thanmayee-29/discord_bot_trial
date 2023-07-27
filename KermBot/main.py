import discord
from discord.ext import commands
# from pip._vendor
import requests
import json

# imports apikeys/tokens
from apitok import *

# prefix
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("the bot is ready to be used :D")
    print("::::::::::::::::::::::::::::::::")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, Iam Kermit the bot aka KermBot")


@client.event
async def on_member_join(member):

    jk = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        "X-RapidAPI-Key": jokeapikey,
        "X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }
    response = requests.request("GET", jk, headers=headers)
    channel = client.get_channel(1077277537899663423)
    await channel.send("LOL heyyyyy")
    await channel.send(json.loads(response.text)['content'])


'''@client.event    
async def on_member_join(member):
    channel = client.get_channel(1077277537899663423)
    await channel.send(member, "left the server T_T")'''

client.run(token)
