import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random


Client = discord.Client()
client = commands.Bot(command_prefix = "zack")

urls = [
"https://i.imgur.com/azqErnB.png",
"https://i.imgur.com/4n1Wb8g.jpg",
"https://imgur.com/55KLTpg.jpg",
"https://i.imgur.com/5g3eV50.jpg",
"https://i.imgur.com/w3eQycZ.png",
"https://i.imgur.com/QZjtRVC.png",

]
@client.event
async def on_ready():
    print ("Ready")

@client.event
async def on_message(dog):
    if dog.content.startswith("zack_dog"):
        url = random.choice(urls)
        await client.send_message(dog.channel,("<@discordUserIDgoeshere> is this a dog?",url,))
        
        
client.run("Your token goes here")
