import discord
from discord.ext import commands
import asyncio
import random
import urllib
import urllib.request


client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('r!talk'):
            quotes=[
                "Hmph, it seems you have bad luck. For you to encounter me, Rama!",
                "Will you hinder my path? Then, you are my enemy. Let's go!",
                "Master, what's wrong?",
                "Aah.. Isn't there anything better to do?",
                "Hey hey, don't pat my head. It's rude.",
                "I am the Servant, you are the Master. But I shall not prostrate before you, for that is the way the world works.",
                "I like anything that I enjoy. Dance, music, martial arts, meditation....",
                "Do not treat me like a child! Hey, geez...",
                "Huh? Master! I think something has happened!"]
            quote=random.choice(quotes)
            await client.send_message(message.channel, quote)

    if message.content.startswith('r!hello'):
        await client.send_message(message.channel, "Hello!")

    if message.content.startswith("r!say"):
        if message.author.id == "227446010094288896" or "414626125889667072" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You can't make me do that!")


    if message.content.startswith("r!happy"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/435484833997783053/439044105264168960/unknown-61.png")
        await client.send_message(message.channel, embed = e)

    if message.content.startswith("r!mono"):
        choice=random.randint(1,4)
        if choice==1:
            await client.send_message(message.channel, "You mean the devil herself, right...? Why would you ask for such a thing?!")
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/435494001710333952/439531257538281485/satan.png")
            await client.send_message(message.channel, embed = e)

        elif choice==2:
            await client.send_message(message.channel, "Mono..? She's a crafty piece of work...")
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/435494001710333952/439521636803280896/cunning.png")
            await client.send_message(message.channel, embed = e)

        elif choice==3:
            await client.send_message(message.channel, "I don't think she's around right now. Wanna leave a message?")

        elif choice==4:
            await client.send_message(message.channel, "Um... She's over there.")
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/439040144914251776/439889095246872607/suspicious.png")
            await client.send_message(message.channel, embed = e)

    if message.content.startswith("r!ping"):
            await client.send_message(message.channel, "Pong!")

    if message.content.startswith("r!randomfgo"):
            response = urllib.request.urlopen('http://fategrandorder.wikia.com/wiki/Special:Random')
            await client.send_message(message.channel, response.geturl())

    if message.content.startswith("r!changegame"):
        
        if message.author.id == "227446010094288896" or "414626125889667072" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "A new game...? Very well.")
            await client.change_status(game=discord.Game(name="%s" % (" ".join(args[1:]))))
            
        else:
            await client.send_message(message.channel, "You don't have permission to do that!")
    
    if message.content.startswith("r!help"):
        await client.send_message(message.channel, """
**General Commands**
r!talk - *Random Rama quote*
r!hello - *Say hello!*
r!happy - *Happy Rama!*
r!mono - *Demonize Mono with one simple command!*
r!ping - *Pong! Tests if the bot is online.*
r!randomfgo - *Posts a random page from the F/GO wiki.*
r!kinassign - *Get your fresh F/GO kinnies here!*
r!8ball - *Get Rama's opinion on things.*

**Command Spells**
r!say - *Make Rama say something*
r!changegame - *Change the game Rama is playing*""")

    if message.content.startswith("r!aster"):
        goodbyes=["Goodbye.", "Sayonara.", "Omae wa mou shindeiru.","Hmph, it seems you have bad luck. For you to encounter me, Rama!"]
        choice=random.choice(goodbyes)
        await client.send_message(message.channel, choice)
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/439040144914251776/441237096355856384/get_in_the_locker.png")
        await client.send_message(message.channel, embed = e)

    if message.content.startswith("r!supportgroup"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/418772194999533588/434666888375566346/ASDFADFSFSDA.png")
        await client.send_message(message.channel, embed = e)

    if message.content.startswith("r!8ball"):
        answers=["It is certain.","You may rely on it.","Ask again later.","Reply hazy, try again.","My reply is no.","My sources say no."]
        reply=random.choice(answers)
        await client.send_message(message.channel, reply)

    if message.content.startswith("r!kinassign"):
        lines = open('FGO.txt').read().splitlines()
        kin =random.choice(lines)
        await client.send_message(message.channel, "The kin I assign you is %s !" % kin)
             

@client.event
async def on_ready():
    print("Servant, Saber. Great King of Kosala, Rama. It's alright, leave it all to me!")


client.run("NDM5MDM4NzI2MjMyOTk3ODk4.DcNkcA.3LifXMyrco4ezO7nItJ5cdfTGho")
