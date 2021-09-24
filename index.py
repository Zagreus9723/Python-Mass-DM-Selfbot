import discord
import datetime
from discord.ext import commands
import asyncio
import time
import json

client = commands.Bot(command_prefix = '++')
client.remove_command('help')
configj = open('config.json', 'r')
config = json.load(configj)
token = config['token']
messagesend = config['message']
users = []

@client.event
async def on_voice_state_update(member):
    if member in users:
        print('Already DMed')
    else:
        try:
            await member.send(messagesend)
            users.append(member)
            print('Said message')
        except:
            print("Couldn't DM this user")

@client.event
async def on_member_update(before, after):
    if after.name in users:
        print('Already DMed')
    else:
        try:
            await after.name.send(messagesend)
            users.append(after.name)
            print('Said message')
        except:
            print("Couldn't DM this user")

@client.event
async def on_message(message):
    if message.author in users:
        print('Already DMed')
    else:
        try:
            await message.author.send(messagesend)
            users.append(message.author)
            print('Said message')
        except:
            print("Couldn't DM this user")

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author in users:
        print('Already DMed')
    else:
        try:
            await reaction.message.author.send(messagesend)
            users.append(reaction.message.author)
            print('Said message')
        except:
            print("Couldn't DM this user")

client.run(token, bot=False)
