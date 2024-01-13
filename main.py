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
import aiohttp
import io
import string
import random
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.default()
intents.voice_states = True

AUTHORIZED_USERS = []

bot = commands.Bot(
    command_prefix='.',
    self_bot=True,
    help_command=None,
    intents=intents
)

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
async def menu(ctx):
    """
    Displays a simple and easy-to-access menu.
    """
    menu_text = (
        "**🌟 Overdusts Selfbot Menu 🌟**\n"
        "1️⃣ `.auto` Autoresponder\n"
        "2️⃣ `.fun` Fun\n"
        "3️⃣ `.admin` Admin\n"
        "4️⃣ `.status` Set bot's status\n"
        "5️⃣ `.self` Selfbot information\n"
        "6️⃣ `.lite` Litecoin\n"
        "7️⃣ `.misc` Miscellaneous\n"
    )

    auto_commands = "Autoresponder Commands: `.addar`, `.removear`, `.listar`, `.startauto`, `.stopauto`"
    fun_commands = "Fun Commands: `.hehe [tag]`, `.truth`, `.dare`, `.pussy`, `.cum`, `.blowjob`, `.hentai`"
    admin_commands = "Admin Commands: `.nuke`, `.setst`, `.nickall`, `.randomnick`, `.purge`"
    status_commands = "Status Commands: `.setst`"
    litecoin_commands = "Litecoin Commands: `.ltcprice`, `.getbal`"
    misc_commands = "Miscellaneous Commands: `.scrape`, `.userinfo`, `.spam`, `.calc`, `.connectvc`, `.copyserver`"

    await ctx.send(menu_text)
    await ctx.send(auto_commands)
    await ctx.send(fun_commands)
    await ctx.send(admin_commands)
    await ctx.send(status_commands)
    await ctx.send(litecoin_commands)
    await ctx.send(misc_commands)


# Other commands remain the same as before

@bot.command(aliases=['info', 'stats'])
@commands.check(is_authorized)
async def selfbot(ctx):
    version = "Infected x1.5"
    language = "Python"
    author = "I N F E C T E D"
    total_commands = len(bot.commands)
    github_link = "https://github.com/zaddyinfected"
    prem_link = "https://infected.store/infectcord"

    ram_info = psutil.virtual_memory()
    total_ram = round(ram_info.total / (1024 ** 3), 2)
    used_ram = round(ram_info.used / (1024 ** 3), 2)
    os_info = platform.platform()

    message = (
        f"**__Infected S3LFB0T__**\n\n"
        f"**• Vers: {version}\n"
        f"• Lang: {language}\n"
        f"• Created By: {author}\n"
        f"• Total Cmds: {total_commands}\n"
        f"• Total RAM: {total_ram} GB\n"
        f"• Used RAM: {used_ram} GB\n"
        f"• Operating System: {os_info}\n\n"
        f"• GitHub: {github_link}\n"
        f"• [Buy Premium Version]({prem_link})"
    )

    embed = discord.Embed(title="Selfbot Information", description=message, color=discord.Color.green())
    await ctx.send(embed=embed)
@bot.command()
@commands.check(is_authorized)
async def scrap(ctx, number: int):
    # Your implementation
    embed = Embed(title="Message Scraping", description=f"Scraped {number} messages.\n[...] Scraped message details", color=discord.Color.teal())
    await ctx.send(embed=embed)

@bot.command()
async def spam(ctx, times: int, *, message):
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(0.1)

@bot.command()
@commands.check(is_authorized)
async def asci(ctx):
    # ASCII art logic here
    await ctx.send("ASCII art")

@bot.command()
@commands.check(is_authorized)
async def avatar(ctx):
    # Get user's avatar logic here
    await ctx.send(ctx.author.avatar_url)

@bot.command()
@commands.check(is_authorized)
async def calc(ctx, *, expression):
    # Calculator logic here
    result = eval(expression)
    await ctx.send(f"Result: {result}")

@bot.command()
@commands.check(is_authorized)
async def connectvc(ctx, channel_name):
    # Connect to a voice channel logic here
    channel = discord.utils.get(ctx.guild.channels, name=channel_name, type=discord.VoiceChannel)
    if channel:
        await channel.connect()
    else:
        await ctx.send(f"Voice channel '{channel_name}' not found.")

@bot.command()
@commands.check(is_authorized)
async def copyserver(ctx, new_server_name):
    # Copy server logic here
    # Note: This might be complex and should be handled carefully
    await ctx.send(f"Copying server to '{new_server_name}'")

@bot.command()
async def hehe(ctx, tag):
    base_url = "http://api.nekos.fun:8080/api/"
    
    valid_tags = ["4k", "bellevid", "cum", "gif", "laugh", "pat", "spank","Ass", "anal", "bj", "feed", "hentai", "lesbian", "poke", "tickle", "animalears", "blowjob", "feet", "holo", "lewd", "pussy", "waifu", "baka", "boobs", "foxgirl", "hug", "lick", "slap", "wallpapers", "belle", "cuddle", "gasm", "kiss", "neko", "smug"]
    
    if tag.lower() not in valid_tags:
        await ctx.send("Invalid tag. Available tags: " + ", ".join(valid_tags))
        return
    
    endpoint = f"{base_url}{tag.lower()}"
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        image_url = response.json()["image"]
        await ctx.send(image_url)
    except requests.exceptions.RequestException as e:
        await ctx.send(f"Error fetching image: {e}")

afk_users = {}  # Dictionary to store AFK status and details

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Check if the message mentions the bot owner
    if bot.user.mentioned_in(message):
        owner_id = "YOUR_OWNER_USER_ID"  # Replace with your actual bot owner's user ID
        if str(message.author.id) == owner_id:
            user_id = str(message.author.id)

            # Check if user is AFK
            if user_id in afk_users:
                afk_info = afk_users[user_id]
                reason = afk_info['reason']
                time_afk = afk_info['time_afk']

                # Calculate the duration
                duration = datetime.datetime.utcnow() - time_afk
                hours, remainder = divmod(duration.seconds, 3600)
                minutes, _ = divmod(remainder, 60)

                await message.channel.send(f"{message.author.display_name} is AFK ({reason}) for {hours} hours and {minutes} minutes.")

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Check if the message mentions an AFK user
    for mention in message.mentions:
        user_id = str(mention.id)
        if user_id in afk_users:
            afk_info = afk_users[user_id]
            reason = afk_info['reason']
            time_afk = afk_info['time_afk']

            # Calculate the duration
            duration = datetime.datetime.utcnow() - time_afk
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, _ = divmod(remainder, 60)

            await message.channel.send(f"{mention.display_name} is AFK ({reason}) for {hours} hours and {minutes} minutes.")

    await bot.process_commands(message)

@bot.command()
async def afk(ctx, *, reason=""):
    user_id = str(ctx.author.id)

    # Check if user is already AFK
    if user_id not in afk_users:
        afk_users[user_id] = {
            'reason': reason,
            'time_afk': datetime.datetime.utcnow()
        }
        await ctx.send(f"{ctx.author.display_name} is now AFK ({reason}).")
    else:
        await ctx.send("You are already AFK.")

@bot.command()
async def unafk(ctx):
    user_id = str(ctx.author.id)

    # Check if user is AFK
    if user_id in afk_users:
        afk_info = afk_users.pop(user_id)
        await ctx.send(f"Welcome back, {ctx.author.display_name}! Removed AFK ({afk_info['reason']}).")
    else:
        await ctx.send("You are not AFK.")


@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    try:
        # Create a new channel with the same settings as the current channel
        new_channel = await ctx.channel.clone()

        # Delete the old channel
        await ctx.channel.delete()

        # Send a message to the new channel indicating it's been nuked
        await new_channel.send(f"Nuked by **{ctx.author.display_name}**")

    except Exception as e:
        await ctx.send(f"Error: {e}")

# Add this decorator to check if the user has the necessary permissions
@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the required permissions to use this command.")
    else:
        await ctx.send(f"Error: {error}")

    await ctx.send("Status rotation updated successfully!")

async def set_status(ctx, status_number):
    await ctx.send(f"Enter text for Status {status_number} (type 'null' to finish):")
    text = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.content.lower() != 'null', timeout=60)
    
    await ctx.send(f"Enter emoji name for Status {status_number} (type 'null' for no emoji):")
    emoji = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.content.lower() != 'null', timeout=60)

    return {"text": text.content, "emoji": emoji.content}

@bot.command()
@commands.check(is_authorized)
async def setst(ctx):
    statuses = []

    for i in range(1, 4):
        status_info = await set_status(ctx, i)
        statuses.append(status_info)

    for i, status in enumerate(statuses):
        content = {
            "custom_status": {"text": status["text"], "emoji_name": status["emoji"]}
        }
        await ctx.send(f"Updating Status {i+1}...")
        requests.patch("https://discord.com/api/v9/users/@me/settings-proto/1", headers={"authorization": bot.http.token}, json=content)
        await asyncio.sleep(4)

    await ctx.send("Status rotation updated successfully!")

@bot.command()
@commands.check(is_authorized)
async def purge(ctx, amount: int = 10):
    """Purge a specific number of messages sent by you."""
    def is_author_message(message):
        return message.author == ctx.author

    if ctx.guild is not None and ctx.channel.type == discord.ChannelType.text:
        await ctx.message.delete()  # Delete the purge command message

        try:
            deleted_messages = await ctx.channel.purge(limit=amount + 1, check=is_author_message)
            await ctx.send(f"Deleted {len(deleted_messages) - 1} messages sent by {ctx.author.display_name}.", delete_after=5)
        except discord.Forbidden:
            await ctx.send("Error: Missing permissions to delete messages.")
        except discord.HTTPException as e:
            await ctx.send(f"Error: {e}")
    elif ctx.guild is None and ctx.channel.type == discord.ChannelType.private:
        # Check if it's a DM channel
        author_messages = [message async for message in ctx.channel.history(limit=amount + 1) if message.author == ctx.author]
        for message in author_messages:
            await message.delete()
        await ctx.send(f"Deleted {len(author_messages) - 1} messages sent by you in DM.", delete_after=5)
    else:
        await ctx.send("This command can only be used in a server text channel or a DM.")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.command()
async def truth(ctx):
    content = requests.get("https://api.truthordarebot.xyz/v1/truth").text
    data = json.loads(content)
    text = data["question"]
    await ctx.reply(f"- {text}")

@bot.command()
async def dare(ctx):
    content = requests.get("https://api.truthordarebot.xyz/v1/dare").text
    data = json.loads(content)
    text = data["question"]
    await ctx.reply(f"- {text}")

@bot.command()
async def pussy(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.nekos.fun:8080/api/pussy") as response:
                data = await response.json()
            image = data["image"]
            async with session.get(image) as img_response:
                image_data = await img_response.read()
            file = discord.File(io.BytesIO(image_data), filename="pussy.jpg")
            await ctx.send(file=file)
            await ctx.message.delete()
    except Exception as e:
        print(f"An Error Occurred: {e}")

@bot.command()
async def cum(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.nekos.fun:8080/api/cum") as response:
                data = await response.json()
            image = data["image"]
            async with session.get(image) as img_response:
                image_data = await img_response.read()
            file = discord.File(io.BytesIO(image_data), filename="cum.jpg")
            await ctx.send(file=file)
            await ctx.message.delete()
    except Exception as e:
        print(f"An Error Occurred: {e}")

@bot.command()
async def blowjob(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.nekos.fun:8080/api/blowjob") as response:
                data = await response.json()
            image = data["image"]
            async with session.get(image) as img_response:
                image_data = await img_response.read()
            file = discord.File(io.BytesIO(image_data), filename="blowjob.jpg")
            await ctx.send(file=file)
            await ctx.message.delete()
    except Exception as e:
        print(f"An Error Occurred: {e}")

@bot.command()
async def hentai(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://api.nekos.fun:8080/api/hentai") as response:
                data = await response.json()
            image = data["image"]
            async with session.get(image) as img_response:
                image_data = await img_response.read()
            file = discord.File(io.BytesIO(image_data), filename="hentai.jpg")
            await ctx.send(file=file)
            await ctx.message.delete()
    except Exception as e:
        print(f"An Error Occurred: {e}")

@bot.command()
async def nickall(ctx, *, name):
    if ctx.message.author.guild_permissions.administrator:
        for member in ctx.guild.members:
            await member.edit(nick=name)
        await ctx.message.delete()
    else:
        await ctx.send("You do not have the required permissions.")

@bot.command()
async def random_nick(ctx):
    nickname = rand_nick()
    await ctx.author.edit(nick=nickname)
    await ctx.send(f"Your new nickname: {nickname}")

@bot.command(aliases=['ltc'])
@commands.check(is_authorized)
async def ltcprice(ctx):
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data['market_data']['current_price']['usd']
        price_change_percentage_24h = data['market_data']['price_change_percentage_24h']
        await ctx.send(f"""
- Litecoin Price: ${price:.2f}
- 24h Price Change: {price_change_percentage_24h:.2f}%""")
        await ctx.message.delete()
    except requests.exceptions.RequestException as e:
        await ctx.send(f"> Unable To Get LiteCoin Price.")
        await ctx.message.delete()

@bot.command(aliases=['bal'])
@commands.check(is_authorized)
async def getbal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("Invalid LiteCoin Address, Please Check.")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("Unable To Fetch Balance.")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    await ctx.message.delete()
    embed = Embed(
        title="Litecoin Balance Information",
        color=discord.Color.blue(),
        description=f"""
**Litecoin Address:** {ltcaddress}
- **Current Balance:** ${usd_balance:.2f}
- **Total Received:** ${usd_total_balance:.2f}
- **Unconfirmed LTC:** ${usd_unconfirmed_balance:.2f}
        """
    )
    await ctx.send(embed=embed)

    response_message = await ctx.send(embed=embed)
    await asyncio.sleep(180)
    await response_message.delete()

def get_rule34_posts(limit=5, pid=1, tags=None):
    url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index"
    params = {
        'limit': limit,
        'pid': pid,
        'tags': tags,
        'json': 1
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@bot.command()
@commands.check(is_authorized)
async def rule34(ctx, *tags):
    if not tags:
        await ctx.send("Please provide tags for Rule34 search.")
        return

    # Combine tags into a single string
    tags_str = " ".join(tags)

    # Make a request to the Rule34 API using the get_rule34_posts function
    data = get_rule34_posts(tags=tags_str)

    if data:
        post = data[0]
        post_url = f"https://rule34.xxx/index.php?page=post&s=view&id={post['id']}"
        image_url = f"https://img.rule34.xxx/images/{post['directory']}/{post['image']}"

        result_message = f"Rule34 Result for tags `{tags_str}`: [Direct Link to Image]({image_url})"
        await ctx.send(result_message)
    else:
        await ctx.send(f"No results found for tags `{tags_str}`.")

@bot.command()
async def w(ctx, tag):
    tags = {
        "versatile": ["maid", "waifu", "marin-kitagawa", "mori-calliope", "raiden-shogun", "oppai", "selfies", "uniform"],
        "nsfw": ["ass", "hentai", "milf", "oral", "paizuri", "ecchi", "ero"]
    }

    valid_tags = [t for category_tags in tags.values() for t in category_tags]
    matching_tags = [t for t in valid_tags if t.startswith(tag)]

    if not matching_tags:
        await ctx.send(f"No matching tags found for prefix '{tag}'.")
        return

    if len(matching_tags) == 1:
        selected_tag = matching_tags[0]
        url = 'https://api.waifu.im/search'
        params = {
            'included_tags': [selected_tag],
            'height': '>=2000'
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            # Process the response data as needed
            await ctx.send(f"Here's a random waifu image with the '{selected_tag}' tag: {data['images'][0]['url']}")
        else:
            await ctx.send(f"Request failed with status code: {response.status_code}")
    else:
        await ctx.send(f"Multiple tags found for prefix '{tag}'. Please use a more specific prefix.")

@bot.command()
async def wf(ctx):
    tags_data = {
        "versatile": ["maid", "waifu", "marin-kitagawa", "mori-calliope", "raiden-shogun", "oppai", "selfies", "uniform"],
        "nsfw": ["ass", "hentai", "milf", "oral", "paizuri", "ecchi", "ero"]
    }

    formatted_tags_data = json.dumps(tags_data, indent=2)
    await ctx.send(f"```json\n{formatted_tags_data}\n```")

super_command_running = False

@bot.command()
async def super(ctx, *, items):
    global super_command_running

    if super_command_running:
        await ctx.send("Super command is already running. Use '.superstop' to stop.")
        return

    items_list = [item.strip() for item in items.split(',')]
    super_command_running = True

    for item in items_list:
        if not super_command_running:
            break

        await ctx.send(f"{item}")
        await asyncio.sleep(0.5)

@bot.command()
async def superstop(ctx):
    global super_command_running
    super_command_running = False
    await ctx.send("Super command stopped.")


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
