#!/usr/bin/python3
# bot.py
import random
import discord
from discord.ext import commands,tasks

TOKEN = 'NzA2MjMxMDIyODUyNzY3NzQ2.XrNRAw.AlrQO1wf7y12E25X9TXFL42Ottw'

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, hows it going, and welcome to HELL!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    messageContent =  str(message.content).lower()
    #print(messageContent)
    
    if messageContent == '!help':
        response = """
!help = Pulls up all commands and what they do (Duh)
!interesting = Something pretty interesting (Random!)
Bullshit = Your not wrong
Swearing = ITS AGAINST THE LAW
"""
        await message.channel.send(response)
    
    if 'bullshit' in messageContent:
        response = "Yep, thats bullshit"
        await message.channel.send(response)
    
    interestingFacts = [
        "North Korea and Cuba are the only places you can't buy Coca-Cola.",
        "The entire world's population could fit inside Los Angeles.",
        'There are more twins now than ever before.',
        'The hottest chili pepper in the world is so hot it could kill you.',
        "More people visit France than any other country.",
        "The world's most densely populated island is the size of two soccer fields.",
        "The Canary Islands are named after dogs, not birds.",
        "Indonesia is home to some of the shortest people in the world.",
        "The Paris Agreement on climate change was signed by the largest number of countries ever in one day.",
        "The world's quietest room is located at Microsoft's headquarters in Washington state.",
        "There are only three countries in the world that don't use the metric system.",
        "The longest place name on the planet is 85 letters long.",
        "Four babies are born every second.",
        "The coldest temperature ever recorded was -144 degrees Fahrenheit.",
        "The Earth's ozone layer will make a full recovery in 50 years."
    ]


    if message.content == '!interesting':
        response = random.choice(interestingFacts)
        await message.channel.send(response)
       
    badNaughty = ['fuck','arse','ass','bastard','bitch','fucker','cunt','damn','hell','frigger','twat','prick','piss','penis','vagina','tits']

    if any(bad_word in message.content.strip().lower().split() for bad_word in badNaughty):
        await message.channel.send(f"{message.author.mention}, Stop! You have violated the Law! Pay the court a fine or serve your sentence. Your stolen goods are now forfeit. https://cdn.discordapp.com/attachments/707746845501161523/708115869179576431/unknown.png")     

bot.run(TOKEN)