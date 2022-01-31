import discord, datetime, asyncio, time, json
from discord.ext import commands
from rich import console, print

client = commands.Bot(command_prefix = '++', self_bot=True)
client.remove_command('help')
configj = open('config.json', 'r')
config = json.load(configj)
token = config['token']
messagesend = config['message']
users = []

@client.event
async def on_voice_state_update(member):
    if member.id in users:
        console.log(f'Already DMed {member.name}#{member.discriminator}.')
    else:
        try:
            await member.send(messagesend)
            users.append(member.id)
            console.log(f'[green]DMed {member.name}#{member.discriminator}.[/green]')
        except:
            console.log(f'[red]Couldn\'t DM {member.name}#{member.discriminator}.]/red]')

@client.event
async def on_member_update(before, after):
    if after.id in users:
        console.log(f'Already DMed {after.name}#{after.discriminator}.')
    else:
        try:
            await after.name.send(messagesend)
            users.append(after.id)
            console.log(f'[green]DMed {after.name}#{after.discriminator}.[/green]')
        except:
            console.log(f'[red]Couldn\'t DM {after.name}#{after.discriminator}.[/red]')

@client.event
async def on_message(message):
    if message.author.id in users:
        console.log(f'Already DMed {message.author.name}#{message.author.discriminator}.')
    else:
        try:
            await message.author.send(messagesend)
            users.append(message.author.id)
            console.log(f'[green]DMed {message.author.name}#{message.author.discriminator}.[/green]')
        except:
            console.log(f'[red]Couldn\'t DM {message.author.name}#{message.author.discriminator}.[/red]')

@client.event
async def on_raw_reaction_add(payload):
    member = payload.member
    if member.id in users:
        console.log(f'Already DMed {member.name}#{member.discriminator}.')
    else:
        try:
            await member.send(messagesend)
            users.append(member.id)
            console.log(f'[green]DMed {member.name}#{member.discriminator}.[/green]')
        except:
            console.log(f'[red]Couldn\'t DM {member.name}#{member.discriminator}.[/red]')

client.run(token, bot=False)
