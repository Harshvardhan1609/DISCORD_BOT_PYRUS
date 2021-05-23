#import discord server 
import discord
from discord.ext import commands

#Client configuration
client = commands.Bot(command_prefix='--')


@client.command(name='version')
async def version(context):

     myEmbed = discord.Embed(Title = "current Version" , description = "Pyrus is in version 1.1", color = 0x00ff0073)
     myEmbed.add_field(name = "version code:", value = "v1.1.0", inline = False)
     myEmbed.add_field(name="Date Released:", value = "May 23, 2021" , inline = False)
     myEmbed.set_footer(text = "I am pyrus your personal assistent")
     myEmbed.set_author(name = "your_Name")
   
     await context.message.channel.send(embed=myEmbed)
    

    

#@client.event is used to start a new event
@client.event
async def on_ready():
#DO STUFF......

    general_channel = client.get_channel('here remove the marks and write the ID of the channel')

    await general_channel.send("nameste world !")

@client.event
async def on_message(message):
#async def on_message(message): = takes function parameter and then this message written in the paranthesis take the messages which is send to the discord
    if message.content == "hello pyrus":
     general_channel = client.get_channel('here remove the marks and write the ID of the channel')
     await general_channel.send("Hello sir ! how are you")

    elif message.content == "What is your version":
     general_channel = client.get_channel('here remove the marks and write the ID of the channel')

     myEmbed = discord.Embed(Title = "current Version" , description = "Pyrus is in version 1.1", color = 0x00ff0073)
     myEmbed.add_field(name = "version code:", value = "v1.1.0", inline = False)
     myEmbed.add_field(name="Date Released:", value = "May 23, 2021" , inline = False)
     myEmbed.set_footer(text = "I am pyrus your personal assistent")
     myEmbed.set_author(name = "Your_name")

     await general_channel.send(embed=myEmbed)
    await client.process_commands(message)

@client.event
async def on_disconnect():
    general_channel = client.get_channel('here remove the marks and write the ID of the channel')
    await general_channel.send("Goodbye sir!")

@client.event
async def on_typeing():
    general_channel = client.get_channel('here remove the marks and write the ID of the channel')
    await general_channel.send("Ready to answer your all questions!")



#Run the code on the server
token = 'Please write down the token code'
client.run(token)
