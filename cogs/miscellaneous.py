import random
import discord
import json
import os
from discord.ext import commands

os.chdir(r"D:\Discordbot\DotaQuizbot")

def open_json(jsonfile):
    with open(jsonfile, "r") as fp:     #load the users.json file
        return json.load(fp)        #openfunc for jsonfiles

def save_json(jsonfile, name):      #savefunc for jsonfiles
    with open(jsonfile, "w") as fp:
        json.dump(name, fp)


class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def oversight(self, ctx):
        await ctx.send("The biggest oversight with Dark Willow is that she's unbelievably sexy. I can't go on a hour of my day without thinking about plowing that tight wooden ass. I'd kill a man in cold blood just to spend a minute with her crotch grinding against my throbbing manhood as she whispers terribly dirty things to me in her geographically ambiguous accent.")

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

    @commands.command(brief = "See the top 10 cheese collectors.")
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
                    basetext = basetext + str(n+1) + ")[Hidden]" + " "*35 + str(sortvalues[n])
                else:
                    basetext = basetext + str(n+1) + ")[Hidden]" + " "*36 + str(sortvalues[n]) + "\n"
        await ctx.send(f"```{basetext}```")

    @commands.command()
    async def missedhook(self, ctx):
        await ctx.send(f"""You missed your hook "because" the ping is {round(self.bot.latency * 1000)}ms""")

    async def cog_command_error(self, ctx, error):
        raise error

def setup(bot):
    bot.add_cog(Miscellaneous(bot))
