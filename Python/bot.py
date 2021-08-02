# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!chuibot để chửi lộn'))

    
    
    

@bot.command(name='bot', help='Call bot')
async def test(ctx):
    bot_chui = [
        'Gọi cc',
        'Gọi clgt?',
        'Gọi cái giè?',
        'Bố mày đây, gọi cc',

    ]

    response = random.choice(bot_chui)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice. Must pick number of dice')
async def roll(ctx, number_of_dice: int):
    number_of_sides = 6
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send('Here is your dice :game_die: :')
    await ctx.send(', '.join(dice))



@bot.command(name='roll', help = 'Roll a random picked number start from 1')
async def random_number(ctx, number: int):
    rnumber = [
        str(random.choice(range(1, number+1)))
    ]
    number_emoji =[':zero:,:one:,:two:,:three:,:four:,:five:,:six:']
    final_number = []
    
    
    await ctx.send(' '.join(rnumber))






@bot.command(name='chuibot', help = 'Toxic with bot')
async def test(ctx, *, arg):
    list_chui = [
        'dmm',
        'con cho bot',
         'bot ngu', 
         'fuck you', 
         'fuck u', 
         'stupid bot',
         'idiot',
         'fuck',
         'cho dien',
         'cho',
         'moron',
         'fucking stupid',
         'ga',
         'noob'
        ]
    for _ in list_chui:
        arg = [
            'chửi cái dmm',
            'mày thích chửi bố mày không, bố mày gọi cả hội giờ?',
            'solo không? chửi cc',
            'Shut the fuck up noob!',
            'Á à, con chó này dám chửi bố mày à?',
            'Anh em ơi, có thằng chó nó chửi em kìa',

            ]

    bot_reply = random.choice(arg)
    await ctx.send(bot_reply)





bot.run(TOKEN)