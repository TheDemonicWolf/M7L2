import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic2 import gen_advice
from bot_logic3 import gen_smile
from model import cancer



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def ready(ctx):
    await ctx.send('Всем привет! Меня зовут {bot.user}. Для более подробной информации напишите "!помощь"')


@bot.command()
async def help(ctx):
    await ctx.send("В список моих команд входят: приветствие (!hi), прощание (!bye), генерация пароля (!password), совет (!advice), калькулятор (!calculator), мемы (!meme), мем с животными (!meme_animals),  варианты поделок из бутылок (!eco_buttles) и проверка человека на наличие рака лёгких по снимку (!check).")

@bot.command()
async def hi(ctx):
    await ctx.send("Приветствую!")

@bot.command()
async def bye(ctx):
    await ctx.send("До свидания!")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def advice(ctx):
    await ctx.send(gen_advice())

@bot.command()
async def calculator(ctx, first: int, action, second: int):
    if action == "+":
        await ctx.send(first + second)
    elif action == "-":
        await ctx.send(first - second)
    elif action == "*":
        await ctx.send(first * second)
    elif action == "/":
        await ctx.send(first / second)
    else:
        await ctx.send("Не допустимая операция")

@bot.command()
async def meme_animals(ctx):
    name = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg', 'mem4.jpg', 'mem5.jpg', 'mem6.jpg', 'mem7.jpg', 'mem8.jpg']
    img_name = random.choice(name)
    with open(f'image/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    name = ['mem1.jpg', 'mem2.jpg', 'mem3.jpg', 'mem4.png', 'mem5.jpg', 'mem6.jpg', 'mem7.jpg', 'mem8.jpg']
    img_name = random.choice(name)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def eco_buttles(ctx):
    name = ['eco1.jpeg', 'eco2.png', 'eco3.jpeg', 'eco4.jpg', 'eco5.jpeg', 'eco6.jpg', 'eco7.jpg', 'eco8.jpg']
    img_name = random.choice(name)
    with open(f'images_eco/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    await ctx.send('Не выбрасывайте пластиковые бутылки! Лучше сделайте такую красивую и полезную вещь!😊')
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"images/{attachment.filename}")
            await ctx.send(f"Сохранили картинку в images/{attachment.filename}")
            name = cancer(f"images/{attachment.filename}")
            if name == "Cancer":
                await ctx.channel.send("У Вас рак лёгких! Срочно обратитесь к врачу!!!")
            elif name == "Good":
                await ctx.channel.send("Поздравляем! Ваши лёгкие совершенно здоровы!")
    else:
        await ctx.send("Вы забыли картинку :(")


bot.run(")
