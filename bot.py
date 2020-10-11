# bot.py
import os
from random import random, choice
from discord.ext import commands
import gif_gen
import discord

TOKEN = os.environ['DISCORD_TOKEN']
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.event
# async def on_message(message):
#     # do some extra stuff here
#     print(message.content)
#     if message.webhookID:
#         print("webhook")


@bot.command(name='gif', help='!gif [statement] - Responds with a gif')
async def show_gif(ctx, *, query: str):
    gif = gif_gen.get_gif(query)
    await ctx.send(gif)


@bot.command(name='tasks', help='Doing tasks mute everyone.')
async def vcmute(ctx):
    voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    print(voice_channel)
    for member in voice_channel.members:
        print(member)
        await member.add_roles(role)
    await ctx.send('Muted everyone: GO DO YOUR TASKS')


@bot.command(name='discuss', help='Discuss: un-mute everyone')
async def vcmute(ctx):
    voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    print(voice_channel)
    for member in voice_channel.members:
        print(member)
        await member.remove_roles(role)
    await ctx.send('Unmuted everyone: WHO IS IMPOSTER')


@bot.command(name='flip', help='-Flip a coin.')
async def roll(ctx):
    sides = ["Heads", "Tails"]
    result = choice(sides)
    await ctx.send(result)


@bot.command(name='jaccuse', help='Accuse a random player of being sus!')
async def randsus(ctx):
    players = []
    voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
    print(voice_channel.members)  # each user is a member object
    for member in voice_channel.members:
        print(member.name)
        players.append(member.name)
    random_sus = choice(players)
    messages = [
        f'{random_sus} is acting vary suspicious',
        f'I think I saw {random_sus} coming out of a vent',
        f'{random_sus} definitely killed that guy',
        f'{random_sus} was faking tasks',
        f'{random_sus} was following me around',
        f'{random_sus} is acting very suspicious',
        f'I saw {random_sus} holding a knife',
        f'{random_sus} is acting vary suspicious',
        f'{random_sus} sure was taking a long time in the bathroom',
        f'{random_sus} stole my yogurt in the fridge that had my name written on it!',
        f'{random_sus} microwaves tuna fish in the common room!',
        f'{random_sus} smelt it, so they probably dealt it',
    ]
    random_message = choice(messages)
    await ctx.send(random_message)


@bot.command(name='dead', help="I am dead, move me to talk to other deceased")
async def killme(ctx):
    author = ctx.message.author
    voice_channel = discord.utils.get(ctx.message.guild.channels, name="Graveyard", type=discord.ChannelType.voice)
    await author.move_to(voice_channel)
    await ctx.send(f'{author.name} joined the graveyard')


@bot.command(name='kill', help="!kill [player name] -Move player the graveyard")
async def killyou(ctx, player_name: str):
    alive_voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
    dead_voice_channel = discord.utils.get(ctx.message.guild.channels, name="Graveyard", type=discord.ChannelType.voice)
    for member in alive_voice_channel.members:
        print(member.name)
        if member.name == player_name:
            await member.move_to(dead_voice_channel)
    await ctx.send(f'{member.name} joined the graveyard')


@bot.command(name='revive', help="!revive [player name] or self -Mistakenly kill, resuscitate")
async def revive_me(ctx, player_name: str = None):
    alive_voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
    dead_voice_channel = discord.utils.get(ctx.message.guild.channels, name="Graveyard", type=discord.ChannelType.voice)
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if player_name is not None:
        for member in dead_voice_channel.members:
            print(member.name)
            if member.name == player_name:
                await member.remove_roles(role)
                await member.move_to(alive_voice_channel)
                await ctx.send(f'{member.name} was resurrected')
    else:
        author = ctx.message.author
        await author.remove_roles(role)
        await author.move_to(alive_voice_channel)
        await ctx.send(f'{author.name} was resurrected')


@bot.command(name='thriller', help="Revive all players")
async def revive_all(ctx, player_name: str = None):
    alive_voice_channel = discord.utils.get(ctx.message.guild.channels, name="General", type=discord.ChannelType.voice)
    dead_voice_channel = discord.utils.get(ctx.message.guild.channels, name="Graveyard", type=discord.ChannelType.voice)
    for member in dead_voice_channel.members:
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.remove_roles(role)
        await member.move_to(alive_voice_channel)
    await ctx.send(f'All players brought back from the dead, hallelujah!')

bot.run(TOKEN)
