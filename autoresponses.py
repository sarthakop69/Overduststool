import platform
import requests
from time import sleep
import asyncio
from discord.ext import commands
import datetime
import psutil
import os
import discord
import json
import asyncio
from discord import Embed
from discord.ext import commands
intents = discord.Intents.default()
intents.voice_states = True

AUTHORIZED_USERS = []

bot = commands.Bot(
    command_prefix='.',
    self_bot=True,
    help_command=None,
    intents=intents
)

def load_autoresponder_data():
    try:
        with open('autoresponder_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_autoresponder_data(data):
    with open('autoresponder_data.json', 'w') as file:
        json.dump(data, file)


def is_authorized(ctx):
    return ctx.author.id in AUTHORIZED_USERS

@bot.event
async def on_ready():
    print("Selfbot connected as {0.user.name} ({0.user.id})".format(bot))
    print("Dev: Highly ")
    print("Version: x1.5")
    print("Server: https://discord.gg/overdusts")
    print("-" * 40)

@bot.command()
@commands.check(is_authorized)
async def menu(ctx, category=None):
    main_menu = """**# 🌟 Overdusts Selfbot Menu 🌟**
1️⃣ `.addar`      - Add autoresponder
2️⃣ `.removear`   - Remove autoresponder
3️⃣ `.listar`     - List autoresponders
4️⃣ `.ping`       - Check bot's latency
5️⃣ `.status`     - Set bot's status
6️⃣ `.selfbot`    - Display selfbot information
7️⃣ `.getbal`     - Get Litecoin balance
8️⃣ `.scrap`      - Scrape messages
9️⃣ `.userinfo`   - Get user information
🔟 `.spam`        - Spam a message
    """

    fun_commands = """**# 🎉 Fun Commands 🎉**
1️⃣ `.hehe [tag]` - Get a fun image based on tags
    """

    auto_commands = """**# 🤖 Auto Commands 🤖**
1️⃣ `.startauto`  - Start autoresponder
2️⃣ `.stopauto`   - Stop autoresponder
    """

    admin_commands = """**# ⚙️ Admin Commands ⚙️**
1️⃣ `.nuke`        - Nuke the channel
2️⃣ `.setst`       - Rotate Discord status
    """

    if category is None:
        await ctx.send(main_menu)
    elif category.lower() == 'fun':
        await ctx.send(fun_commands)
    elif category.lower() == 'auto':
        await ctx.send(auto_commands)
    elif category.lower() == 'admin':
        await ctx.send(admin_commands)
    else:
        await ctx.send("Invalid category. Available categories: main, fun, auto, admin")


# Other commands remain the same as before

@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
      
    autoresponder_data = load_autoresponder_data()
    content = message.content.lower()
    if content in autoresponder_data:
        response = autoresponder_data[content]
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command()
@commands.check(is_authorized)
async def addar(ctx, trigger, *, response):
    autoresponder_data = load_autoresponder_data()
    autoresponder_data[trigger] = response
    save_autoresponder_data(autoresponder_data)
    await ctx.send(f'Autoresponder added: `{trigger}` -> `{response}`')

@bot.command()
@commands.check(is_authorized)
async def removear(ctx, trigger):
    autoresponder_data = load_autoresponder_data()
    if trigger in autoresponder_data:
        del autoresponder_data[trigger]
        save_autoresponder_data(autoresponder_data)
        await ctx.send(f'Autoresponder removed: `{trigger}`')
    else:
        await ctx.send('Autoresponder not found.')

@bot.command()
@commands.check(is_authorized)
async def listar(ctx):
    autoresponder_data = load_autoresponder_data()
    if autoresponder_data:
        response = 'Autoresponders:\n'
        for trigger, response_text in autoresponder_data.items():
            response += f'`{trigger}` -> `{response_text}`\n'
        await ctx.send(response)
    else:
        await ctx.send('No autoresponders found.')

# Add other commands similarly

if __name__ == "__main__":
    if not os.path.isfile('.env'):
        token = input("Enter your bot token: ")
        user_id = int(input("Enter your user ID: "))

        config_data = {
            "token": token,
            "user_id": str(user_id)
        }

        with open('.env', 'w') as file:
            json.dump(config_data, file)

    with open('.env', 'r') as file:
        config_data = json.load(file)

    bot_token = config_data['token']
    AUTHORIZED_USERS.append(int(config_data['user_id']))

    bot.run(bot_token, bot=False)