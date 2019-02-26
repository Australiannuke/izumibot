import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the server,enjoy your stay....from Park !')
    print('Sent message to ' + member.name)
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the server,enjoy your stay....from Park !')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'Iz!kill':
        em = discord.Embed(description='')
        em.set_image(url='https://data.whicdn.com/images/41798484/original.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!murder':
        em = discord.Embed(description='')
        em.set_image(url='https://steamuserimages-a.akamaihd.net/ugc/919178087587838801/84DB842956BB8F34761A2B92C8CCB908FE0D8706/')
        await client.send_message(message.channel, embed=em)
        em.set_image(url='https://data.whicdn.com/images/136971350/original.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!displeased':
        em = discord.Embed(description='')
        em.set_image(url='https://pa1.narvii.com/6335/8934e92e8887a7dd1b90e58e5529ae8bc244b417_hq.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!eat':
        em = discord.Embed(description='mmmmmm')
        em.set_image(url='http://s1.desu-usergeneratedcontent.xyz/a/image/1445/12/1445125457801.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!interested':
        em = discord.Embed(description='')
        em.set_image(url='https://data.whicdn.com/images/104959760/original.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!smack':
        em = discord.Embed(description='Ouch !')
        em.set_image(url='https://media.giphy.com/media/bc8zN2blg67oA/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!scared':
        em = discord.Embed(description='')
        em.set_image(url='https://media.giphy.com/media/ALiHt04wgBEPK/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!looking':
        em = discord.Embed(description='')
        em.set_image(url='http://fanaru.com/another/image/245770-another-izumi-akazawa.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!fight':
        em = discord.Embed(description='')
        em.set_image(url='https://i.pinimg.com/originals/c4/84/7b/c4847b0e234b677a51db12a094f12555.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!fire':
        em = discord.Embed(description='')
        em.set_image(url='https://data.whicdn.com/images/237801803/original.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!laughing':
        em = discord.Embed(description='')
        em.set_image(url='https://data.whicdn.com/images/29771935/original.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!arrive':
        em = discord.Embed(description='')
        em.set_image(url='http://24.media.tumblr.com/tumblr_m1ka4scfyc1r01du3o2_r1_250.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!faceplant':
        em = discord.Embed(description='')
        em.set_image(url='https://66.media.tumblr.com/43927802d6ea73d95fca07b1f82bcb31/tumblr_inline_mjvwv1tzOc1qz4rgp.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!stab':
        em = discord.Embed(description='DIE')
        em.set_image(url='https://66.media.tumblr.com/tumblr_m3sbz4Oc861rv23tco1_500.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!dies':
        em = discord.Embed(description='')
        em.set_image(url='https://i.pinimg.com/originals/eb/fd/5c/ebfd5c4b40d16839261c2990e9814070.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Iz!hello':
        await client.send_message(message.channel,'Hello,how are you ')
    if message.content == 'Iz!Bp':
        await client.send_message(message.channel,'Blackpink in Your areaaaaaaa')
    if message.content == 'Iz!cry':
        em = discord.Embed(description='im not crying you are')
        em.set_image(url='https://pa1.narvii.com/5738/6c1d501c242368c8bfa56c29fa1676bda6d7ded4_hq.gif')
        await client.send_message(message.channel, embed=em)
client.run('NTQ3ODIxNTk2ODkxNDE0NTU5.D08WYA.aZpZbO_w3n-X0jyaZvVYIB-xfPU')
