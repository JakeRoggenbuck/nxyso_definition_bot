import discord
import shlex
import json
import difflib

token = open("token.txt", "r").read()

client = discord.Client()

with open("data.json") as json_data:
    data = json.load(json_data)

keys = [a for a in data.keys()]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot == False:
        command_split = shlex.split(message.content)
        if command_split[0] == "/search" or command_split[0] == "/s":
            words = difflib.get_close_matches(command_split[1], keys)
            embed=discord.Embed(title=f"Closest definitions for {command_split[1]}", color=0x4100b2)
            for word in words:
                embed.add_field(name=word, value=data[word], inline=True)
            await message.channel.send(embed=embed)

client.run(token)
