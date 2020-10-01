# DotAQuiz
A discord bot made with python, using the discord.py package.

This is a project I started in 2020 May to learn more about python, so it's probably not the best in terms of efficiency.
All of the images and sound effects I use in the bot are from DotA2, the bot has commands such as quiz, blitz, iconquiz shopquiz and endless which
allow users to make money which they can spend on the store commands or use to duel others to earn more gold,
items they can purchase enhance how they get to use the quiz commands mentioned above.

https://discord.gg/nhBvdqV here's the discord server where users can hear bot updates, give feedback and report mistakes and typos
that might be present in cogs.quizes.py questdict dictionary.

Images and audio used for regular quiz questions, for shopquiz, iconquiz annd audioquiz are stored in seperate folders inside the main folder (next to discordquizbot.py)
I didn't include these files here since they are over 900 in total. Folders are named: "quizimages", "shopkeepimages", "soundquizaudio" and "iconquizimages",
You can see these folders being called in various commands in /cogs/quizes.py

# Issues
There are many issues, mostly OOP related ones:
I can't sort the help command, optimally, it would be as such:
Quizes:
 - quiz
 - blitz
 - iconquiz
 - shopquiz
 - audioquiz
 - duel
 - endless
 
Store:
- store
- buy
- sell
- gold 
- givecheese
- inventory

Miscallenous:
  ....
...
Store and Miscallenous commands being sorted don't have much of an impact but the "Quizes" cog should be sorted.

