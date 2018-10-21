import discord
import sql_handler
import random
import time
import datetime

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

    if message.content.startswith('!say joke'):
        joke = sql_handler.get_random_joke()
        await client.send_message(message.channel, joke[0])
        time.sleep(5)
        await client.send_message(message.channel, joke[1])
        await client.send_message(message.channel, "By: -" + joke[2])
        log_actions("Said joke, ID: " + str(joke[3]))
        pass

    if message.content.startswith("!logout") and message.author.name == "OzoneGuy":
        print('logging out...')
        await client.logout()


client.run('NTAxOTQwMzgyMDU4MjgzMDE4.Dqgs3g._5fQc16mzPawl6aWPBVLeBgAQ1o')
