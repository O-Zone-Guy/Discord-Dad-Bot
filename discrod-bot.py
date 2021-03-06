import discord
import sql_handler
import random
import time
import datetime
import config

client = discord.Client()


def contains_im(text):
    if 'I am' in text:
        word = text.split("I am", 1)[1].split(" ")[1]
        return [True, word]

    if "I'm" in text:
        word = text.split("I'm", 1)[1].split(" ")[1]
        return [True, word]

    if "Im" in text:
        word = text.split("Im", 1)[1].split(" ")[1]
        return [True, word]

    if "im" in text:
        word = text.split("im", 1)[1].split(" ")[1]
        return [True, word]
    return [False, '']


def log_actions(text):
    f = open("log.txt", 'a')
    f.write(str(datetime.datetime.now()) + ": " + text + "\n")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.send_message(client.get_channel('501942173974134786'), "I am Back!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if contains_im(message.content)[0] and random.random() < 0.2:
        await client.send_message(message.channel, 'Hello ' + contains_im(message.content)[1] +
                                  ". I'm Dad Bot! {0.author.mention}".format(message))
        pass

    # uses database generated by reddit bot to retrieve joke and then says said joke
    # sends the joke in three lines
    # first the header/post title
    # second is the body/ actual joke
    # third is the author
    if message.content.startswith('!say joke'):
        joke = sql_handler.get_random_joke()
        await client.send_message(message.channel, joke[0])
        time.sleep(5)
        await client.send_message(message.channel, joke[1] if joke[1] is not None else '')
        await client.send_message(message.channel, "By: -" + joke[2])
        log_actions("Said joke, ID: " + str(joke[3]))
        pass

    if message.content.startswith('!get roles'):
        for role in message.server.roles:
            print(role.name)
    # gives admin tag to message author
    if message.content.startswith('!tag admin'):
        await client.add_roles(message.author, discord.utils.get(message.server.roles, name='Admin'))

    if message.content.startswith("!logout") and message.author.name == "OzoneGuy":
        print('logging out...')
        await client.logout()


client.run(config.discord_code)
