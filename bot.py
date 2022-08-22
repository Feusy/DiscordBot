import os, discord, webscrape
from dotenv import load_dotenv
from discord.ext import commands , tasks


# Load secrets from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 
CHANNELID = int(os.getenv('CHANNELID'))

# Setup the Client connection
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    # Start task
    on_change.start()
 

# Bot functions 
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


#Get last post
async def get_last_msg_async():
    channel = bot.get_channel(int(CHANNELID))
    if channel is None:
        return
  
    
    message = await channel.fetch_message(channel.last_message_id)
    if message.embeds:   
        return message.embeds[0]

    return

# Posting news
@tasks.loop(minutes=2)   
async def on_change():
    print('Getting news')
    last_news = await get_last_msg_async()
    post = webscrape.get_last_news()
    embed = discord.Embed(title=post[0], description=post[1], url=post[2])

    if last_news == embed:
        return
    else:  
        channel = bot.get_channel(CHANNELID)
        await channel.send(embed=embed)

bot.run(TOKEN)

