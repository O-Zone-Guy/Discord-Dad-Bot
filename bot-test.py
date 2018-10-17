import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # await client.send_message(client.get_channel(501942173974134786), "I am back!")
    print ()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await client.send_message(message.channel, 'Hello! {0.author.mention}'.format(message))
        print('sending message...')

    if message.content.startswith("!logout"):
        print('logging out...')
        await client.logout()

client.run('NTAxOTQwMzgyMDU4MjgzMDE4.Dqgs3g._5fQc16mzPawl6aWPBVLeBgAQ1o')
