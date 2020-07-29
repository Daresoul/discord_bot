import discord
from discord.ext import commands

Server_id = 458386020212408331
Channel_id = 696438547976159302
message_id = 696798422232989819
admins = [240925972000407552]
bot_id = 458384145962237982
role_ids = [696885914416447619, 696885956090789889, 696885995978620998]
role_emoji = ['🙂', '❤️', '👍']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await client.change_presence(activity=discord.Game(name='my game'))

        activity = discord.Activity(name='For your reaction!', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)

    async def on_message(self, message):
        args = message.content.split()
        #print(message)
        if message.content.startswith('$write'):
            channel = client.get_channel(int(message.channel.id))
            if(len(args) >= 3):
                wordEmoji = args[1]
                fillEmoji = args[2]
                newArgs = args[3:]
                await message.delete()
                for arg in newArgs:
                    text = CreateSentences(arg, wordEmoji, fillEmoji)
                    await channel.send(text[0] + "\n" + text[1] + "\n" + text[2] + "\n" + text[3] + "\n" + text[4] + "\n" + text[5] + "\n" + text[6])
            

def CreateSentences(whatToWrite, wordEmoji, fillEmoji):
    arr = ["", "", "", "", "", "", ""]

    AddSpace(arr, fillEmoji)

    for c in whatToWrite:
        GetCharacter(arr, c, wordEmoji, fillEmoji)
        AddSpace(arr, fillEmoji)


    return arr

def AddSpace(arr, fillEmoji):
        arr[0] += fillEmoji
        arr[1] += fillEmoji
        arr[2] += fillEmoji
        arr[3] += fillEmoji
        arr[4] += fillEmoji
        arr[5] += fillEmoji
        arr[6] += fillEmoji

def printA(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printB(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printC(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printD(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printE(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printF(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printG(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printH(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printI(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[3] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printJ(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printK(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printL(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printM(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printN(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[2] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printO(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printP(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printQ(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += fillEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[4] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printR(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printS(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += fillEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[3] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printT(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[3] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printU(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printV(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printW(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printX(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printY(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[2] += wordEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[3] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[4] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[5] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def printZ(arr, wordEmoji, fillEmoji):
    arr[0] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji
    arr[1] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[2] += fillEmoji +  " "  + wordEmoji +  " "  + fillEmoji
    arr[3] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[4] += fillEmoji +  " "  + fillEmoji +  " "  + wordEmoji
    arr[5] += wordEmoji +  " "  + wordEmoji +  " "  + wordEmoji
    arr[6] += fillEmoji +  " "  + fillEmoji +  " "  + fillEmoji

def GetCharacter(arr, c, wordEmoji, fillEmoji):
    print("2: " + str(len(arr[0])))
    if c == 'a': printA(arr, wordEmoji, fillEmoji)
    elif c =='b': printB(arr, wordEmoji, fillEmoji)
    elif c == 'c': printC(arr, wordEmoji, fillEmoji)
    elif c == 'd': printD(arr, wordEmoji, fillEmoji)
    elif c == 'e': printE(arr, wordEmoji, fillEmoji)
    elif c == 'f': printF(arr, wordEmoji, fillEmoji)
    elif c == 'g': printG(arr, wordEmoji, fillEmoji)
    elif c == 'h': printH(arr, wordEmoji, fillEmoji)
    elif c == 'i': printI(arr, wordEmoji, fillEmoji)
    elif c == 'j': printJ(arr, wordEmoji, fillEmoji)
    elif c == 'k': printK(arr, wordEmoji, fillEmoji)
    elif c == 'l': printL(arr, wordEmoji, fillEmoji)
    elif c == 'm': printM(arr, wordEmoji, fillEmoji)
    elif c == 'n': printN(arr, wordEmoji, fillEmoji)
    elif c == 'o': printO(arr, wordEmoji, fillEmoji)
    elif c == 'p': printP(arr, wordEmoji, fillEmoji)
    elif c == 'q': printQ(arr, wordEmoji, fillEmoji)
    elif c == 'r': printR(arr, wordEmoji, fillEmoji)
    elif c == 's': printS(arr, wordEmoji, fillEmoji)
    elif c == 't': printT(arr, wordEmoji, fillEmoji)
    elif c == 'u': printU(arr, wordEmoji, fillEmoji)
    elif c == 'v': printV(arr, wordEmoji, fillEmoji)
    elif c == 'w': printW(arr, wordEmoji, fillEmoji)
    elif c == 'x': printX(arr, wordEmoji, fillEmoji)
    elif c == 'y': printY(arr, wordEmoji, fillEmoji)
    elif c == 'z': printZ(arr, wordEmoji, fillEmoji)

client = MyClient()
client.run('NDU4Mzg0MTQ1OTYyMjM3OTgy.WyglgA.5VRlCREIkmRH_wBBX-ddqUiADYQ')
