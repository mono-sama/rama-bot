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
        if "yes" in (y.name.lower() for y in message.author.roles) or message.author.id == "227446010094288896" or "yeehaw" in (y.name.lower() for y in message.author.roles):
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            if message.author.id == "227446010094288896":
                await client.delete_message(message) 
        else:
            await client.send_message(message.channel, "Hey! I can't let you do that!!")      
    
    if message.content.startswith("r!ramacake"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/470680030951768064/470681235958530049/2018-07-22_12-07-21.png")
        await client.send_message(message.channel, embed = e)
        
    if message.content.startswith("r!okada"):
        e = discord.Embed()
        msg="***RAT ALERT***"
        e.set_image(url="https://cdn.discordapp.com/attachments/414700659884163073/456518684698083338/unknown.png")
        await client.send_message(message.channel, msg, embed = e)

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

        CEthree=["Mooncell Automaton","Runestone","Anchors Aweigh","Demon Boar","Clock Tower","Ryudoji Temple","Mana Gauge","Elixir of Love","Storch Ritter","Hermitage","Motored Cuirassier","Stuffed Lion","Lugh's Halo","Beast of Billows","Self Geass Scroll","Bronze Link Manipulator","Ath nGabla","Bygone Dream","Extremely Spicy Mapo Tofu","Jeweled Sword Zelretch","Battle of Camlann"]
        CEfour=["Iron-Willed Training","Primeval Curse","Projection","Gandr","Verdant Sound of Destruction","Gem Magecraft: Antumbra","Be Elegant","The Imaginary Element","Divine Banquet","Angel's Song","Seal Designation Enforcer","Holy Shroud of Magdalene","With One Strike","Code Cast","Knight's Dignity","Necromancy","Awakened Will","Golden Millennium Tree","Record Holder","Art of the Poisonous Snake","Art of Death","Gentle Affection","Innocent Maiden","Covering Fire"]
        CEfive=["Formal Craft","Imaginary Around","Limited/Zero Over","Kaleidoscope","Heaven's Feel","Prisma Cosmos","The Black Grail","Victor of the Moon","Another Ending","A Fragment of 2030","500 Year Obsession","Vessel of the Saint","Ideal Holy King","Volumen Hydrargyrum","Before Awakening","Origin Bullet"]
        SERVthree=["Gaius Julius Caesar","Fergus mac Róich","Gilles de Rais","Robin Hood","David","Billy the Kid","Euryale","Gilgamesh (Child)","Cú Chulainn","Diarmuid Ua Duibhne","Cú Chulainn (Prototype)","Romulus","Hektor","Medusa","Boudica","Ushiwakamaru","Alexander","Medea","Gilles de Rais","Paracelsus von Hohenheim","Charles Babbage","Mephistopheles","Geronimo","Hassan of the Hundred Personas","Henry Jekyll & Hyde","Jing Ke","Lu Bu Fengxian","Darius III","Kiyohime","Bedivere","Fuuma Kotarou"]
        SERVfour=["Artoria Pendragon (Alter)","Nero Claudius","Siegfried","Rama","Chevalier d'Eon","Emiya","Atalante","Elizabeth Báthory","Fionn mac Cumhaill","Li Shuwen","Astolfo","Anne Bonny & Mary Read","Marie Antoinette","Martha","Nursery Rhyme","Medea (Lily)","Helena Blavatsky","Thomas Edison","Stheno","Emiya (Assassin)","Carmilla","Heracles","Lancelot","Frankenstein","Beowulf","Tamamo Cat","Gawain","Lancelot (Saber)","Tristan","Artoria Pendragon (Alter) (Lancer)","Nitocris","Ibaraki-Douji"]
        SERVfive=["Artoria Pendragon","Mordred","Altera","Orion","Nikola Tesla","Arjuna","Karna","Francis Drake","Queen Medb","Tamamo-no-Mae","Zhuge Liang (Lord El-Melloi II)","Jack the Ripper","Vlad III","Florence Nightingale","Cú Chulainn (Alter)","Jeanne d'Arc","Xuanzang Sanzang","Artoria Pendragon (Lancer)","Ozymandias"]
        
        if option>10:
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

    if message.content.startswith("r!foodsummon"):      
        args = message.content.split(" ")      
        option = " ".join(args[1:])
        option=int(option)
        summonlist=[] 
        fulllist="--------------\n"
        summon=""
        maid = [["Jello","Skewer","Pancake"],["Popcorn"]]
        rare = [["Long Bao","Coffee","Sashimi","Macaron","Zongzi","Sakuramochi","Tom Yum","Taiyaki","Milk","Dorayaki","Sake","Tempura","Spicy Gluten"],["Jiuniang","Omurice","Orange Juice","Ume Ochazuke","Miso Soup","Yellow Wine"]]
        superrare=[["Tiramisu","Escargot","Hotdog","Mango Pudding","Hamburger","Steak","Tangyuan","Sanma","Napoleon Cake","Salad","Pastel de nata","Yuxiang","Sukiyaki","Brownie","Red Wine","Gyoza","Chocolate"],["Eggette"],["Pineapple Cake"]]
        ultrarare=[["Crab Long Bao","Gingerbread"],["Foie Gras","Peking Duck","B-52"],["Bamboo Rice"],["Boston Lobster","Double Scoops"]]	

        if option>6:
            await client.send_message(message.channel, "You can only summon up to 6 times at once! Don't be greedy!")
        else:
            for i in range(0,option):
                chance=random.randint(1,10000)

                if chance<=138:      
                    summon="M: "   
                    summon+=random.choice(maid[0])
                elif chance<=185 and chance>138:     
                    summon="M: "
                    summon+=random.choice(maid[1])
                elif chance<=5554 and chance>185:
                    summon="R: "    
                    summon+=random.choice(rare[0])
                elif chance<=8038 and chance>5554:
                    summon="R: "
                    summon+=random.choice(rare[1])
                elif chance<=9398 and chance>8038:
                    summon="SR: "
                    summon+=random.choice(superrare[0])
                elif chance<=9548 and chance>9398:
                    summon="SR: "
                    summon+=random.choice(superrare[1])
                elif chance<=9699 and chance>9548:
                    summon="SR: "
                    summon+=random.choice(superrare[2])
                elif chance<=9745 and chance>9699:
                    summon="**UR**: "
                    summon+=random.choice(ultrarare[0])
                elif chance<=9928 and chance>9745:
                    summon="**UR**: "
                    summon+=random.choice(ultrarare[1])
                elif chance<=9990 and chance>9928:
                    summon="**UR**: "
                    summon+=random.choice(ultrarare[2])
                elif chance<=10000 and chance>9990:
                    summon="**UR**: "
                    summon+=random.choice(ultrarare[3])

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
            
            
    if message.content.startswith("r!fuckyou"):
	    if message.author.id == "227446010094288896":
            	args = message.content.split(" ")
            	fullmsg = " ".join(args[1:])
            	fullmsg=fullmsg.split(",")
            	personid=""+fullmsg[0]
            	nickname=""+fullmsg[1]
            	person = discord.Server.get_member(personid)
            	await client.change_nickname(person, nickname)
            
            
    if message.content.startswith("r!search"):
        args = message.content.split(" ")
        url_end="%s" % (" ".join(args[1:]))
        url_end.replace(" ", "_")
        url="http://fategrandorder.wikia.com/wiki/" + url_end

        
    if message.content.startswith('r!cleanup'):
        tmp = await client.send_message(message.channel, 'Sweep sweep...')
        async for msg in client.logs_from(message.channel):
            if msg.author.id == "227446010094288896":
                await client.delete_message(msg)
        
        
        with urllib.request.urlopen(url) as response:
            html = response.read()
            wig=html.decode("ascii")
   
            if "This title wasn't found in any other Namespace" in wig:
                await client.send_message(message.channel, "Article not found! Did you spell it right?")

            else:
                await client.send_message(message.channel, url)


    if message.content.startswith("r!changegame"):
        if message.author.id == "227446010094288896" or "414626125889667072" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "A new game? I guess it'll kill some time...")
            await client.change_presence(game=discord.Game(name="%s" % (" ".join(args[1:]))))
        else:
            await client.send_message(message.channel, "Hey! I can't let you do that!!")
        
    if message.content.startswith("r!bones"):
        await client.send_message(message.channel, "Your bones are mine. :skull_crossbones: Thank you for your contribution to my programming.")
        
    if message.content.lower().startswith("dr roman"):
        answers=["It is certain.","You may rely on it.","Ask again later.","Reply hazy, try again.","My reply is no.","My sources say no."]
        reply=random.choice(answers)
        await client.send_message(message.channel, reply)
        
    if "can we get an f" in message.content.lower():
        await client.send_message(message.channel,":regional_indicator_f:")
                                  
    if "doctor play despacito" in message.content.lower():
        reply="https://www.youtube.com/watch?v=kJQP7kiw5Fk"
        await client.send_message(message.channel, reply)
        
    if "romani" in message.content.lower() and "dailies" in message.content.lower():
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441831504604037122/478989703316504586/DAILY_LIST.png")
        await client.send_message(message.channel, embed = e)
        
    if "mozart play despacito" in message.content.lower():
        reply="https://www.youtube.com/watch?v=GmtTDvNcXcU"
        await client.send_message(message.channel, reply)
        
    if "tristan play despacito" in message.content.lower():
        reply="https://youtu.be/1yuOLpNlD8c?t=13"
        await client.send_message(message.channel, reply)

            
    if message.content.startswith("r!ghost"):
        args = message.content.split(" ")
        await client.send_message(discord.Object(id='503553728016809994'), "%s" % (" ".join(args[1:])))
        
        
    if message.content.startswith("r!help"):
        if "yes" in (y.name.lower() for y in message.author.roles) or "masters" in (y.name.lower() for y in message.author.roles) or "yeehaw" in (y.name.lower() for y in message.author.roles):
            await client.send_message(message.channel, """
**General Procedure**
r!hello - *Say hello!*
r!ping - *Pong! Tests if the bot is online.*
r!8ball - *Use Romani's 8 ball!.*
r!avatar - *Snatch someone's avatar!*
r!roll [number] - *Roll a die with the specified number of sides! E.G. r!roll 20 rolls a d20, etc.*
**Fate/Bullshit**
r!respect - *F.*
r!randomfgo - *Posts a random page from the F/GO wiki.*
r!fatekin - *Chaldea Assigned Kins!*
r!classes - *For when you can't be bothered to check up class advantages in game.*
r!lancelot - *Lancelot fucks.*
r!birthday - *Happy Birthday!*
r!nasty - *Lancelot booty shorts in Rome.*
r!5star - *Can't roll any 5-stars? Pretend you did!*
r!summon [0-10] - *F/GO NA Summon Simulator! I'm not responsible for any disappointment caused...*
**Medical Personnel Only!**
r!say - *Oh, you know...*
r!changegame - *Give Romani a new game!*""")
            
        else:
            await client.send_message(message.channel, """
r!hello - *Say hello!*
r!ping - *Pong! Tests if the bot is online.*
r!8ball - *Use Romani's 8 ball!.*
r!avatar - *Snatch someone's avatar!*
r!roll [number] - *Roll a die with the specified number of sides! E.G. r!roll 20 rolls a d20, etc.*
**Fate/Bullshit**
r!randomfgo - *Posts a random page from the F/GO wiki.*
r!fatekin - *Chaldea Assigned Kins!*
r!classes - *For when you can't be bothered to check up class advantages in game.*
r!summon [0-10] - *F/GO NA Summon Simulator! I'm not responsible for any disappointment caused...*
**Medical Personnel Only!**
r!say - *Oh, you know...*
r!changegame - *Give Romani a new game!*""")

        

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
        kinlist=['http://fategrandorder.wikia.com/wiki/Mashu_Kyrielight\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nero_Claudius\n', 'http://fategrandorder.wikia.com/wiki/Siegfried\n', 'http://fategrandorder.wikia.com/wiki/Gaius_Julius_Caesar\n', 'http://fategrandorder.wikia.com/wiki/Attila\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais_(Saber)\n', "http://fategrandorder.wikia.com/wiki/Chevalier_d'Eon\n", 'http://fategrandorder.wikia.com/wiki/Okita_Souji\n', 'http://fategrandorder.wikia.com/wiki/Fergus_mac_Róich\n', 'http://fategrandorder.wikia.com/wiki/Lancelot_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/Gawain\n', 'http://fategrandorder.wikia.com/wiki/Bedivere\n', 'http://fategrandorder.wikia.com/wiki/Arthur_Pendragon\n', 'http://fategrandorder.wikia.com/wiki/Frankenstein_(Saber)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh\n', 'http://fategrandorder.wikia.com/wiki/Robin_Hood\n', 'http://fategrandorder.wikia.com/wiki/Solomon\n', 'http://fategrandorder.wikia.com/wiki/Atalanta\n', 'http://fategrandorder.wikia.com/wiki/Euryale\n', 'http://fategrandorder.wikia.com/wiki/Arash\n', 'http://fategrandorder.wikia.com/wiki/Orion\n', 'http://fategrandorder.wikia.com/wiki/David\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga\n', 'http://fategrandorder.wikia.com/wiki/Nikola_Tesla\n', 'http://fategrandorder.wikia.com/wiki/Arjuna\n', 'http://fategrandorder.wikia.com/wiki/Kid_Gil\n', 'http://fategrandorder.wikia.com/wiki/Billy_The_Kid\n', 'http://fategrandorder.wikia.com/wiki/Tristan\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)\n', 'http://fategrandorder.wikia.com/wiki/Ishtar\n', 'http://fategrandorder.wikia.com/wiki/James_Moriarty\n', 'http://fategrandorder.wikia.com/wiki/Chiron\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Prototype)\n', 'http://fategrandorder.wikia.com/wiki/Hector\n', 'http://fategrandorder.wikia.com/wiki/Scáthach\n', 'http://fategrandorder.wikia.com/wiki/Diarmuid_Ua_Duibhne\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Karna\n', 'http://fategrandorder.wikia.com/wiki/Fionn_mac_Cumhaill\n', 'http://fategrandorder.wikia.com/wiki/Brynhildr\n', 'http://fategrandorder.wikia.com/wiki/Li_Shuwen_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae_(Lancer)\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime_(Lancer)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)_(Santa_Lily)\n", 'http://fategrandorder.wikia.com/wiki/Enkidu\n', 'http://fategrandorder.wikia.com/wiki/Jaguar_Man\n', 'http://fategrandorder.wikia.com/wiki/Medusa\n', 'http://fategrandorder.wikia.com/wiki/Georgios\n', 'http://fategrandorder.wikia.com/wiki/Edward_Teach\n', 'http://fategrandorder.wikia.com/wiki/Boudica\n', 'http://fategrandorder.wikia.com/wiki/Ushiwakamaru\n', 'http://fategrandorder.wikia.com/wiki/Alexander\n', 'http://fategrandorder.wikia.com/wiki/Marie_Antoinette\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha\n', 'http://fategrandorder.wikia.com/wiki/Francis_Drake\n', 'http://fategrandorder.wikia.com/wiki/Anne_Bonny_&_Mary_Read\n', 'http://fategrandorder.wikia.com/wiki/Ozymandias\n', 'http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Santa_Alter)\n', 'http://fategrandorder.wikia.com/wiki/Astolfo\n', 'http://fategrandorder.wikia.com/wiki/Medb\n', 'http://fategrandorder.wikia.com/wiki/Iskandar\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki_(Rider)\n', 'http://fategrandorder.wikia.com/wiki/Achilles\n', 'http://fategrandorder.wikia.com/wiki/Medea\n', 'http://fategrandorder.wikia.com/wiki/Gilles_de_Rais\n', 'http://fategrandorder.wikia.com/wiki/Hans_Christian_Andersen\n', 'http://fategrandorder.wikia.com/wiki/William_Shakespeare\n', 'http://fategrandorder.wikia.com/wiki/Mephistopheles\n', 'http://fategrandorder.wikia.com/wiki/Wolfgang_Amadeus_Mozart\n', 'http://fategrandorder.wikia.com/wiki/Zhuge_Liang_(Lord_El-Melloi_II)\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Elizabeth_Bathory_(Halloween)\n', 'http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae\n', 'http://fategrandorder.wikia.com/wiki/Medea_(Lily)\n', 'http://fategrandorder.wikia.com/wiki/Nursery_Rhyme\n', 'http://fategrandorder.wikia.com/wiki/Paracelsus_von_Hohenheim\n', 'http://fategrandorder.wikia.com/wiki/Charles_Babbage\n', 'http://fategrandorder.wikia.com/wiki/Helena_Blavatsky\n', 'http://fategrandorder.wikia.com/wiki/Thomas_Edison\n', 'http://fategrandorder.wikia.com/wiki/Geronimo\n', 'http://fategrandorder.wikia.com/wiki/Irisviel_(Dress_of_Heaven)\n', 'http://fategrandorder.wikia.com/wiki/Xuanzang\n', 'http://fategrandorder.wikia.com/wiki/Nitocris\n', 'http://fategrandorder.wikia.com/wiki/Leonardo_Da_Vinci\n', 'http://fategrandorder.wikia.com/wiki/Gilgamesh_(Caster)\n', 'http://fategrandorder.wikia.com/wiki/Merlin\n', 'http://fategrandorder.wikia.com/wiki/Avicebron\n', 'http://fategrandorder.wikia.com/wiki/Sieg\n', 'http://fategrandorder.wikia.com/wiki/Anastasia_Nikolaevna_Romanova\n', 'http://fategrandorder.wikia.com/wiki/Cursed_Arm_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Stheno\n', 'http://fategrandorder.wikia.com/wiki/Jing_Ke\n', 'http://fategrandorder.wikia.com/wiki/Charles-Henri_Sanson\n', 'http://fategrandorder.wikia.com/wiki/The_Phantom_of_the_Opera\n', 'http://fategrandorder.wikia.com/wiki/Mata_Hari\n', 'http://fategrandorder.wikia.com/wiki/Carmilla\n', 'http://fategrandorder.wikia.com/wiki/Jack_the_Ripper\n', 'http://fategrandorder.wikia.com/wiki/Henry_Jekyll_&_Hyde\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X\n', 'http://fategrandorder.wikia.com/wiki/Ryougi_Shiki_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/EMIYA_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Hundred-Faced_Hassan\n', 'http://fategrandorder.wikia.com/wiki/Fuuma_Kotarou\n', 'http://fategrandorder.wikia.com/wiki/Shuten_Douji\n', 'http://fategrandorder.wikia.com/wiki/Hassan_of_Serenity\n', 'http://fategrandorder.wikia.com/wiki/Cleopatra\n', 'http://fategrandorder.wikia.com/wiki/Nitocris_(Assassin)\n', 'http://fategrandorder.wikia.com/wiki/Semiramis\n', 'http://fategrandorder.wikia.com/wiki/Heracles\n', 'http://fategrandorder.wikia.com/wiki/Lancelot\n', 'http://fategrandorder.wikia.com/wiki/Lu_Bu\n', 'http://fategrandorder.wikia.com/wiki/Spartacus\n', 'http://fategrandorder.wikia.com/wiki/Sakata_Kintoki\n', 'http://fategrandorder.wikia.com/wiki/Vlad_III\n', 'http://fategrandorder.wikia.com/wiki/Asterios\n', 'http://fategrandorder.wikia.com/wiki/Caligula\n', 'http://fategrandorder.wikia.com/wiki/Darius_III\n', 'http://fategrandorder.wikia.com/wiki/Kiyohime\n', 'http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Paul_Bunyan\n', 'http://fategrandorder.wikia.com/wiki/Atalanta_(Alter)\n', 'http://fategrandorder.wikia.com/wiki/Oda_Nobunaga_(Berserker)\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc\n", 'http://fategrandorder.wikia.com/wiki/Amakusa_Shirou\n', 'http://fategrandorder.wikia.com/wiki/Saint_Martha_(Ruler)\n', 'http://fategrandorder.wikia.com/wiki/Sherlock_Holmes\n', 'http://fategrandorder.wikia.com/wiki/Edmond_Dantes\n', "http://fategrandorder.wikia.com/wiki/Jeanne_d'Arc_(Alter)\n", 'http://fategrandorder.wikia.com/wiki/Angra_Mainyu\n', 'http://fategrandorder.wikia.com/wiki/Gorgon\n', 'http://fategrandorder.wikia.com/wiki/Antonio_Salieri\n', 'http://fategrandorder.wikia.com/wiki/Hessian_Lobo\n', 'http://fategrandorder.wikia.com/wiki/BB\n', 'http://fategrandorder.wikia.com/wiki/Passionlip\n', 'http://fategrandorder.wikia.com/wiki/Sessyoin_Kiara\n', 'http://fategrandorder.wikia.com/wiki/Abigail_Williams\n', 'http://fategrandorder.wikia.com/wiki/Katsushika_Hokusai','http://fategrandorder.wikia.com/wiki/Sigurd\n','http://fategrandorder.wikia.com/wiki/Medb_(Saber)\n','http://fategrandorder.wikia.com/wiki/Napoleon\n','http://fategrandorder.wikia.com/wiki/Jeanne_d%27Arc_(Archer)\n','http://fategrandorder.wikia.com/wiki/Parvati\n','http://fategrandorder.wikia.com/wiki/Nezha\n','http://fategrandorder.wikia.com/wiki/Ereshkigal\n','http://fategrandorder.wikia.com/wiki/Valkyrie\n','http://fategrandorder.wikia.com/wiki/Ibaraki_D%C5%8Dji_(Lancer)\n','http://fategrandorder.wikia.com/wiki/Sakamoto_Ry%C5%8Dma\n','http://fategrandorder.wikia.com/wiki/Sc%C3%A1thach-Ska%C3%B0i\n','http://fategrandorder.wikia.com/wiki/Okada_Iz%C5%8D\n','http://fategrandorder.wikia.com/wiki/Ushiwakamaru_(Assassin)\n','http://fategrandorder.wikia.com/wiki/Jeanne_d%27Arc_(Berserker_Alter)\n','http://fategrandorder.wikia.com/wiki/Okita_S%C5%8Dji_(Alter)\n','http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Foreigner)\n']
        kin=random.choice(kinlist)
        msg = "{0.author.mention}".format(message)
        await client.send_message(message.channel, msg + " Your Chaldea assigned kin is... %s" % kin)
        
    if message.content.startswith("r!hypmickin"):
        kinlist=["http://hypnosis-mic.wikia.com/wiki/Ichiro_Yamada","http://hypnosis-mic.wikia.com/wiki/Samatoki_Aohitsugi","http://hypnosis-mic.wikia.com/wiki/Ramuda_Amemura","http://hypnosis-mic.wikia.com/wiki/Jakurai_Jinguji","http://hypnosis-mic.wikia.com/wiki/Jiro_Yamada","http://hypnosis-mic.wikia.com/wiki/Rio_Mason_Busujima","http://hypnosis-mic.wikia.com/wiki/Gentaro_Yumeno","http://hypnosis-mic.wikia.com/wiki/Hifumi_Izanami","http://hypnosis-mic.wikia.com/wiki/Saburo_Yamada","http://hypnosis-mic.wikia.com/wiki/Jyuto_Iruma","http://hypnosis-mic.wikia.com/wiki/Dice_Arisugawa","http://hypnosis-mic.wikia.com/wiki/Doppo_Kannonzaka"]
        kin=random.choice(kinlist)
        msg = "{0.author.mention}".format(message)
        await client.send_message(message.channel, msg + " Your Chaldea assigned kin is... %s" % kin)
            
    if message.content.startswith("r!foodkin"):
        foodlist=['https://food-fantasy.wikia.com/wiki/B-52', 'https://food-fantasy.wikia.com/wiki/Bamboo_Rice', 'https://food-fantasy.wikia.com/wiki/Boston_Lobster', 'https://food-fantasy.wikia.com/wiki/Canele', 'https://food-fantasy.wikia.com/wiki/Crab_Longbao', 'https://food-fantasy.wikia.com/wiki/Double_Scoop', 'https://food-fantasy.wikia.com/wiki/Foie_Gras', 'https://food-fantasy.wikia.com/wiki/Gingerbread', 'https://food-fantasy.wikia.com/wiki/Peking_Duck', 'https://food-fantasy.wikia.com/wiki/Raindrop_Cake', 'https://food-fantasy.wikia.com/wiki/Toso', 'http://food-fantasy.wikia.com/wiki/Cloud_Tea', 'https://food-fantasy.wikia.com/wiki/Beggar%27s_Chicken', 'https://food-fantasy.wikia.com/wiki/Black_Tea', 'https://food-fantasy.wikia.com/wiki/Brownie', 'https://food-fantasy.wikia.com/wiki/Chocolate', 'https://food-fantasy.wikia.com/wiki/Eggette', 'https://food-fantasy.wikia.com/wiki/Escargot', 'https://food-fantasy.wikia.com/wiki/Matcha_Rice', 'https://food-fantasy.wikia.com/wiki/Gyoza', 'https://food-fantasy.wikia.com/wiki/Hamburger', 'https://food-fantasy.wikia.com/wiki/Hotdog', 'https://food-fantasy.wikia.com/wiki/Laba_Congee', 'https://food-fantasy.wikia.com/wiki/Mango_Puding', 'https://food-fantasy.wikia.com/wiki/Milk_Tea', 'https://food-fantasy.wikia.com/wiki/Moon_Cake', 'https://food-fantasy.wikia.com/wiki/Napoleon_Cake', 'https://food-fantasy.wikia.com/wiki/Pastal_de_Nata', 'https://food-fantasy.wikia.com/wiki/Pineapple_Cake', 'https://food-fantasy.wikia.com/wiki/Red_Wine', 'https://food-fantasy.wikia.com/wiki/Salad', 'https://food-fantasy.wikia.com/wiki/Salty_Tofu', 'https://food-fantasy.wikia.com/wiki/Sanma_Shioyaki', 'https://food-fantasy.wikia.com/wiki/Spaghetti', 'https://food-fantasy.wikia.com/wiki/Steak', 'https://food-fantasy.wikia.com/wiki/Sukiyaki', 'https://food-fantasy.wikia.com/wiki/Sushi', 'https://food-fantasy.wikia.com/wiki/Sweet_Tofu', 'https://food-fantasy.wikia.com/wiki/Tangyuan', 'https://food-fantasy.wikia.com/wiki/Tiramisu', 'https://food-fantasy.wikia.com/wiki/Tortoise_Jelly', 'https://food-fantasy.wikia.com/wiki/Vodka', 'https://food-fantasy.wikia.com/wiki/Wonton', 'https://food-fantasy.wikia.com/wiki/Yogurt', 'https://food-fantasy.wikia.com/wiki/Yunnan_Noodles', 'https://food-fantasy.wikia.com/wiki/Yuxiang', 'https://food-fantasy.wikia.com/wiki/Coffee', 'https://food-fantasy.wikia.com/wiki/Cola', 'https://food-fantasy.wikia.com/wiki/Shrimp', 'https://food-fantasy.wikia.com/wiki/Crepe', 'https://food-fantasy.wikia.com/wiki/Dorayaki', 'https://food-fantasy.wikia.com/wiki/Jiuniang', 'https://food-fantasy.wikia.com/wiki/Long_Bao', 'https://food-fantasy.wikia.com/wiki/Macaroon', 'https://food-fantasy.wikia.com/wiki/Milk', 'https://food-fantasy.wikia.com/wiki/Miso_Soup', 'https://food-fantasy.wikia.com/wiki/Nasi_Lemak', 'https://food-fantasy.wikia.com/wiki/Omurice', 'https://food-fantasy.wikia.com/wiki/Orange_Juice', 'https://food-fantasy.wikia.com/wiki/Plum_Juice', 'https://food-fantasy.wikia.com/wiki/Sake', 'https://food-fantasy.wikia.com/wiki/Sakuramochi', 'https://food-fantasy.wikia.com/wiki/Sashimi', 'https://food-fantasy.wikia.com/wiki/Spicy_Gluten', 'https://food-fantasy.wikia.com/wiki/Taiyaki', 'https://food-fantasy.wikia.com/wiki/Tempura', 'https://food-fantasy.wikia.com/wiki/Tom_Yum', 'https://food-fantasy.wikia.com/wiki/Ume_Ochazuke', 'https://food-fantasy.wikia.com/wiki/Yellow_Wine', 'https://food-fantasy.wikia.com/wiki/Zongzi', 'https://food-fantasy.wikia.com/wiki/Hawthorne_Ball', 'https://food-fantasy.wikia.com/wiki/Jello', 'https://food-fantasy.wikia.com/wiki/Pancake', 'https://food-fantasy.wikia.com/wiki/Popcorn', 'https://food-fantasy.wikia.com/wiki/Pudding', 'https://food-fantasy.wikia.com/wiki/Sandwich', 'https://food-fantasy.wikia.com/wiki/Skewer', 'https://food-fantasy.wikia.com/wiki/Strawberry_Daifuku', 'https://food-fantasy.wikia.com/wiki/Toast','http://food-fantasy.wikia.com/wiki/Amazake','http://food-fantasy.wikia.com/wiki/Conchi','http://food-fantasy.wikia.com/wiki/Garuda','http://food-fantasy.wikia.com/wiki/Nekomata','http://food-fantasy.wikia.com/wiki/Prajna','http://food-fantasy.wikia.com/wiki/Specter','http://food-fantasy.wikia.com/wiki/Aizen','http://food-fantasy.wikia.com/wiki/Inugami','http://food-fantasy.wikia.com/wiki/Orochi','http://food-fantasy.wikia.com/wiki/Queen_Conch','http://food-fantasy.wikia.com/wiki/Spectra','http://food-fantasy.wikia.com/wiki/Thundaruda','http://food-fantasy.wikia.com/wiki/Uke_Mochi'] 
        kin=random.choice(foodlist)
        msg = "{0.author.mention}".format(message)
        await client.send_message(message.channel, msg + " Your Chaldea assigned kin is... %s" % kin)
        
    if message.content.startswith("r!birthday"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441190970403323914/441574720761233408/Cy_rRxlUcAAYiC5.png")
        await client.send_message(message.channel, embed = e)

             
    if message.content.startswith("r!nasty"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/439040144914251776/441676875136237579/ARE_YOU_LANCELOT.png")
        await client.send_message(message.channel, embed = e)
        
    if message.content.startswith("r!sho"):
        e = discord.Embed()
        sholist=["https://cdn.discordapp.com/attachments/505883233523728384/505883360233521173/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883522070872064/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883596595134465/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883638567665684/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883688043544597/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883738685571072/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883783598309379/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883837302177798/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505883913680453633/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505884015740452864/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505884192467320842/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505884292602265601/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/505884337955143690/unknown.png","https://cdn.discordapp.com/attachments/505883233523728384/506938194697256970/HIDESHO.png","https://cdn.discordapp.com/attachments/505883233523728384/505885455170928647/demon_sho.png","https://cdn.discordapp.com/attachments/505883233523728384/505885605360697344/WATANABE.png"]
        sho=random.choice(sholist)
        e.set_image(url=sho)
        await client.send_message(message.channel, embed = e)

        
    if message.content.startswith("r!5star"):
        ssrs=["http://fategrandorder.wikia.com/wiki/Shuten_Douji","http://fategrandorder.wikia.com/wiki/Minamoto_no_Yorimitsu","http://fategrandorder.wikia.com/wiki/Jeanne_d%27Arc_(Alter)","http://fategrandorder.wikia.com/wiki/Sc%C3%A1thach","http://fategrandorder.wikia.com/wiki/Sherlock_Holmes","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon","http://fategrandorder.wikia.com/wiki/Jeanne_d%27Arc","http://fategrandorder.wikia.com/wiki/Sakata_Kintoki","http://fategrandorder.wikia.com/wiki/Merlin","http://fategrandorder.wikia.com/wiki/Gilgamesh","http://fategrandorder.wikia.com/wiki/Mordred","http://fategrandorder.wikia.com/wiki/Miyamoto_Musashi","http://fategrandorder.wikia.com/wiki/%22The_Old_Man_of_the_Mountain%22","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Lancer)","http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae","http://fategrandorder.wikia.com/wiki/Achilles","http://fategrandorder.wikia.com/wiki/Zhuge_Liang_(Lord_El-Melloi_II)","http://fategrandorder.wikia.com/wiki/Cu_Chulainn_(Alter)","http://fategrandorder.wikia.com/wiki/Nightingale","http://fategrandorder.wikia.com/wiki/Ozymandias","http://fategrandorder.wikia.com/wiki/Anastasia_Nikolaevna_Romanova","http://fategrandorder.wikia.com/wiki/Arthur_Pendragon_(Prototype)","http://fategrandorder.wikia.com/wiki/Brynhildr","http://fategrandorder.wikia.com/wiki/Xuanzang","http://fategrandorder.wikia.com/wiki/Jack_the_Ripper","http://fategrandorder.wikia.com/wiki/Okita_Souji","http://fategrandorder.wikia.com/wiki/Katsushika_Hokusai","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Archer)","http://fategrandorder.wikia.com/wiki/Scheherazade","http://fategrandorder.wikia.com/wiki/Karna","http://fategrandorder.wikia.com/wiki/Sessyoin_Kiara","http://fategrandorder.wikia.com/wiki/Medb","http://fategrandorder.wikia.com/wiki/Artoria_Pendragon_(Rider_Alter)","http://fategrandorder.wikia.com/wiki/Attila","http://fategrandorder.wikia.com/wiki/Enkidu","http://fategrandorder.wikia.com/wiki/Tamamo_no_Mae_(Lancer)","http://fategrandorder.wikia.com/wiki/Orion","http://fategrandorder.wikia.com/wiki/Semiramis","http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X_(Alter)","http://fategrandorder.wikia.com/wiki/Illyasviel_von_Einzbern","http://fategrandorder.wikia.com/wiki/Ivan_the_Terrible","http://fategrandorder.wikia.com/wiki/Nero_Claudius_(Bride)","http://fategrandorder.wikia.com/wiki/Mysterious_Heroine_X","http://fategrandorder.wikia.com/wiki/Edmond_Dantes","http://fategrandorder.wikia.com/wiki/Osakabehime","http://fategrandorder.wikia.com/wiki/Iskandar","http://fategrandorder.wikia.com/wiki/Francis_Drake","http://fategrandorder.wikia.com/wiki/Amakusa_Shirou","http://fategrandorder.wikia.com/wiki/James_Moriarty","http://fategrandorder.wikia.com/wiki/Leonardo_Da_Vinci","http://fategrandorder.wikia.com/wiki/Arjuna","http://fategrandorder.wikia.com/wiki/Quetzalcoatl","http://fategrandorder.wikia.com/wiki/Nero_Claudius_(Caster)","http://fategrandorder.wikia.com/wiki/Vlad_III","http://fategrandorder.wikia.com/wiki/Meltlilith","http://fategrandorder.wikia.com/wiki/Cleopatra","http://fategrandorder.wikia.com/wiki/Ryougi_Shiki_(Saber)","http://fategrandorder.wikia.com/wiki/Hijikata_Toshizou","http://fategrandorder.wikia.com/wiki/Nikola_Tesla","http://fategrandorder.wikia.com/wiki/Sc%C3%A1thach-Ska%C3%B0i","http://fategrandorder.wikia.com/wiki/Sigurd","http://fategrandorder.wikia.com/wiki/Okita_S%C5%8Dji_(Alter)","http://fategrandorder.wikia.com/wiki/Ereshkigal","http://fategrandorder.wikia.com/wiki/B_B_(Summer)","http://fategrandorder.wikia.com/wiki/Napoleon"]
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
            
    if message.content.startswith("r!datetime"):
        year = "Current year: "+ datetime.date.today().strftime("%Y") + "\n"
        month = "Month of year: "+ datetime.date.today().strftime("%B") + "\n"
        week_number = "Week number of the year: "+ datetime.date.today().strftime("%W") + "\n"
        weekday = "Weekday of the week: "+ datetime.date.today().strftime("%w") + "\n"
        dayyear = "Day of year: "+ datetime.date.today().strftime("%j") + "\n"
        daymonth = "Day of the month : "+ datetime.date.today().strftime("%d") + "\n"
        dayweek = "Day of week: "+ datetime.date.today().strftime("%A") + "\n"
        full = year + month + week_number + weekday + dayyear + daymonth + dayweek
        await client.send_message(message.channel, full)
        
        
    if message.content.startswith("r!daily"):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/441831504604037122/478989703316504586/DAILY_LIST.png")
        await client.send_message(message.channel, embed = e)
            
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
    print("Ready!")

token=os.environ["BOT_TOKEN"]
client.run(token)
