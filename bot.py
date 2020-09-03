import os#imports library for os
import discord #imports library for dicord.py
from discord import file


TOKEN={your_bot_token}
GUILD={your_guild_name}

#main loop
client=discord.Client()

@client.event #
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user.name} has connected to Discord!\n'
    f'{guild.name}(id: {guild.id})'
    )
 
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {GUILD} !\n'
        f'Kindly Introduce Yourself!'
    )

@client.event
async def on_message(message):
    if message.author==client.user:
        return 
    
    known={"!hi":"Hey, how are you?","!favorite character":"Yamori from TKG.","!whats your age?":"Does it matter.","!who are you?":"Your future master, but rn I'm just a little bot."}
    
    imgList=os.listdir("./images")
    imgDir=['201','202','203','204','212','213','214','301','302','303','304','311','312','316']

    if str(message.content) in known:
        await message.channel.send(
            f'{known[message.content]}'
        )
    
    elif message.content=="!help":
         await message.dm_channel.send(
             f'Go to resources!'
         )
    elif message.content=="!Syl2":
        await message.channel.send(
            f'Commands for syllabus of second semester:\n'
            '!S-201- Engineering Mathematics\n'
            '!S-203- Engineering Chemistry\n'
            '!S-204- Basic Electronics\n'
            '!S-202- Engineering Physics\n'
            '!S-214- Basic Electronics Lab\n'
            '!S-213- Physics Lab\n'
            '!S-212- Chemistry Lab\n'
        )
    elif message.content=="!Syl3":
        await message.channel.send(
            f'Commands for syllabus of third semester:\n'
            '!S-301- Computer Programming\n'
            '!S-302- Electronic Devices and Circuits\n'
            '!S-303- Signals and Systems\n'
            '!S-304- Electrical Network Theory\n'
            '!S-312- Electronic Devices Lab\n'
            '!S-316- Circuit Simulation Lab\n'
            '!S-311- Computer Programming Lab\n'
        )
    elif str(str(message.content)[3:]) in imgDir:
            await message.channel.send( file=discord.File("./images/"+str(str(message.content)[3:])+".jpg"))
            
    
    
    
    

client.run(TOKEN)
