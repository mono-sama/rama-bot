import discord
from discord.ext import commands
import asyncio
import random
import urllib
import urllib.request
import os
import datetime

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('r!ramatalk'):
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
        
    if message.content.startswith("r!invite"):
        await client.send_message(message.channel, """
Want to add me elsewhere? Sure thing!
**Bot permissions only:** https://discordapp.com/api/oauth2/authorize?client_id=439038726232997898&permissions=0&scope=bot
**+ Admin permissions:** https://discordapp.com/api/oauth2/authorize?client_id=439038726232997898&permissions=8&scope=bot
""")
        
    if message.content.startswith("r!respect"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441190970403323914/452694136555044864/F.gif")
        await client.send_message(message.channel, embed = e)
        
    if message.content.startswith("r!avatar"):
        for user in message.mentions:
            avatarurl=user.avatar_url
            e = discord.Embed()
            e.set_image(url=avatarurl)
            await client.send_message(message.channel, embed = e)
        
    if message.content.startswith("r!say"):
        if "yes" in (y.name.lower() for y in message.author.roles) or message.author.id == "227446010094288896":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            if message.author.id == "227446010094288896":
                await client.delete_message(message) 
        else:
            await client.send_message(message.channel, "Sorry! You're not allowed to do that.")


    if message.content.startswith("r!happy"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/435484833997783053/439044105264168960/unknown-61.png")
        await client.send_message(message.channel, embed = e)
        
        
    if message.content.startswith("r!okada"):
        e = discord.Embed()
        msg="***RAT ALERT***"
        e.set_image(url="https://cdn.discordapp.com/attachments/414700659884163073/456518684698083338/unknown.png")
        await client.send_message(message.channel, msg, embed = e)

    if message.content.startswith("r!mono"):
        choice=random.randint(1,4)
        if choice==1:
            await client.send_message(message.channel, "You mean the devil herself, right...? Why would you ask for such a thing?!")
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/435494001710333952/439531257538281485/satan.png")
            await client.send_message(message.channel, embed = e)

        elif choice==2:
            await client.send_message(message.channel, "I don't think she's around right now. Wanna leave a message?")

        elif choice==3:
            await client.send_message(message.channel, "Um... She's over there.")
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/439040144914251776/439889095246872607/suspicious.png")
            await client.send_message(message.channel, embed = e)

    if message.content.startswith("r!ping"):
            await client.send_message(message.channel, "Pong!")
    
    if message.content.startswith("r!summon"):
        args = message.content.split(" ")
        option = " ".join(args[1:])
        option=int(option)
        summonlist=[]
        fulllist="--------------\n"
        summon=""
        foursummon=""

        CEthree=["Mooncell Automaton","Runestone","Anchors Aweigh","Demon Boar","Clock Tower","Ryudoji Temple","Mana Gauge","Elixir of Love","Storch Ritter","Hermitage","Motored Cuirassier","Stuffed Lion","Lugh's Halo","Beast of Billows","Self Geas Scroll"]
        CEfour=["Iron-Willed Training","Primeval Curse","Projection","Gandr","Verdant Sound of Destruction","Gem Magecraft: Antumbra","Be Elegant","The Imaginary Element","Divine Banquet","Angel's Song","Seal Designation Enforcer","Holy Shroud of Magdalene","With One Strike","Code Cast","Knight's Dignity","Necromancy","Awakened Will","Golden Millennium Tree","Record Holder","Art of the Poisonous Snake","Art of Death","Gentle Affection","Innocent Maiden"]
        CEfive=["Formal Craft","Imaginary Around","Limited/Zero Over","Kaleidoscope","Heaven's Feel","Prisma Cosmos","The Black Grail","Victor of the Moon","Another Ending","A Fragment of 2030","500 Year Obsession","Vessel of the Saint","Ideal Holy King","Volumen Hydrargyrum","Before Awakening"]
        SERVthree=["Gaius Julius Caesar","Fergus mac Róich","Gilles de Rais","Robin Hood","David","Billy the Kid","Euryale","Gilgamesh (Child)","Cú Chulainn","Diarmuid Ua Duibhne","Cú Chulainn (Prototype)","Romulus","Hektor","Medusa","Boudica","Ushiwakamaru","Alexander","Medea","Gilles de Rais","Paracelsus von Hohenheim","Charles Babbage","Mephistopheles","Geronimo","Hassan of the Hundred Personas","Henry Jekyll & Hyde","Jing Ke","Lu Bu Fengxian","Darius III","Kiyohime"]
        SERVfour=["Altria Pendragon (Alter)","Nero Claudius","Siegfried","Rama","Chevalier d'Eon","Emiya","Atalante","Elizabeth Báthory","Fionn mac Cumhaill","Li Shuwen","Astolfo","Anne Bonny & Mary Read","Marie Antoinette","Martha","Nursery Rhyme","Medea (Lily)","Helena Blavatsky","Thomas Edison","Stheno","Emiya (Assassin)","Carmilla","Heracles","Lancelot","Frankenstein","Beowulf","Tamamo Cat"]
        SERVfive=["Altria Pendragon","Mordred","Altera","Orion","Nikola Tesla","Arjuna","Karna","Francis Drake","Queen Medb","Tamamo-no-Mae","Zhuge Liang (Lord El-Melloi II)","Jack the Ripper","Vlad III","Florence Nightingale","Cú Chulainn (Alter)","Jeanne d'Arc"]
        
        if option==69:
            e = discord.Embed()
            e.set_image(url="https://cdn.discordapp.com/attachments/446268259721805825/446780412400762880/unknown-93.png")
            await client.send_message(message.channel, embed = e)
        
        elif option>10:
            await client.send_message(message.channel, "You can only summon up to 10 times! Don't be greedy!")
 
        else:
            if option==10:
                option-=1
                fourchance=random.randint(1,100)
                if fourchance<=80:
                    foursummon="4✰ CE: "
                    foursummon+=random.choice(CEfour)
                else:
                    foursummon="**4✰**: "
                    foursummon+=random.choice(SERVfour)
                foursummon+="\n"
                summonlist.append(foursummon)

            for i in range(0,option):
                chance=random.randint(1,100)
                if chance<=40:
                    summon="3✰ CE: "
                    summon+=random.choice(CEthree)
                elif chance<=80 and chance>40:
                    summon="**3✰**: "
                    summon+=random.choice(SERVthree)
                elif chance<=92 and chance>80:
                    summon="4✰ CE: "
                    summon+=random.choice(CEfour)
                elif chance<=95 and chance>92:
                    summon="**4✰**: "
                    summon+=random.choice(SERVfour)
                elif chance<=99 and chance>95:
                    summon="5✰ CE: "
                    summon+=random.choice(CEfive)
                elif chance==100:
                    summon="**5✰**: "
                    summon+=random.choice(SERVfive)
                summon+="\n"
                summonlist.append(summon)

            for x in summonlist:
                fulllist+=x
            fulllist+="--------------"

            msg = "{0.author.mention}".format(message)
            e = discord.Embed()
            e.add_field(name="Summoning Results:", value=fulllist, inline=False)
            await client.send_message(message.channel, msg, embed = e)

    
    if message.content.startswith("r!randomfgo"):
            response = urllib.request.urlopen('http://fategrandorder.wikia.com/wiki/Special:Random')
            await client.send_message(message.channel, response.geturl())

    if message.content.startswith("r!changegame"):
        if message.author.id == "227446010094288896" or "414626125889667072" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "A new game...? Very well.")
            await client.change_presence(game=discord.Game(name="%s" % (" ".join(args[1:]))))
        else:
            await client.send_message(message.channel, "You don't have permission to do that!")
        
    if message.content.startswith("rama, ") and message.content.endswith("?"):
        answers=["It is certain.","You may rely on it.","Ask again later.","Reply hazy, try again.","My reply is no.","My sources say no."]
        reply=random.choice(answers)
        await client.send_message(message.channel, reply)
        
    if "rama play despacito" in message.content.lower():
        reply="https://www.youtube.com/watch?v=kJQP7kiw5Fk"
        await client.send_message(message.channel, reply)
        
    if "mozart play despacito" in message.content.lower():
        reply="https://www.youtube.com/watch?v=GmtTDvNcXcU"
        await client.send_message(message.channel, reply)
        
    if "tristan play despacito" in message.content.lower():
        reply="https://youtu.be/1yuOLpNlD8c?t=13"
        await client.send_message(message.channel, reply)
    
    
    if "goodnight" in message.content.lower():
        if message.author.id == "227446010094288896":
            await client.send_message(message.channel,"Goodnight. Dream of the quartz you'll never have.")
            
    if message.content.startswith("r!ghost"):
        args = message.content.split(" ")
        await client.send_message(discord.Object(id='446268259721805825'), "%s" % (" ".join(args[1:])))
        
        
    if message.content.startswith("r!help"):
        await client.send_message(message.channel, """
**General Commands**
r!hello - *Say hello!*
r!ping - *Pong! Tests if the bot is online.*
r!8ball - *Get Rama's opinion on things.*
r!avatar - *Snatch someone's avatar!*
r!roll [number] - *Roll a die with the specified number of sides! E.G. r!roll 20 rolls a d20, etc.*
**Fate/Bullshit**
r!respect - *Pay respects with Caster Cu!*
r!ramatalk - *Random Rama quote.*
r!randomfgo - *Posts a random page from the F/GO wiki.*
r!fatekin - *Get your fresh F/GO kins here!*
r!classes - *For when you can't be bothered to check up class advantages in game.*
r!lancelot - *Lancelot fucks.*
r!birthday - *Happy Birthday!*
r!nasty - *Lancelot booty shorts in Rome.*
r!5star - *Can't roll any 5-stars? Pretend you did!*
r!summon [0-10] - *F/GO NA Summon Simulator! I'm not responsible for any disappointment caused.*
**Dangan Ronpa: Goodbye Ramabot**
*Coming soon!*
**Command Spells**
r!say - *Make Rama say something*
r!changegame - *Change the game Rama is playing.*""")

            
    if message.content.startswith("r!aster"):
        goodbyes=["Goodbye.", "Sayonara.","Hmph, it seems you have bad luck. For you to encounter me, Rama!"]
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

    if message.content.startswith("r!fatekin"):
        if message.author.id == "208017434374963200":
            saberfaces=['http://fategrandorder.wikia.com/wiki/Artoria_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius_(Bride)\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Okita_Souji\n', 'http://fategrandorder.wikia.com/wiki/Bedivere\n', 'http://fategrandorder.wikia.com/wiki/Arthur_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Rider_Alter)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)_(Santa_Lily)\n", 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Santa_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Mordred\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc\n", "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(alter)"]
            saberkin=random.choice(saberfaces)
            msg = "{0.author.mention}".format(message)
            await client.send_message(message.channel, msg + " Your Rama assigned kin is... %s" % saberkin)
            
        elif message.author.id == "227446010094288896":
            if message.content.startswith("r!fatekin bypass"):
                kinlist=['http://fategrandorder.wikia.com/wiki/Mashu_Kyrielight\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius\n', 'http://fategrandorder.wikia.com/wiki/Siegfried\n', 'http://fategrandorder.wikia.com/wiki/Gaius_Julius_Caesar\n', 'http://fategrandorder.wikia.com/wiki/Attila\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais_(Saber)\n', "http://fategrandorder.wikia.com/wiki/Chevalier_d'Eon\n", 'http://fategrandorder.wikia.com/wiki/Okita_Souji\n', 'http://fategrandorder.wikia.com/wiki/Fergus_mac_Róich\n', 'http://fategrandorder.wikia.com/wiki/Lancelot_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/Gawain\n', 'http://fategrandorder.wikia.com/wiki/Bedivere\n', 'http://fategrandorder.wikia.com/wiki/Arthur_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Frankenstein_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh\n', 'http://fategrandorder.wikia.com/wiki/Robin_Hood\n', 'http://fategrandorder.wikia.com/wiki/Solomon\n', 'http://fategrandorder.wikia.com/wiki/Atalanta\n', 'http://fategrandorder.wikia.com/wiki/Euryale\n', 'http://fategrandorder.wikia.com/wiki/Arash\n', 'http://fategrandorder.wikia.com/wiki/Orion\n', 'http://fategrandorder.wikia.com/wiki/David\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga\n', 'http://fategrandorder.wikia.com/wiki/Nikola_Tesla\n', 'http://fategrandorder.wikia.com/wiki/Arjuna\n', 'http://fategrandorder.wikia.com/wiki/Kid_Gil\n', 'http://fategrandorder.wikia.com/wiki/Billy_The_Kid\n', 'http://fategrandorder.wikia.com/wiki/Tristan\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)\n', 'http://fategrandorder.wikia.com/wiki/Ishtar\n', 'http://fategrandorder.wikia.com/wiki/James_Moriarty\n', 'http://fategrandorder.wikia.com/wiki/Chiron\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Prototype)\n', 'http://fategrandorder.wikia.com/wiki/Hector\n', 'http://fategrandorder.wikia.com/wiki/Scáthach\n', 'http://fategrandorder.wikia.com/wiki/Diarmuid_Ua_Duibhne\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Karna\n', 'http://fategrandorder.wikia.com/wiki/Fionn_mac_Cumhaill\n', 'http://fategrandorder.wikia.com/wiki/Brynhildr\n', 'http://fategrandorder.wikia.com/wiki/Li_Shuwen_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime_(Lancer)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)_(Santa_Lily)\n", 'http://fategrandorder.wikia.com/wiki/Enkidu\n', 'http://fategrandorder.wikia.com/wiki/Jaguar_Man\n', 'http://fategrandorder.wikia.com/wiki/Medusa\n', 'http://fategrandorder.wikia.com/wiki/Georgios\n', 'http://fategrandorder.wikia.com/wiki/Edward_Teach\n', 'http://fategrandorder.wikia.com/wiki/Boudica\n', 'http://fategrandorder.wikia.com/wiki/Ushiwakamaru\n', 'http://fategrandorder.wikia.com/wiki/Alexander\n', 'http://fategrandorder.wikia.com/wiki/Marie_Antoinette\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha\n', 'http://fategrandorder.wikia.com/wiki/Francis_Drake\n', 'http://fategrandorder.wikia.com/wiki/Anne_Bonny_&_Mary_Read\n', 'http://fategrandorder.wikia.com/wiki/Ozymandias\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Santa_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Astolfo\n', 'http://fategrandorder.wikia.com/wiki/Medb\n', 'http://fategrandorder.wikia.com/wiki/Iskandar\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki_(Rider)\n', 'http://fategrandorder.wikia.com/wiki/Achilles\n', 'http://fategrandorder.wikia.com/wiki/Medea\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais\n', 'http://fategrandorder.wikia.com/wiki/Hans_Christian_Andersen\n', 'http://fategrandorder.wikia.com/wiki/William_Shakespeare\n', 'http://fategrandorder.wikia.com/wiki/Mephistopheles\n', 'http://fategrandorder.wikia.com/wiki/Wolfgang_Amadeus_Mozart\n', 'http://fategrandorder.wikia.com/wiki/Zhuge_Liang_(Lord_El-Melloi_II)\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory_(Halloween)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae\n', 'http://fategrandorder.wikia.com/wiki/Medea_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nursery_Rhyme\n', 'http://fategrandorder.wikia.com/wiki/Paracelsus_von_Hohenheim\n', 'http://fategrandorder.wikia.com/wiki/Charles_Babbage\n', 'http://fategrandorder.wikia.com/wiki/Helena_Blavatsky\n', 'http://fategrandorder.wikia.com/wiki/Thomas_Edison\n', 'http://fategrandorder.wikia.com/wiki/Geronimo\n', 'http://fategrandorder.wikia.com/wiki/Irisviel_(Dress_of_Heaven)\n', 'http://fategrandorder.wikia.com/wiki/Xuanzang\n', 'http://fategrandorder.wikia.com/wiki/Nitocris\n', 'http://fategrandorder.wikia.com/wiki/Leonardo_Da_Vinci\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Merlin\n', 'http://fategrandorder.wikia.com/wiki/Avicebron\n', 'http://fategrandorder.wikia.com/wiki/Sieg\n', 'http://fategrandorder.wikia.com/wiki/Anastasia_Nikolaevna_Romanova\n', 'http://fategrandorder.wikia.com/wiki/Cursed_Arm_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Stheno\n', 'http://fategrandorder.wikia.com/wiki/Jing_Ke\n', 'http://fategrandorder.wikia.com/wiki/Charles-Henri_Sanson\n', 'http://fategrandorder.wikia.com/wiki/The_Phantom_of_the_Opera\n', 'http://fategrandorder.wikia.com/wiki/Mata_Hari\n', 'http://fategrandorder.wikia.com/wiki/Carmilla\n', 'http://fategrandorder.wikia.com/wiki/Jack_the_Ripper\n', 'http://fategrandorder.wikia.com/wiki/Henry_Jekyll_&_Hyde\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X\n', 'http://fategrandorder.wikia.com/wiki/Ryougi_Shiki_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Hundred-Faced_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Fuuma_Kotarou\n', 'http://fategrandorder.wikia.com/wiki/Shuten_Douji\n', 'http://fategrandorder.wikia.com/wiki/Hassan_of_Serenity\n', 'http://fategrandorder.wikia.com/wiki/Cleopatra\n', 'http://fategrandorder.wikia.com/wiki/Nitocris_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Semiramis\n', 'http://fategrandorder.wikia.com/wiki/Heracles\n', 'http://fategrandorder.wikia.com/wiki/Lancelot\n', 'http://fategrandorder.wikia.com/wiki/Lu_Bu\n', 'http://fategrandorder.wikia.com/wiki/Spartacus\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki\n', 'http://fategrandorder.wikia.com/wiki/Vlad_III\n', 'http://fategrandorder.wikia.com/wiki/Asterios\n', 'http://fategrandorder.wikia.com/wiki/Caligula\n', 'http://fategrandorder.wikia.com/wiki/Darius_III\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Paul_Bunyan\n', 'http://fategrandorder.wikia.com/wiki/Atalanta_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga_(Berserker)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc\n", 'http://fategrandorder.wikia.com/wiki/Amakusa_Shirou\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha_(Ruler)\n', 'http://fategrandorder.wikia.com/wiki/Sherlock_Holmes\n', 'http://fategrandorder.wikia.com/wiki/Edmond_Dantes\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)\n", 'http://fategrandorder.wikia.com/wiki/Angra_Mainyu\n', 'http://fategrandorder.wikia.com/wiki/Gorgon\n', 'http://fategrandorder.wikia.com/wiki/Antonio_Salieri\n', 'http://fategrandorder.wikia.com/wiki/Hessian_Lobo\n', 'http://fategrandorder.wikia.com/wiki/BB\n', 'http://fategrandorder.wikia.com/wiki/Passionlip\n', 'http://fategrandorder.wikia.com/wiki/Sessyoin_Kiara\n', 'http://fategrandorder.wikia.com/wiki/Abigail_Williams\n', 'http://fategrandorder.wikia.com/wiki/Katsushika_Hokusai']
                kin=random.choice(kinlist)
                msg = "{0.author.mention}".format(message)
                await client.send_message(message.channel, msg + " Your Rama assigned kin is... %s" % kin)
            else:
                msg = "{0.author.mention}".format(message)
                await client.send_message(message.channel, msg + " Your Rama assigned kin is... %s" % 'http://fategrandorder.wikia.com/wiki/Rama\n')
        
        elif message.author.id == "289133057414529024":
            msg = "{0.author.mention}".format(message)
            furries=["http://fategrandorder.wikia.com/wiki/Chiron","http://fategrandorder.wikia.com/wiki/Thomas_Edison","http://fategrandorder.wikia.com/wiki/David","http://fategrandorder.wikia.com/wiki/Asterios","http://fategrandorder.wikia.com/wiki/Henry_Jekyll_&_Hyde"]
            furrykin=random.choice(furries)
            await client.send_message(message.channel, msg + " Your Rama assigned kin is... %s" % furrykin)
        
        else:
            kinlist=['http://fategrandorder.wikia.com/wiki/Mashu_Kyrielight\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius\n', 'http://fategrandorder.wikia.com/wiki/Siegfried\n', 'http://fategrandorder.wikia.com/wiki/Gaius_Julius_Caesar\n', 'http://fategrandorder.wikia.com/wiki/Attila\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais_(Saber)\n', "http://fategrandorder.wikia.com/wiki/Chevalier_d'Eon\n", 'http://fategrandorder.wikia.com/wiki/Okita_Souji\n', 'http://fategrandorder.wikia.com/wiki/Fergus_mac_Róich\n', 'http://fategrandorder.wikia.com/wiki/Lancelot_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/Gawain\n', 'http://fategrandorder.wikia.com/wiki/Bedivere\n', 'http://fategrandorder.wikia.com/wiki/Arthur_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Frankenstein_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh\n', 'http://fategrandorder.wikia.com/wiki/Robin_Hood\n', 'http://fategrandorder.wikia.com/wiki/Solomon\n', 'http://fategrandorder.wikia.com/wiki/Atalanta\n', 'http://fategrandorder.wikia.com/wiki/Euryale\n', 'http://fategrandorder.wikia.com/wiki/Arash\n', 'http://fategrandorder.wikia.com/wiki/Orion\n', 'http://fategrandorder.wikia.com/wiki/David\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga\n', 'http://fategrandorder.wikia.com/wiki/Nikola_Tesla\n', 'http://fategrandorder.wikia.com/wiki/Arjuna\n', 'http://fategrandorder.wikia.com/wiki/Kid_Gil\n', 'http://fategrandorder.wikia.com/wiki/Billy_The_Kid\n', 'http://fategrandorder.wikia.com/wiki/Tristan\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)\n', 'http://fategrandorder.wikia.com/wiki/Ishtar\n', 'http://fategrandorder.wikia.com/wiki/James_Moriarty\n', 'http://fategrandorder.wikia.com/wiki/Chiron\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Prototype)\n', 'http://fategrandorder.wikia.com/wiki/Hector\n', 'http://fategrandorder.wikia.com/wiki/Scáthach\n', 'http://fategrandorder.wikia.com/wiki/Diarmuid_Ua_Duibhne\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Karna\n', 'http://fategrandorder.wikia.com/wiki/Fionn_mac_Cumhaill\n', 'http://fategrandorder.wikia.com/wiki/Brynhildr\n', 'http://fategrandorder.wikia.com/wiki/Li_Shuwen_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime_(Lancer)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)_(Santa_Lily)\n", 'http://fategrandorder.wikia.com/wiki/Enkidu\n', 'http://fategrandorder.wikia.com/wiki/Jaguar_Man\n', 'http://fategrandorder.wikia.com/wiki/Medusa\n', 'http://fategrandorder.wikia.com/wiki/Georgios\n', 'http://fategrandorder.wikia.com/wiki/Edward_Teach\n', 'http://fategrandorder.wikia.com/wiki/Boudica\n', 'http://fategrandorder.wikia.com/wiki/Ushiwakamaru\n', 'http://fategrandorder.wikia.com/wiki/Alexander\n', 'http://fategrandorder.wikia.com/wiki/Marie_Antoinette\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha\n', 'http://fategrandorder.wikia.com/wiki/Francis_Drake\n', 'http://fategrandorder.wikia.com/wiki/Anne_Bonny_&_Mary_Read\n', 'http://fategrandorder.wikia.com/wiki/Ozymandias\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Santa_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Astolfo\n', 'http://fategrandorder.wikia.com/wiki/Medb\n', 'http://fategrandorder.wikia.com/wiki/Iskandar\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki_(Rider)\n', 'http://fategrandorder.wikia.com/wiki/Achilles\n', 'http://fategrandorder.wikia.com/wiki/Medea\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais\n', 'http://fategrandorder.wikia.com/wiki/Hans_Christian_Andersen\n', 'http://fategrandorder.wikia.com/wiki/William_Shakespeare\n', 'http://fategrandorder.wikia.com/wiki/Mephistopheles\n', 'http://fategrandorder.wikia.com/wiki/Wolfgang_Amadeus_Mozart\n', 'http://fategrandorder.wikia.com/wiki/Zhuge_Liang_(Lord_El-Melloi_II)\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory_(Halloween)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae\n', 'http://fategrandorder.wikia.com/wiki/Medea_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nursery_Rhyme\n', 'http://fategrandorder.wikia.com/wiki/Paracelsus_von_Hohenheim\n', 'http://fategrandorder.wikia.com/wiki/Charles_Babbage\n', 'http://fategrandorder.wikia.com/wiki/Helena_Blavatsky\n', 'http://fategrandorder.wikia.com/wiki/Thomas_Edison\n', 'http://fategrandorder.wikia.com/wiki/Geronimo\n', 'http://fategrandorder.wikia.com/wiki/Irisviel_(Dress_of_Heaven)\n', 'http://fategrandorder.wikia.com/wiki/Xuanzang\n', 'http://fategrandorder.wikia.com/wiki/Nitocris\n', 'http://fategrandorder.wikia.com/wiki/Leonardo_Da_Vinci\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Merlin\n', 'http://fategrandorder.wikia.com/wiki/Avicebron\n', 'http://fategrandorder.wikia.com/wiki/Sieg\n', 'http://fategrandorder.wikia.com/wiki/Anastasia_Nikolaevna_Romanova\n', 'http://fategrandorder.wikia.com/wiki/Cursed_Arm_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Stheno\n', 'http://fategrandorder.wikia.com/wiki/Jing_Ke\n', 'http://fategrandorder.wikia.com/wiki/Charles-Henri_Sanson\n', 'http://fategrandorder.wikia.com/wiki/The_Phantom_of_the_Opera\n', 'http://fategrandorder.wikia.com/wiki/Mata_Hari\n', 'http://fategrandorder.wikia.com/wiki/Carmilla\n', 'http://fategrandorder.wikia.com/wiki/Jack_the_Ripper\n', 'http://fategrandorder.wikia.com/wiki/Henry_Jekyll_&_Hyde\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X\n', 'http://fategrandorder.wikia.com/wiki/Ryougi_Shiki_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Hundred-Faced_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Fuuma_Kotarou\n', 'http://fategrandorder.wikia.com/wiki/Shuten_Douji\n', 'http://fategrandorder.wikia.com/wiki/Hassan_of_Serenity\n', 'http://fategrandorder.wikia.com/wiki/Cleopatra\n', 'http://fategrandorder.wikia.com/wiki/Nitocris_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Semiramis\n', 'http://fategrandorder.wikia.com/wiki/Heracles\n', 'http://fategrandorder.wikia.com/wiki/Lancelot\n', 'http://fategrandorder.wikia.com/wiki/Lu_Bu\n', 'http://fategrandorder.wikia.com/wiki/Spartacus\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki\n', 'http://fategrandorder.wikia.com/wiki/Vlad_III\n', 'http://fategrandorder.wikia.com/wiki/Asterios\n', 'http://fategrandorder.wikia.com/wiki/Caligula\n', 'http://fategrandorder.wikia.com/wiki/Darius_III\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Paul_Bunyan\n', 'http://fategrandorder.wikia.com/wiki/Atalanta_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga_(Berserker)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc\n", 'http://fategrandorder.wikia.com/wiki/Amakusa_Shirou\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha_(Ruler)\n', 'http://fategrandorder.wikia.com/wiki/Sherlock_Holmes\n', 'http://fategrandorder.wikia.com/wiki/Edmond_Dantes\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)\n", 'http://fategrandorder.wikia.com/wiki/Angra_Mainyu\n', 'http://fategrandorder.wikia.com/wiki/Gorgon\n', 'http://fategrandorder.wikia.com/wiki/Antonio_Salieri\n', 'http://fategrandorder.wikia.com/wiki/Hessian_Lobo\n', 'http://fategrandorder.wikia.com/wiki/BB\n', 'http://fategrandorder.wikia.com/wiki/Passionlip\n', 'http://fategrandorder.wikia.com/wiki/Sessyoin_Kiara\n', 'http://fategrandorder.wikia.com/wiki/Abigail_Williams\n', 'http://fategrandorder.wikia.com/wiki/Katsushika_Hokusai']
            kin=random.choice(kinlist)
            msg = "{0.author.mention}".format(message)
            await client.send_message(message.channel, msg + " Your Rama assigned kin is... %s" % kin)
        
    if message.content.startswith("r!birthday"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441190970403323914/441574720761233408/Cy_rRxlUcAAYiC5.png")
        await client.send_message(message.channel, embed = e)

             
    if message.content.startswith("r!nasty"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/439040144914251776/441676875136237579/ARE_YOU_LANCELOT.png")
        await client.send_message(message.channel, embed = e)

        
    if message.content.startswith("r!5star"):
        ssrs=["http://fategrandorder.wikia.com/wiki/Shuten_Douji","http://fategrandorder.wikia.com/wiki/Minamoto_no_Yorimitsu","http://fategrandorder.wikia.com/wiki/Jeanne_d%27Arc_(Alter)","http://fategrandorder.wikia.com/wiki/Sc%C3%A1thach","http://fategrandorder.wikia.com/wiki/Sherlock_Holmes","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon","http://fategrandorder.wikia.com/wiki/Jeanne_d%27Arc","http://fategrandorder.wikia.com/wiki/Sakata_Kintoki","http://fategrandorder.wikia.com/wiki/Merlin","http://fategrandorder.wikia.com/wiki/Gilgamesh","http://fategrandorder.wikia.com/wiki/Mordred","http://fategrandorder.wikia.com/wiki/Miyamoto_Musashi","http://fategrandorder.wikia.com/wiki/%22The_Old_Man_of_the_Mountain%22","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)","http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae","http://fategrandorder.wikia.com/wiki/Achilles","http://fategrandorder.wikia.com/wiki/Zhuge_Liang_(Lord_El-Melloi_II)","http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Alter)","http://fategrandorder.wikia.com/wiki/Nightingale","http://fategrandorder.wikia.com/wiki/Ozymandias","http://fategrandorder.wikia.com/wiki/Anastasia_Nikolaevna_Romanova","http://fategrandorder.wikia.com/wiki/Arthur_Pendragon_(Prototype)","http://fategrandorder.wikia.com/wiki/Brynhildr","http://fategrandorder.wikia.com/wiki/Xuanzang","http://fategrandorder.wikia.com/wiki/Jack_the_Ripper","http://fategrandorder.wikia.com/wiki/Okita_Souji","http://fategrandorder.wikia.com/wiki/Katsushika_Hokusai","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)","http://fategrandorder.wikia.com/wiki/Scheherazade","http://fategrandorder.wikia.com/wiki/Karna","http://fategrandorder.wikia.com/wiki/Sessyoin_Kiara","http://fategrandorder.wikia.com/wiki/Medb","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Rider_Alter)","http://fategrandorder.wikia.com/wiki/Attila","http://fategrandorder.wikia.com/wiki/Enkidu","http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae_(Lancer)","http://fategrandorder.wikia.com/wiki/Orion","http://fategrandorder.wikia.com/wiki/Semiramis","http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)","http://fategrandorder.wikia.com/wiki/Illyasviel_von_Einzbern","http://fategrandorder.wikia.com/wiki/Ivan_the_Terrible","http://fategrandorder.wikia.com/wiki/Nero_Claudius_(Bride)","http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X","http://fategrandorder.wikia.com/wiki/Edmond_Dantes","http://fategrandorder.wikia.com/wiki/Osakabehime","http://fategrandorder.wikia.com/wiki/Iskandar","http://fategrandorder.wikia.com/wiki/Francis_Drake","http://fategrandorder.wikia.com/wiki/Amakusa_Shirou","http://fategrandorder.wikia.com/wiki/James_Moriarty","http://fategrandorder.wikia.com/wiki/Leonardo_Da_Vinci","http://fategrandorder.wikia.com/wiki/Arjuna","http://fategrandorder.wikia.com/wiki/Quetzalcoatl","http://fategrandorder.wikia.com/wiki/Nero_Claudius_(Caster)","http://fategrandorder.wikia.com/wiki/Vlad_III","http://fategrandorder.wikia.com/wiki/Meltlilith","http://fategrandorder.wikia.com/wiki/Cleopatra","http://fategrandorder.wikia.com/wiki/Ryougi_Shiki_(Saber)","http://fategrandorder.wikia.com/wiki/Hijikata_Toshizou","http://fategrandorder.wikia.com/wiki/Nikola_Tesla"]
        ssr=random.choice(ssrs)
        msg = "{0.author.mention}".format(message)
        await client.send_message(message.channel, "Congratulations, " + msg + "! You summoned %s !" % ssr)
        
    if message.content.startswith("r!classes"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/420827955779076096/441986891122868254/latest.png")
        await client.send_message(message.channel, embed = e)
        
    if message.content.startswith("r!lancelot"):
        locations=["FUYUKI","RYUUDOU TEMPLE","CARNIVAL PHANTASM","YOUR NIGHTMARES","GARDEN OF AVALON","HIS ARMOR", "SHINJUKU","MSPAINT","SNARK'S HOUSE","YOUR SUPPORT LIST","YOUR GACHA ROLLS","YOUR SAINT QUARTZ","DA VINCI'S SHOP","A RANDOM PARKING LOT IN JAPAN","A LAKE","BEHIND 7/11","F/GO SUPPORT GROUP","ORLEANS","ROME","OKEANOS","LONDON","AMERICA","CAMELOT","BABYLONIA","MEDB'S CARRIAGE","ACHILLES' CHARIOT","AN OLD SOCK","BOOTY SHORTS","OZYMANDIAS' LARGE TEMPLE COMPLEX, PRESENT IN HIS NOBLE PHANTASM, RAMESSEUM TENTYRIS, WHEREIN A LARGE NUMBER OF PHANTASMAL BEASTS DWELL INSIDE","GILGAMESH'S TREASURY","MOON CELL","THE FAR SIDE OF THE MOON","THE NEAR SIDE OF THE MOON","ARTURIA'S HOUSE","SEMIRAMIS' HANGING GARDENS OF BABYLON","CHALDEA'S BATHROOM","ISKANDAR'S IONIAN HETAIROI","INFINITY WAR","THE HOLY GRAIL'S INNER CONTENTS","THE GRAIL SAUCE","UNLIMITED BLADE WORKS","THE GRANDORDER SUBREDDIT","OFFICIAL FATE/GRAND ORDER DISCORD SERVER","A FATE MMD","MONTY PYTHON AND THE HOLY GRAIL","FATE/PROTOTYPE","FILTHYFATECONFESSIONS","A TRUCK","REDDIT","CUCKLAND","SHIROU'S KITCHEN","EINZBERN CASTLE","HOMUHARA ACADEMY","UNDER THE KNIGHT OF THE ROUND TABLE'S ROUND TABLE","THE OCEAN","THE EINZBERN CONSULTATION ROOM","DESPACITO"] 
        fucksin=random.choice(locations)
        lancelotfucksin="*LANCELOT FUCKS IN " + fucksin + "*"
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441831504604037122/441974102052306954/20180504_154700.png")
        await client.send_message(message.channel, lancelotfucksin, embed = e)

        
    if message.content.startswith("r!members"):
        await client.send_message(message.channel, "Sending debug information to the test dungeon....")
        x = message.server.members
        for person in x:
            person=str(person)
            person=person[:-5]
            await client.send_message(discord.Object(id='446268259721805825'), person)
            
            
    if message.content.startswith("r!roll"):
        args = message.content.split(" ")
        number=" ".join(args[1:])
        number=int(number)
        chosenroll=random.randint(1,number)
        chosenroll=str(chosenroll)
        msg = "{0.author.mention}".format(message)
        full=msg+" You rolled a **" + chosenroll + "**!"
        await client.send_message(message.channel, full)
        
               
@client.event
async def on_ready():
    print("Servant, Saber. Great King of Kosala, Rama. It's alright, leave it all to me!")

token=os.environ["BOT_TOKEN"]
client.run(token)
