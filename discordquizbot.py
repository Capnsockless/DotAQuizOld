import discord
import os
import sys, traceback
import itertools
import json
from discord.ext import commands

os.chdir(r"D:\Discordbot\DotaQuizbot")

def open_json(jsonfile):
	with open(jsonfile, "r") as fp:
		return json.load(fp)	#openfunc for jsonfiles

def save_json(jsonfile, name):	#savefunc for jsonfiles
	with open(jsonfile, "w") as fp:
		json.dump(name, fp)

def strip_str(text):        #function to remove punctuations spaces from string and make it lowercase
    punctuations = ''' !-;:`'"\,/_?'''
    text2 = ""
    for char in text:
        if char not in punctuations:
            text2 = text2 + char
    return text2.lower().replace("the", "")

async def find_channel(guild):      #find the first usable channel for intro message
    for chnnl in guild.text_channels:
        if not chnnl.permissions_for(guild.me).send_messages:
            continue
        return chnnl

#Detailed command infos for 322 help command
command_dinfos = {"quiz":"A single question which gives 14-18 gold with 22 seconds of time to answer.",
"blitz":"""50 seconds of rapid questions which start after a short delay, each question also has a limited time to answer which depends on the size of the question. Blitz is high-risk high-reward in terms of gold, you get more gold according to how many correct answers you have, wrong answers and late answers take away gold but you can skip a question by typing "skip" in chat during the blitz to lose less time and gold.""",
"shopquiz":"""Endlessly sends icons of a DotA2 items until you run out of the 3 lives you get, a life is lost whenever the player types in an incorrect item or is too late to answer(you have 20 seconds to type in each item), you must type in the items required to assemble the shown item **One by One** in no particular order, you can message "skip" to skip an item and "stop" to stop the quiz entirely at any point. Gives bonus gold according to the amount of correct answers.""",
"endless":"""Endlessly sends questions, item icons and ability icons randomly, you are given 5 lives. You're given 14 seconds to type in each answer or item. Gives bonus gold according to the amount of current correct answers. You can type in "skip" to skip a question and "stop" to stop the quiz entirely any time. **Aghanim's Scepter is required to use this command**""",
"iconquiz":"""Endlessly sends DotA 2 ability icons that must be named, you are given 3 lives, you earn more gold the more icons you name correctly. You type "skip" to jump to the next icon to lose less hp and type stop to "stop" the quiz entirely.""",
"duel":"Usage: 322 duel @User <gold amount> | Both duellers must have enough gold to start a duel. After a short delay, sends 15 questions(one by one) which can be answered by both duel participants, first to answer gets +1 point, if the first answer to be sent is incorrect the challenger will lose 1 point. After all 15 questions are answered the winner will get 200 less gold than the wager while the loser loses the full amount of gold. Minimum wager is 300 gold while the maximum is 1000 unless the initiator has a Pirate Hat.", "audioquiz":"""You must be in an accesible voice channel to use this command. Plays sound effects from the game and must be answered in the chat by typing in the name of the item or spell that makes the sound. You can use "skip" to skip a sound or "stop" to disconnect the bot entirely. Each correct answer gives additional 3.2 seconds and every next answer gives more gold.""",
"freeforall":"Asks 25(35 if initiator has a Necronomicon) questions in a channel which anyone can answer. The prize pool increases exponentially according to the amount of participants who gave at least one correct answer and how many questions were answered correctly in total. Players get points for correct answers and lose a point for a wrong answer. The prize pool is then distributed among the top 5 players as 60%, 20%, 10%, 5%, 5% of the total prize pool.",
"buy":"Buy one of the items from the store to improve some stats for the quiz commands.", "sell":"Sell an item you already own for half its price.", "store":"Check available items, their prices and what they do.", "inventory":"Check which items you have in your inventory.", "gold":"Check the amount of gold you currently have.", "oversight":"The biggest oversight.", "hohoohahaa":"The Shifting Snow.", "newpatch":"Icefrog releases a new patch.",
"givecheese":"Usage: 322 givecheese @User <cheese amount> Give another user any amount of cheese.", "cheeseboard":"Check the top 10 users who have the most cheese. Users in different servers have their names hidden but the cheese amount is visible.", "missedhook":"Check why you missed your hook.", "serverinvite":"Get a server invite to our discord server!"}

#Help command
class MyHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__(command_attrs = {'help':'Shows help about the bot or a command'})
        self.no_category = "Information"
        self.sort_commands = False

    async def send_command_help(self, command):         #gets the full detailed info of a command
        cmd_info = command_dinfos[strip_str(str(command))]
        await self.get_destination().send(f"``{cmd_info}``")

intents = discord.Intents(messages=True, members=True, guilds=True, typing=False, presences=False, voice_states=True)
bot = commands.Bot(command_prefix='322 ', case_insensitive=True, help_command=MyHelpCommand(), intents=intents)


startcogs = ["cogs.quizes", "cogs.miscellaneous", "cogs.store"]     #list of cogs to load

if __name__ == '__main__':              #loading the cogs from the directory ./cogs
    for extension in startcogs:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Try "322 help"'))
    print('online')

@bot.event
async def on_guild_join(guild):         #sends message in the first usable channel when joining a new server
    channel = await find_channel(guild)
    await channel.send("```Hi, this is DotAQuiz, a bot that allows you to learn many details of DotA you might've never known before. You can test your knowledge of the game with the quiz commands: 322 quiz | 322 blitz | 322 shopquiz | 322 audioquiz | 322 iconquiz | 322 endless (Note that most of these commands can be quite spammy so I recommed you use a channel dedicated to spam for these commands.) and you can challenge others with  322 duel  You can use the gold you earn with these commands to buy items with | 322 buy | that can help improve some stats in these commands. Don't forget to do 322 help and 322 help [command] to see all the information that might interest you. If you find any factual mistakes, typos and want to notify us to fix it or just want to give feedback for the bot do 322 serverinvite for an invite to our server.```")

@bot.event
async def on_guild_remove(guild):       #removes server from rngfix.json if bot gets removed
    rng = open_json("rngfix.json")
    id = str(guild.id)
    if id in rng.keys():
        rng.pop(id)
        save_json("rngfix.json", rng)

@bot.command(brief = "Bonus info about the bot and an invite to our discord server.")
async def serverinvite(ctx):             #sends bot information and server invite link to the server
    user = bot.get_user(ctx.author.id)
    try:
        await user.send("This bot revolves around DotA 2, all the images/icons are taken from DotA 2(except the profile picture, which is based on the DotA 2 logo), this bot was made just for fun, it doesn't serve any real purpose so it's not meant to be professional. The bot isn't always online since I simply host it on my pc and I don't keep it turned on all day. You can use Quiz commands to gain money and buy items to gain some buffs from them, I recommend you use a channel dedicated to spam since some of these commands can be spammy. The questions are all in english and only accept English versions of DotA words, names and terms. Also note that many of the questions used by this bot were written without factchecking so you might find some incorrect information, typos and grammatical errors, if you wish to report these mistakes, just want to give feedback and suggestions or wish to see updates you can do so on this discord server:  https://discord.gg/nhBvdqV ")
        await ctx.send("Info has been sent to you.")
    except Exception:
        await ctx.send("Info can't be sent to you in direct messages(Due to your account privacy settings).")

#event for wrong "322 cmnd"
@bot.event              #ignore and raise certain errors
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("""That command doesn't exist, try "**322 help**" to see the existing commands.""")
    elif isinstance(error, (commands.CommandOnCooldown, commands.MissingRequiredArgument, commands.BadArgument)):
        pass
    else:
        raise error


bot.run(TOKEN)
