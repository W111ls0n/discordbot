import discord
client = discord.Client
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
         await message.channel.send('pong')

@client.event
async def on_message(message):
    if message.content.startswith('?thumb')
    channel = message.channel
    await channel.send('send me that 👍 reaction pls!')

    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == '👍'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout= 60.0, check=check)
    except asyncio.TimeoutError:
        await channel.send('👎')
    else:
        await channel.send('👍')

@client.event
async def on_message(message):
    if message.content.startswith('?live')
    channel = message.channel
    await channel.send('@everyone come watch me live now at https://www.twitch.tv/talleyho1')

@client.event
async def on_message(message):
    if message.content.startswith('?commands')
    channel = message.channel
    await channel.send('COMMANDS \n ?thumb, for attendance or something \n ?live, for talleyho1s twitch \n ?emojis, shows the servers emojis \n ?help, shows the commands command \n poke, poke')

@client.event
async def on_message(message):
    if message.content.startswith('?emojis')
    channel = message.channel
    await channel.send(List[emojis])

@client.event
async def on_message(message):
    if message.content.startswith('?help')
    channel = message.channel
    await channel.send('type ?commands for a list of commands')

@client.event
async def on_message(message):
    if message.content.startswith('pong')
    channel = message.channel
    await channel.send('ping')

@client.event
async def on_message(message):
    if message.content.startswith('whats ur favorite game')
    channel = message.channel
    await message.send('idk ask master white')

@client.event
async def on_message(message):
    if message.content.startswith('poke')
    channel = message.channel
    await message.send('poke')

@client.event
async def on_message(message):
    if message.content.startswith('humpty dumpty') 
    channel = message.channel
    await message.send('sat on a wall')

@client.event
async def on_message(message):
    if message.content.startswith('?info')
    channel = message.channel
    await message.channel






@client.run('insert bot key here')
