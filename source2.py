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
        choice=random.randint(1,2)
        if choice==1:
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/418772194999533588/434666888375566346/ASDFADFSFSDA.png")
            await client.send_message(message.channel, embed = e)
        elif choice==2:
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/441190970403323914/441574611713523712/birds_stacked_on_each_other.jpg")
            await client.send_message(message.channel, embed = e)

    if message.content.startswith("r!8ball"):
        answers=["It is certain.","You may rely on it.","Ask again later.","Reply hazy, try again.","My reply is no.","My sources say no."]
        reply=random.choice(answers)
        await client.send_message(message.channel, reply)

    if message.content.startswith("r!kinassign"):
        kinlist=['http://fategrandorder.wikia.com/wiki/Mashu_Kyrielight\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius\n', 'http://fategrandorder.wikia.com/wiki/Siegfried\n', 'http://fategrandorder.wikia.com/wiki/Gaius_Julius_Caesar\n', 'http://fategrandorder.wikia.com/wiki/Attila\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais_(Saber)\n', "http://fategrandorder.wikia.com/wiki/Chevalier_d'Eon\n", 'http://fategrandorder.wikia.com/wiki/Okita_Souji\n', 'http://fategrandorder.wikia.com/wiki/Fergus_mac_Róich\n', 'http://fategrandorder.wikia.com/wiki/Lancelot_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/Gawain\n', 'http://fategrandorder.wikia.com/wiki/Bedivere\n', 'http://fategrandorder.wikia.com/wiki/Arthur_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Frankenstein_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh\n', 'http://fategrandorder.wikia.com/wiki/Robin_Hood\n', 'http://fategrandorder.wikia.com/wiki/Solomon\n', 'http://fategrandorder.wikia.com/wiki/Atalanta\n', 'http://fategrandorder.wikia.com/wiki/Euryale\n', 'http://fategrandorder.wikia.com/wiki/Arash\n', 'http://fategrandorder.wikia.com/wiki/Orion\n', 'http://fategrandorder.wikia.com/wiki/David\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga\n', 'http://fategrandorder.wikia.com/wiki/Nikola_Tesla\n', 'http://fategrandorder.wikia.com/wiki/Arjuna\n', 'http://fategrandorder.wikia.com/wiki/Kid_Gil\n', 'http://fategrandorder.wikia.com/wiki/Billy_The_Kid\n', 'http://fategrandorder.wikia.com/wiki/Tristan\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)\n', 'http://fategrandorder.wikia.com/wiki/Ishtar\n', 'http://fategrandorder.wikia.com/wiki/James_Moriarty\n', 'http://fategrandorder.wikia.com/wiki/Chiron\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Prototype)\n', 'http://fategrandorder.wikia.com/wiki/Hector\n', 'http://fategrandorder.wikia.com/wiki/Scáthach\n', 'http://fategrandorder.wikia.com/wiki/Diarmuid_Ua_Duibhne\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Karna\n', 'http://fategrandorder.wikia.com/wiki/Fionn_mac_Cumhaill\n', 'http://fategrandorder.wikia.com/wiki/Brynhildr\n', 'http://fategrandorder.wikia.com/wiki/Li_Shuwen_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime_(Lancer)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)_(Santa_Lily)\n", 'http://fategrandorder.wikia.com/wiki/Enkidu\n', 'http://fategrandorder.wikia.com/wiki/Jaguar_Man\n', 'http://fategrandorder.wikia.com/wiki/Medusa\n', 'http://fategrandorder.wikia.com/wiki/Georgios\n', 'http://fategrandorder.wikia.com/wiki/Edward_Teach\n', 'http://fategrandorder.wikia.com/wiki/Boudica\n', 'http://fategrandorder.wikia.com/wiki/Ushiwakamaru\n', 'http://fategrandorder.wikia.com/wiki/Alexander\n', 'http://fategrandorder.wikia.com/wiki/Marie_Antoinette\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha\n', 'http://fategrandorder.wikia.com/wiki/Francis_Drake\n', 'http://fategrandorder.wikia.com/wiki/Anne_Bonny_&_Mary_Read\n', 'http://fategrandorder.wikia.com/wiki/Ozymandias\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Santa_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Astolfo\n', 'http://fategrandorder.wikia.com/wiki/Medb\n', 'http://fategrandorder.wikia.com/wiki/Iskandar\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki_(Rider)\n', 'http://fategrandorder.wikia.com/wiki/Achilles\n', 'http://fategrandorder.wikia.com/wiki/Medea\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais\n', 'http://fategrandorder.wikia.com/wiki/Hans_Christian_Andersen\n', 'http://fategrandorder.wikia.com/wiki/William_Shakespeare\n', 'http://fategrandorder.wikia.com/wiki/Mephistopheles\n', 'http://fategrandorder.wikia.com/wiki/Wolfgang_Amadeus_Mozart\n', 'http://fategrandorder.wikia.com/wiki/Zhuge_Liang_(Lord_El-Melloi_II)\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory_(Halloween)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae\n', 'http://fategrandorder.wikia.com/wiki/Medea_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nursery_Rhyme\n', 'http://fategrandorder.wikia.com/wiki/Paracelcus_Von_Hohenheim\n', 'http://fategrandorder.wikia.com/wiki/Charles_Babbage\n', 'http://fategrandorder.wikia.com/wiki/Helena_Blavatsky\n', 'http://fategrandorder.wikia.com/wiki/Thomas_Edison\n', 'http://fategrandorder.wikia.com/wiki/Geronimo\n', 'http://fategrandorder.wikia.com/wiki/Irisviel_(Dress_of_Heaven)\n', 'http://fategrandorder.wikia.com/wiki/Xuanzang\n', 'http://fategrandorder.wikia.com/wiki/Nitocris\n', 'http://fategrandorder.wikia.com/wiki/Leonardo_Da_Vinci\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Merlin\n', 'http://fategrandorder.wikia.com/wiki/Avicebron\n', 'http://fategrandorder.wikia.com/wiki/Sieg\n', 'http://fategrandorder.wikia.com/wiki/Anastasia_Nikolaevna_Romanova\n', 'http://fategrandorder.wikia.com/wiki/Cursed_Arm_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Stheno\n', 'http://fategrandorder.wikia.com/wiki/Jing_Ke\n', 'http://fategrandorder.wikia.com/wiki/Charles-Henri_Sanson\n', 'http://fategrandorder.wikia.com/wiki/The_Phantom_of_the_Opera\n', 'http://fategrandorder.wikia.com/wiki/Mata_Hari\n', 'http://fategrandorder.wikia.com/wiki/Carmilla\n', 'http://fategrandorder.wikia.com/wiki/Jack_the_Ripper\n', 'http://fategrandorder.wikia.com/wiki/Henry_Jekyll_&_Hyde\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X\n', 'http://fategrandorder.wikia.com/wiki/Ryougi_Shiki_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Hundred-Faced_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Fuuma_Kotarou\n', 'http://fategrandorder.wikia.com/wiki/Shuten_Douji\n', 'http://fategrandorder.wikia.com/wiki/Hassan_of_Serenity\n', 'http://fategrandorder.wikia.com/wiki/Cleopatra\n', 'http://fategrandorder.wikia.com/wiki/Nitocris_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Semiramis\n', 'http://fategrandorder.wikia.com/wiki/Heracles\n', 'http://fategrandorder.wikia.com/wiki/Lancelot\n', 'http://fategrandorder.wikia.com/wiki/Lu_Bu\n', 'http://fategrandorder.wikia.com/wiki/Spartacus\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki\n', 'http://fategrandorder.wikia.com/wiki/Vlad_III\n', 'http://fategrandorder.wikia.com/wiki/Asterios\n', 'http://fategrandorder.wikia.com/wiki/Caligula\n', 'http://fategrandorder.wikia.com/wiki/Darius_III\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Paul_Bunyan\n', 'http://fategrandorder.wikia.com/wiki/Atalanta_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga_(Berserker)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc\n", 'http://fategrandorder.wikia.com/wiki/Amakusa_Shirou\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha_(Ruler)\n', 'http://fategrandorder.wikia.com/wiki/Sherlock_Holmes\n', 'http://fategrandorder.wikia.com/wiki/Edmond_Dantes\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(alter)\n", 'http://fategrandorder.wikia.com/wiki/Angra_Mainyu\n', 'http://fategrandorder.wikia.com/wiki/Gorgon\n', 'http://fategrandorder.wikia.com/wiki/Antonio_Salieri\n', 'http://fategrandorder.wikia.com/wiki/Hessian_Lobo\n', 'http://fategrandorder.wikia.com/wiki/BB\n', 'http://fategrandorder.wikia.com/wiki/Passionlip\n', 'http://fategrandorder.wikia.com/wiki/Sessyoin_Kiara\n', 'http://fategrandorder.wikia.com/wiki/Abigail_Williams\n', 'http://fategrandorder.wikia.com/wiki/Katsushika_Hokusai']
        kin=random.choice(kinlist)
        await client.send_message(message.channel, "Your Rama assigned kin is... %s" % kin)
        
    if message.content.startswith("r!birthday"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441190970403323914/441574720761233408/Cy_rRxlUcAAYiC5.png")
        await client.send_message(message.channel, embed = e)
             

@client.event
async def on_ready():
    print("Servant, Saber. Great King of Kosala, Rama. It's alright, leave it all to me!")


client.run("NDM5MDM4NzI2MjMyOTk3ODk4.DcNkcA.3LifXMyrco4ezO7nItJ5cdfTGho")
