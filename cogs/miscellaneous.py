import random
import discord
import json
import os
from discord.ext import commands

os.chdir(r"D:\Discordbot\DotaQuizbot")

#Copypastas for 322 copypasta
copypastas = {"diretide":"༼ つ ◕_◕ ༽つ GIVE DIRETIDE",
"oversight":"The biggest oversight with Dark Willow is that she's unbelievably sexy. I can't go on a hour of my day without thinking about plowing that tight wooden ass. I'd kill a man in cold blood just to spend a minute with her crotch grinding against my throbbing manhood as she whispers terribly dirty things to me in her geographically ambiguous accent.",
"heyrtz":"ＨＥＹ　ＲＴＺ，　Ｉ’Ｍ　ＴＲＹＩＮＧ　ＴＯ　ＬＥＡＲＮ　ＴＯ　ＰＬＡＹ　ＲＩＫＩ．　Ｉ　ＪＵＳＴ　ＨＡＶＥ　Ａ　ＱＵＥＳＴＩＯＮ　ＡＢＯＵＴ　ＴＨＥ　ＳＫＩＬＬ　ＢＵＩＬＤ：　ＳＨＯＵＬＤ　Ｉ　ＭＡＸ　ＢＡＣＫＳＴＡＢ　ＬＩＫＥ　ＹＯＵ　ＢＡＣＫＳＴＡＢＢＥＤ　ＥＧ，　ＳＭＯＫＥＳＣＲＥＥＮ　ＳＯ　ＴＨＥＲＥ＇Ｓ    ３２５  ＡＯＥ  ＤＲＡＭＡ  ＡＲＯＵＮＤ  ＹＯＵ， \
　ＯＲ  ＢＬＩＮＫ  ＳＴＲＩＫＥ  ＬＩＫＥ  ＴＨＥ  ＷＡＹ  ＹＯＵ  ＢＬＩＮＫＥＤ  ＢＡＣＫ  ＴＯ  ＥＧ  ＡＦＴＥＲ  ＴＨＥＹ  ＨＡＤ  ＷＯＮ  ＴＩ",
"artour":"""My name Artour Babaev. Sorry bad englandsky. I grow up in small farm to have make potatoes. Father say "Arthour, potato harvest is bad. Need you to have play professional DOTO2 in Amerikanski for make money for head-scarf for babushka." I bring honor to komrade and babushka. Plz no copy pasteschniko.""",
"puppey":"The scariest moment in my time with secret was during our practices, when Puppey would walk around with a machete and talk about how he always wanted to see what the inside of a human looked like. He said he had experimented on animals before and he wanted to go for the real thing. I believed him.",
"averageplay":"ＥＨ， ＡＶＥＲＡＧＥ ＰＬＡＹ． ＯＢＶＩＯＵＳ ＱＯＰ ＷＯＵＬＤ ＢＬＩＮＫ， ＳＯ ＩＴ ＷＯＵＬＤ ＢＥ ＳＴＵＰＩＤ ＴＯ ＮＯＴ ＢＬＩＮＫ ＴＯ ＴＨＡＴ ＥＸＡＣＴ ＳＰＯＴ ＡＮＤ ＥＶＥＮ ＦＡＫＥ ＹＯＵＲ ＵＬＴ Ａ ＬＩＴＴＬＥ ＦＩＲＳＴ ＴＯ ＭＡＫＥ ＨＥＲ ＴＨＩＮＫ ＹＯＵ ＷＥＲＥＮ＇Ｔ ＧＯＩＮＧ ＴＯ ＤＯ ＩＴ！， ５／１０",
"report":"Good Jokes mate real funny see u at FUCK YOUJ", "sodium":"""Sodium, atomic number 11, was first isolated by Peter "ppd" Dager in 1807. A chemical component of salt, he named it Na in honor of the saltiest region on earth, North America.""",
"juggernaut":"I'M THE JUGGERNAUT, BITCH!", "flower":"SPAM 🌻 THIS 🌻 FLOWER 🌻 TO 🌻 GIVE 🌻 NOTAIL 🌻 POWER 🌻"}

copypastainfo = {"diretide":"Give diretide volvo.", "oversight":"The biggest oversight.", "heyrtz":"Riki skillbuild.", "artour":"Story of Artour Babaev.",
"puppey":"Fight me.", "averageplay":"Miracle-'s average play.", "report":"Nice jokes mate.", "sodium":"Information about Sodium - Na.", "juggernaut":"A famous quote of the hero.",
"flower":"Give N0tail power."}

pastas = []
for key, value in copypastainfo.items():
    pastas.append(key + "   ––––	" + value)
pastalist = discord.Embed( colour=0x9b59b6)
pastalist.add_field(name="Copypastas:", value="\n".join(pastas), inline=False)

def open_json(jsonfile):
    with open(jsonfile, "r") as fp:     #load the users.json file
        return json.load(fp)        #openfunc for jsonfiles

def save_json(jsonfile, name):      #savefunc for jsonfiles
    with open(jsonfile, "w") as fp:
        json.dump(name, fp)

def strip_str(text):		#function to remove punctuations, spaces and "the" from string and make it lowercase,
	punctuations = ''' !-;:`'"\,/_?'''			# in order to compare bot answers and user replies
	text2 = ""
	text.replace("the ", "")
	for char in text:
		if char not in punctuations:
			text2 = text2 + char
	return text2.lower()

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Get a copy of a DotA copypasta.", aliases = ["pasta"])
    async def copypasta(self, ctx, pasta):
        if strip_str(pasta) in list(copypastas.keys()):
            await ctx.send(copypastas[strip_str(pasta)])
        else:
            await ctx.send("That is not one of the available copypastas: ", embed=pastalist)

    @commands.command()
    async def hohoohahaa(self, ctx):
        await ctx.send(file=discord.File('snoper.png'))

    @commands.command()
    async def newpatch(self, ctx):
        rng = open_json("rngfix.json")
        id = str(ctx.guild.id)
        if id not in rng.keys():
            rng[id] = {"questnumbers":"[]", "shopkeepnumbers":"[]", "iconquiznumbers":"[]", "audioquiznumbers":"[]", "vacuumcd":16}
        rng[id]["vacuumcd"] += random.randint(1, 3)
        await ctx.send(f"""Vacuum cooldown has been increased, it is now **{rng[id]["vacuumcd"]}** seconds long.""")
        save_json("rngfix.json", rng)

    @commands.command(brief = "See the top 10 cheese collectors.", aliases = ["board"])
    async def cheeseboard(self, ctx):
        users = open_json("users.json")
        onlycheese = {k: v["cheese"] for k, v in users.items()}         #create a dict of user ids and their cheese
        sort = {k: v for k, v in sorted(onlycheese.items(), key=lambda item: item[1], reverse=True)}      #sort the dictionary according to cheese amounts
        sortkeys, sortvalues = list(sort.keys()), list(sort.values())       #obtain lists of the keys and values for later use
        basetext = "Collector:                         Cheese amount:\n"
        for n in range(0, 10):
            user = ctx.guild.get_member(int(sortkeys[n]))
            if type(user) == discord.Member:        #if user is in the server it will display the name
                multiplier = 44 - len(user.display_name)
                if n == 9:          #if it's the 10th user it will be less indented to be in line with other users
                    basetext = basetext + str(n+1) + ")" + user.display_name + " "*(multiplier-1) + str(sortvalues[n])
                else:
                    basetext = basetext + str(n+1) + ")" + user.display_name + " "*multiplier + str(sortvalues[n]) + "\n"
            else:           #otherwise it will just say "hidden" instead
                if n == 9:        #if it's the 10th user it will be less indented to be in line with other users
                    basetext = basetext + str(n+1) + ")[Hidden User]" + " "*30 + str(sortvalues[n])
                else:
                    basetext = basetext + str(n+1) + ")[Hidden User]" + " "*31 + str(sortvalues[n]) + "\n"
        await ctx.send(f"```{basetext}```")

    @commands.command()
    async def missedhook(self, ctx):
        await ctx.send(f"""You missed your hook "because" the ping is {round(self.bot.latency * 1000)}ms""")

    @copypasta.error
    async def copypastaerror(self, ctx, error):
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f"""You need to specify which copypasta you want like so: 322 copypasta <pasta> out of one of these copypastas:\n```{pastalist}```""")

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            pass
        else:
            raise error

def setup(bot):
    bot.add_cog(Miscellaneous(bot))
