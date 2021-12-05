import os
import sys
import json
import random
import asyncio
import discord
import datetime
import tracemalloc
from io import BytesIO
from calendar import month
from resourses.directory import *
from resourses.token import bot_token
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from discord.ext.commands import MissingRequiredArgument, CommandNotFound, BadArgument, BucketType, \
    ArgumentParsingError, CommandOnCooldown, MissingRole, MissingPermissions, BotMissingRole

player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
guild_ids = [786463967002361897, 772367053696008204, 786131980940476416,
             786463967002361897, 814425913001115698, 785807768841748500,
             765808478798479400]
discord.Permissions.use_external_emojis = True
tracemalloc.start()
test = discord.Client()
current, peak = tracemalloc.get_traced_memory()
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=[".", "c!"], intents=intents)
os.chdir(r"D:\Programming\Discord bots\CandyCane")


@client.event
async def on_ready():
    os.system('cls')
    print("Activating bot.")
    await asyncio.sleep(1)
    os.system('cls')
    print("Activating bot..")
    await asyncio.sleep(1)
    os.system('cls')
    print("Activating bot...")
    await asyncio.sleep(1)
    os.system('cls')
    print("Activating bot.")
    await asyncio.sleep(1)
    os.system('cls')
    print("Activating bot..")
    await asyncio.sleep(1)
    os.system('cls')
    print("Activating bot...")
    await asyncio.sleep(1)
    os.system('cls')
    print('Logged in as {0.user}'.format(client))
    print("---------------------------")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="living"))
    print(f"Ping Time    : {round(client.latency * 1000)}ms")
    print(f"Guild Count  : {len(client.guilds)}")
    await asyncio.sleep(5)
    print(f"Memory: ")
    print(f"    - Memory usage : {current / 10 ** 6}MB")
    print(f"    - Peak was {peak / 10 ** 6}MB")
    tracemalloc.stop()
    with open("LOG.txt", "a") as log:
        log.write("\n---------------------------\n")


@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass
    else:
        with open('json/reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(
                        payload.guild_id).roles, id=x['role_id'])
                    await payload.member.add_roles(role)


@client.event
async def on_guild_join(guild):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"CandyCane joined {guild.name}")
    emb_welcome = discord.Embed(
        title="Hello! Thanks for inviting me! :wave:", description=f"{welcome_msg}")
    emb_welcome.set_thumbnail(url=f"{guild.icon_url}")
    emb_welcome.set_footer(
        text="Thanks again for inviting me and i hope we have a fun time to gether", icon_url=guild.icon_url)
    await guild.system_channel.send(embed=emb_welcome)


@client.event
async def on_message(msg):
    if msg.author.id == 785491757214728223:
        return
    if msg.content.lower() == ">prefix":
        await msg.channel.send(f"Current prefix is: **`.`** and **`c!`**")
    if msg.content.lower() in ["hi", "hello"]:
        emb = discord.Embed(
            title=f"Hi {msg.author.name} :wave:!", color=0x0000ff)
        await msg.channel.send(embed=emb)
    if "haha" in msg.content.lower() or "hehe" in msg.content.lower():
        emb = discord.Embed(title="Hahaha...",
                            description=":rofl:", color=0xffdd00)
        await msg.channel.send(embed=emb)
    if "umm" in msg.content.lower():
        emb = discord.Embed(title=":grimacing:", color=0xff0000)
        await msg.channel.send(embed=emb)
    if "hmm" in msg.content.lower():
        emb = discord.Embed(
            title="Hmmmm...", description=":thinking:", color=0xfcba03)
        await msg.channel.send(embed=emb)
    await client.process_commands(msg)


@client.event
async def on_member_join(member):
    guild = member.guild
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{member} joined {guild}")
    emb = discord.Embed(title=f"Welcome to {guild} {member.name}",
                        description=f"We hope you stay at {guild}!",
                        color=random.choice(colors_dir))
    emb.add_field(name="Member ID", value=f"{member.id}")
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Welcome {member.name}",
                   icon_url=f"{member.avatar_url}")
    await guild.system_channel.send(embed=emb)
    await guild.system_channel.send('**Welcome to our server please check read the rules and enjoy your time here**')


client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx, category=None):
    if category is None:
        emb = discord.Embed(
            title="Help", description="Use `c!help <category>`to see all the commands in that category!",
            color=random.choice(colors_dir))
        emb.add_field(name="Currency",
                      value="Do `c!help currency`", inline=False)
        emb.add_field(name="Fun", value="Do `c!help fun`", inline=False)
        emb.add_field(name="Images", value="Do `c!help img`", inline=False)
        emb.add_field(name="Bot", value="Do `c!help bot`", inline=False)
        emb.add_field(name="Moderation", value="Do `c!help mod`", inline=False)
        await ctx.send(embed=emb)
    elif category == "currency":
        emb1 = discord.Embed(title="test Currency",
                             description="Here are all the currency orientated commands.",
                             color=random.choice(colors_dir))
        emb1.add_field(name="Commands:",
                       value=f"`{currency_commands}`")
        await ctx.send(embed=emb1)
    elif category == "fun":
        emb2 = discord.Embed(title="Help Fun",
                             description="Here are all the fun commands.", color=random.choice(colors_dir))
        emb2.add_field(name="Commands:",
                       value=f"`{fun_commands}`")
        await ctx.send(embed=emb2)
    elif category == "bot":
        emb3 = discord.Embed(title="Help Bot",
                             description="Here are all the bot commands.", color=random.choice(colors_dir))
        emb3.add_field(name="Commands:",
                       value=f"`{bot_commands}`")
        await ctx.send(embed=emb3)
    elif category == "img":
        emb3 = discord.Embed(title="Help Images",
                             description="Here are all the image commands.", color=random.choice(colors_dir))
        emb3.add_field(name="Commands:",
                       value=f"`{img_commands}`")
        await ctx.send(embed=emb3)
    elif category == "mod":
        emb4 = discord.Embed(title="Help Mod",
                             description="Here are all the moderation commands.",
                             color=random.choice(colors_dir))
        emb4.add_field(name="Commands:",
                       value=f"`{mod_commands}`")
        await ctx.send(embed=emb4)


@client.command(help="| Kick people from server")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} used kick and kicked {member}")
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member} from the guild; reason = {reason}")


@client.command(help="| Ban people form server", aliases=["ban"])
@commands.has_permissions(ban_members=True)
async def ban_hammer(ctx, member: discord.Member, *, reason=None):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(
            f"{ctx.author} used ban and banned {member} because of reason: {reason}")
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member} from the guild; reason = {reason}")


@client.command(help="| Unban people from the server")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} used unban")
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    await unban(member, reason=None)
    await ctx.send(member + " has been unbanned!")

    for banned_entry in banned_users:
        user = banned_entry
        print(f"{banned_entry}")

        if (user.name, user.disciminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " has been unbanned!")
            return
    await ctx.send(member + " was not found...")


@client.command(help="| Lockdown a channel")
@commands.has_permissions(manage_channels=True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(ctx.channel.mention + " ***is now in lockdown.***")


# SLOWMODE
@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, amount):
    with open("LOG.txt", "a") as mylog:
        mylog.write("\n")
        mylog.write(f"{ctx.author} activated slowmode for {amount}")
    await ctx.channel.edit(slowmode_delay=amount)
    embed = discord.Embed(
        title="SLOWMODE", description=f"{ctx.channel} was put into slowmode for {amount} seconds", color=0xffff00)
    await ctx.send(embed=embed)


@client.command(help="| Un-lock a locked channel")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")


@client.command(help="| Bot Statistics", aliases=["stat"])
async def stats(ctx):
    emb = discord.Embed(title="Bot Statistics",
                        color=random.choice(colors_dir))
    emb.add_field(name=":stopwatch: Ping Time:",
                  value=f"{round(client.latency * 1000)}ms")
    emb.add_field(name=":ballot_box: Guild Count:",
                  value=f" {len(client.guilds)}")
    emb.add_field(
        name=":pencil: Memory", value=f"{current / 10 ** 6}MB")
    await ctx.send(embed=emb)


@client.command(help='| This command returns the latency in milliseconds')
async def ping(ctx):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(
            f"{ctx.author} used ping and the bot latency was {round(client.latency * 1000)}")
    em = discord.Embed(title=":ping_pong: **Pong!**",
                       color=random.choice(colors_dir))
    em.add_field(name="Latency", value=f"{round(client.latency * 1000)}ms")
    await ctx.send(embed=em)


@client.command(help="| See Error Codes")
async def error(ctx, code=None):
    if code is None:
        emb = discord.Embed(title="List of Error Codes",
                            colors=random.choice(colors_dir),
                            timestamp=datetime.datetime.utcnow())
        emb.add_field(name="Missing Required Argument", value="`MRA`")
        emb.add_field(name="Command Not Found", value="`CNF`")
        emb.add_field(name="Bad Argument", value="`BA`")
        emb.add_field(name="Argument Parsing Error", value="`APE`")
        emb.add_field(name="BotMissingRole", value="`BMR`")
        emb.add_field(name="Command On Cooldown",
                      value="`COC` **`(invalid_exception)`**")
        emb.add_field(name="Missing Role", value="`MR`")
        emb.add_field(name="Missing Permissions", value="`MP`")
        await ctx.send(embed=emb)
    if code == "MR":
        await ctx.send("You seem to have a missing role: thinking: ")
    if code == "APE":
        await ctx.send("Nothing can be done about this other than pray the devs fix this")
    if code == "MRA":
        await ctx.send("Hmm buddy seems though you are missing an important argumnet")
    if code == "BA":
        await ctx.send("Damn son that is a bad argument if i have ever seen one!")
    if code == "COC":
        await ctx.send("Please do **`c!c`** to see all the cooldowns")
    if code == "BMR":
        await ctx.send("Seems thogh that the bot dont have role!!!! **GIMME ROLE OR ELSE.**")


@client.command(help='| This command displays the guild icon', hidden=True)
async def guild_icon(ctx):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} used guild_icon in {ctx.guild}")
    await ctx.send("{}".format(ctx.message.guild.icon_url))


@client.command(hidden=True)
@commands.has_role(786136812325437460)
async def guild_count(ctx):
    await ctx.send("**I'm in {} Guilds!**".format(len(client.guilds)))


@client.command(hidden=True, aliases=['mainbank', 'bankdata'])
async def mainbank_json(ctx):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} used mainbank_json")
    if ctx.author.id in devs:
        with open("json/mainbank.json", "r") as f:
            data = json.load(f)
        await ctx.send(data)
        return
    if ctx.author.id not in devs:
        await ctx.send("You may not access this data...")


@client.command(help='| Slap some one', hidden=True)
async def slap(ctx, target: discord.Member):
    await ctx.send(f"**{ctx.author.display_name}** just slapped {target.mention} silly!")


@client.command(help='| Get your avatar')
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    emb = discord.Embed(title=f"{member}`s avatar",
                        description="{}".format(member.avatar_url))
    await ctx.send(embed=emb)


@client.command(help='| This command repeats what your put in quotes after ".repeat"', aliases=['say'])
async def repeat(ctx, *, message=None):
    message = str(message)
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} used repeat to say: {message}")
    if message is None:
        await ctx.send("Please provide a message!")
        return
    msg = await ctx.channel.fetch_message(ctx.message.id)
    await msg.delete()
    await ctx.send(message)


@client.command(help="| Start a new google meeting")
async def meeting(ctx):
    emb = discord.Embed(title="New Meeting",
                        description="https://meet.google.com/new",
                        color=random.choice(colors_dir))
    await ctx.send(embed=emb)


@client.command(help="| Gives random stuff...")
async def randomize(ctx, mode=None):
    if mode is None:
        await ctx.send("Please eneter a mode:... \n     1.`letter`        letter\n     2.`color`       color")
    else:
        if mode == "letter":
            b = random.randint(1, 26)
            emb = discord.Embed(
                title="Here is your random number", color=random.choice(colors_dir))
            emb.add_field(name="Ur random letter",
                          value=f"`{char[b]}`")
            await ctx.send(embed=emb)
            return
        if mode == "color":
            special_colors = ["Red", "Blue", "Green", "Pink"]
            a = str(random.choice(special_colors))
            url = ""
            if a == "Red":
                url = "https://cdn.discordapp.com/emojis/820246123062362122.png?v=1"
                emoji = "<:Red:820246123062362122>"
                hex_code = 0xff0000
            if a == "Blue":
                url = "https://cdn.discordapp.com/emojis/820246069191245844.png?v=1"
                emoji = "<:Blue:820246069191245844>"
                hex_code = 0x0000ff
            if a == "Pink":
                url = "https://cdn.discordapp.com/emojis/820246155162157067.png?v=1"
                emoji = "<:Pink:820246155162157067>"
                hex_code = 0xff00d5
            if a == "Green":
                url = "https://cdn.discordapp.com/emojis/820246094054424648.png?v=1"
                emoji = "<:Green:820246094054424648>"
                hex_code = 0x00ff00
            emb = discord.Embed(
                title=f"‎{a}", description=f"{emoji}", color=hex_code)
            emb.set_thumbnail(url=f"{url}")
            emb.set_footer(text=f"{a} color")
            await ctx.send(embed=emb)
        else:
            await ctx.send("Please eneter a valid mode... \n1.`letter`        letter\n2.`color`       color")


@client.command(help='| This command will generate a random number')
async def random_no(ctx, start=0, end=100):
    n = random.randint(start, end)
    emb = discord.Embed(
        title="Here is your random number", color=random.choice(colors_dir))
    emb.add_field(name="Ur random number", value=f"`{n}`")
    await ctx.send(embed=emb)


@client.command(help="| This command gives reaction roles")
@commands.has_permissions(administrator=True)
async def reactrole(ctx, the_emoji, role: discord.Role, *, message):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(
            f"{ctx.author} started a reactrole with a role of {role}")
    emb = discord.Embed(title="React Role", description=message,
                        timestamp=datetime.datetime.utcnow())
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(the_emoji)

    with open('json/reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name': role.name,
            'role_id': role.id,
            'emoji': the_emoji,
            'message_id': msg.id
        }

        data.append(new_react_role)

    with open('json/reactrole.json', 'w') as j:
        json.dump(data, j, indent=4)


@client.command(help='| Get link to random games on itch.io', aliases=['game', 'play'])
async def games(ctx):
    rand_games = random.choice(games)
    await ctx.send(rand_games)


@client.command(hidden=True)
async def abcdefghijklmnopqrstuvwxyz(ctx):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(
            f"{ctx.author} found the `abcdefghijklmnopqrstuvwxyz` easter egg")
    msg = await ctx.channel.fetch_message(ctx.message.id)
    await msg.delete()
    await ctx.author.send('👏 Congrats you just found an easter egg!!  👏: `abcdefghijklmnopqrstuvwxyz`')


@client.command(help='| Calendar', aliases=['calender', 'cal'])
async def calendar(ctx):
    dt = datetime.datetime.today()
    yy = dt.year
    mm = dt.month
    await ctx.send(month(yy, mm))


@client.command(help='| Get the current time')
async def time(ctx):
    t = datetime.datetime.utcnow()
    emb = discord.Embed(title='Date and Time:',
                        description=f"The current time is:- **{t}**", color=0x00ff00)
    await ctx.send(embed=emb)


@client.command(help='| This command will erase the number of messages after ".clear"', aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
    limit = limit + 1
    await ctx.channel.purge(limit=limit)
    await ctx.send(f'Messages cleared by **`{ctx.author.name}`**')


@client.command(hidden=True)
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    await ctx.channel.purge(limit=500)
    await asyncio.sleep(2)
    await ctx.send("***Nuked this cannel!***")
    await ctx.send(r"https://tenor.com/view/explosion-boom-explode-gif-17383346")


@client.command(help='| This commands displays a welcome message')
async def welcome(ctx):
    await ctx.send('**Welcome to our server please check read the rules and enjoy your time here**')


@client.command(help='| This command displays kenny gang memes')
async def kenny(ctx):
    rand_kenny = random.choice(kenny)
    await ctx.send(rand_kenny)


@client.command(help='| Make an announcement', aliases=['announce'])
@commands.has_permissions(administrator=True)
async def announcement(ctx, channel: discord.TextChannel, message):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(
            f"{ctx.author} made an announcement in {channel} saying: '{message}'")
    emb = discord.Embed(title=f'An announcement by: {ctx.author}📢', description=f'**{message}**', color=0x000000,
                        timestamp=datetime.datetime.utcnow())
    emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    await channel.send(embed=emb)


@client.command(hidden=True)
async def pog(ctx):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} found the easter egg `pog`")
    msg = await ctx.channel.fetch_message(ctx.message.id)
    await msg.delete()
    user = ctx.author
    await user.send('👏 Congrats you just found an easter egg!!  👏: `POG`')


@client.command(help="|Get your self some motivation!")
async def motivate(ctx):
    motivation = random.choice(motivations)
    await ctx.send(f"Hey, {ctx.author.name}! **{motivation}** :)")


@client.command(help='| SPICY MEMES', aliases=['meme', 'dankmeme', 'dankmemes'])
async def memes(ctx):
    rand_memes = random.choice(memes)
    await ctx.send(rand_memes)


@client.command(help='| This command will display a random emoji')
async def emoji(ctx):
    rand_emoji = random.choice(emojis)
    await ctx.send(rand_emoji)


@client.command(help='| This command will display a joke', aliases=['lol', 'lel', 'lul'])
async def joke(ctx):
    rand_joke = random.choice(jokes)
    await ctx.send(rand_joke)


@client.command(help='| This command will display a pun')
async def pun(ctx):
    rand_pun = random.choice(pun)
    await ctx.send(rand_pun)


@client.command(help='| This command tells us the most wanted person')
async def wanted(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    wanted_img = Image.open("images/wanted.jpg")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((177, 177))
    wanted_img.paste(pfp, (150, 265))
    wanted_img.save("images/profile.jpg")
    await ctx.send(file=discord.File("images/profile.jpg"))


@client.command(help="| See into the future and veiw someones gravestone...", aliases=["RIP"])
async def rip(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    wanted_img = Image.open("images/RIP.jpg")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((180, 180))
    wanted_img.paste(pfp, (238, 249))
    wanted_img.save("images/Dead.jpg")
    await ctx.send(f"**Noooooooo anyone but {user.name}! 😭**")
    await ctx.send(file=discord.File("images/Dead.jpg"))


@client.command(help="| Trash")
async def trash(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    trash_img = Image.open("images/trashcan.jpg")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((176, 176))
    trash_img.paste(pfp, (91, 41))
    trash_img.save("images/Trash.jpg")
    await ctx.send(file=discord.File("images/Trash.jpg"))


@client.command(help="| Boo")
async def scare(ctx, *, text=None):
    if text is None:
        ctx.send("You need something to be scared of!")
    boo_img = Image.open("images/boo.jpg")
    Font = ImageFont.truetype("fonts/DotGothic16-Regular.ttf", 30)
    draw = ImageDraw.Draw(boo_img)
    text = str(text)
    draw.text((451, 550), text, (0, 0, 0), font=Font)
    boo_img.save("images/Scare.jpg")
    await ctx.send(file=discord.File("images/Scare.jpg"))


@client.command(help="| meh meme")
async def eh(ctx, *, text=None):
    if text is None:
        await ctx.send("Try again with some text")
    if "," not in text:
        await ctx.send("There must be 2 sets of text seperated by a comma")
    text1, text2 = text.split(',')
    eh_img = Image.open("images/eh.jpg")
    Font = ImageFont.truetype("fonts/DotGothic16-Regular.ttf", 30)
    draw = ImageDraw.Draw(eh_img)
    text1 = str(text1)
    draw.text((14, 388), text1, (0, 0, 0), font=Font)
    text2 = str(text2)
    draw.text((25, 932), text2, (0, 0, 0), font=Font)
    eh_img.save("images/eh_finito.jpg")
    await ctx.send(file=discord.File("images/eh_finito.jpg"))


@client.command(help="| Drake meme")
async def drake(ctx, *, text=None):
    if "|" not in text:
        ctx.send("There must be 2 sets of text seperated by |")
    text1, text2 = text.split('|')
    drake_img = Image.open("images/drake.jpg")
    Font = ImageFont.truetype("fonts/DotGothic16-Regular.ttf", 30)
    draw1 = ImageDraw.Draw(drake_img)
    text1 = str(text1)
    draw1.text((404, 68), text1, (0, 0, 0), font=Font)
    text2 = str(text2)
    draw1.text((404, 343), text2, (0, 0, 0), font=Font)
    drake_img.save("images/meme.jpg")
    await ctx.send(file=discord.File("images/meme.jpg"))


@client.command(help="| no sleep")
async def idontneedsleep(ctx, *, text=None):
    if text is None:
        ctx.send("Enter some text and try again...")
    sleep = Image.open("images/no_slep.jpg")
    Font = ImageFont.truetype("fonts/DotGothic16-Regular.ttf", 30)
    draw = ImageDraw.Draw(sleep)
    text = str(text)
    draw.text((565, 375), text, (255, 255, 255), font=Font)
    sleep.save("images/no_sleep_for_me.jpg")
    await ctx.send(file=discord.File("images/no_sleep_for_me.jpg"))


@client.command(help="| Drake meme")
async def brain(ctx, *, text=None):
    if text is None:
        ctx.send("Enter some text and try again...")
    jpg = random.choice(
        ["images/brain_sleep_frozen.jpg", "images/brain_sleep.jpg"])
    brain_img = Image.open(jpg)
    Font = ImageFont.truetype("fonts/DotGothic16-Regular.ttf", 30)
    draw = ImageDraw.Draw(brain_img)
    text = str(text)
    if jpg == "images/brain_sleep.jpg":
        x = 35
        y = 372
        file_name = "images/brain_sleep_fin.jpg"
    if jpg == "images/brain_sleep_frozen.jpg":
        x = 37
        y = 415
        file_name = "brain_sleep_frozen_fin.jpg"
    draw.text((x, y), text, (0, 0, 0), font=Font)
    brain_img.save(file_name)
    await ctx.send(file=discord.File(file_name))


@client.command(help="|Draw text on a white background")
async def write(ctx, *, text=None):
    if text is None:
        await ctx.send("No text provided")
    img = Image.open("images/White.jpg")
    Font = ImageFont.truetype("fonts/Chewy_Regular.ttf", 45)
    draw = ImageDraw.Draw(img)
    text = str(text)
    draw.text((79, 71), text, (255, 0, 170), font=Font)
    img.save("images/text.jpg")
    await ctx.send(file=discord.File("images/text.jpg"))


@client.command(help='| Report someone to the cops')
async def report(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    await ctx.send(f'Thanks for reporting in **@{user}** We are thankful, you are such a trooper')
    await ctx.send(f"And no you don't get money *it was just a clever trick to get **{user}** where he/she/it belongs*")


@client.command(pass_context=True, no_pm=True, aliases=["8ball"])
async def _8ball(ctx, *, message=None):
    if message is None:
        await ctx.send("You need a question to which the magic 8ball give the answer to... NOW QUESTION GIMME")
    embed = discord.Embed(
        title=f"Magic 8ball's thoughts on `{message}` is...",
        color=0x800080
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/emojis/820224589958873118.png?v=1")
    embed.add_field(name="Hmmm...", value=str(
        random.choice(choices)), inline=True)
    await ctx.send(embed=embed)


@client.command(aliases=["hl"])
async def highlow(ctx, amount=None):
    await open_account(ctx.author)
    amount = int(amount)
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    elif amount < 10:
        await ctx.send("Amount must be positive or more than 10!")
        return
    elif amount > 10000000:
        await ctx.send("Amount must be less than 10000000")
        return
    bal = await update_bank(ctx.author)
    if amount > bal[0]:
        await ctx.send("you don't have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive!")
        return
    actual = random.randint(1, 100)
    guess_number = random.randint(1, 100)
    emb = discord.Embed(
        title="HighLow!", description=f"The number is between 1 and 100 Your hint is **{guess_number}**, \nRespond "
                                      f"with `high` or `low` or `jackpot`", color=random.choice(colors_dir))
    msg = await ctx.channel.send(embed=emb)
    while True:
        guess_message = await client.wait_for('message')
        if guess_message.author == ctx.message.author:
            if guess_message.content not in game_possibilities:
                emb = discord.Embed(
                    title="Invalid command!", description=f"The options were `high`, `low` and `jackpot` what you "
                                                          f"said was not an option... Try again with more brain "
                                                          f"cells next time! Btw the number was **{actual}**",
                    color=0xff0000)
                await ctx.send(embed=emb)
                break
            guess = str(guess_message.content)
            if guess == "high" and actual > guess_number:
                emb = discord.Embed(
                    title="You Win!", description=f"You win... The number was **{actual}**", color=0x11ff11)
                other_msg = await ctx.send(embed=emb)
                await msg.add_reaction("💰")
                await msg.add_reaction("😂")
                await other_msg.add_reaction("💰")
                await other_msg.add_reaction("😂")
                await update_bank(ctx.author, amount, 'wallet')
                await update_bank(ctx.author, amount, 'wallet')
                break
            if guess == "low" and actual < guess_number:
                emb = discord.Embed(
                    title="You Win!", description=f"You win... The number was **{actual}**", color=0x11ff11)
                other_msg = await ctx.send(embed=emb)
                await msg.add_reaction("💰")
                await msg.add_reaction("😂")
                await other_msg.add_reaction("💰")
                await other_msg.add_reaction("😂")
                await update_bank(ctx.author, amount, 'wallet')
                await update_bank(ctx.author, amount, 'wallet')
                break
            if guess == "jackpot" and actual == guess_number:
                emb = discord.Embed(
                    title="You Win!", description=f"You win... The number was **{actual}**", color=0x11ff11)
                other_msg = await ctx.send(embed=emb)
                await msg.add_reaction("💰")
                await msg.add_reaction("😂")
                await other_msg.add_reaction("💰")
                await other_msg.add_reaction("😂")
                await update_bank(ctx.author, amount, 'wallet')
                await update_bank(ctx.author, amount, 'wallet')
                break
            else:
                emb = discord.Embed(
                    title="You Lose!", description=f"The number was **{actual}**", color=0xff1111)
                emb_reaction = await ctx.send(embed=emb)
                await update_bank(ctx.author, -amount, 'wallet')
                await emb_reaction.add_reaction("🙁")
                break


@client.command()
async def tictactoe(ctx, p1: discord.Member):
    p2 = ctx.author
    if p1 is None:
        emb = discord.Embed(
            title="Please mention someone to play with!", color=0xff1111)
        await ctx.send(embed=emb)
        return
    if p1 == ctx.author:
        emb = discord.Embed(
            title="You cant play with your self silly!", color=0x0000ff)
        await ctx.send(embed=emb)
        return

    global count
    global player1
    global player2
    global turn
    global gameOver
    if gameOver:
        global board
        board = ["<:board:820130016163135498>", "<:board:820130016163135498>", "<:board:820130016163135498>",
                 "<:board:820130016163135498>", "<:board:820130016163135498>", "<:board:820130016163135498>",
                 "<:board:820130016163135498>", "<:board:820130016163135498>", "<:board:820130016163135498>"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        emb = discord.Embed(
            title="A game is already in progress please finish it before starting a new one!", color=0xff0000)
        await ctx.send(embed=emb)


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    print(count)
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = "<:circle:819935674333265940>"
            elif turn == player2:
                mark = "<:cross:819935696038395924>"
            if 0 < pos < 10 and board[pos - 1] == "<:board:820130016163135498>":
                board[pos - 1] = mark
                count += 1

                # print the board

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver is True:
                    emb = discord.Embed(title=mark + " wins!", color=0x11ff11)
                    await ctx.send(embed=emb)
                elif count >= 9:
                    gameOver = True
                    emb = discord.Embed(
                        title="Its a tie!", description="*audience boo go brrrrrrrrrrrrrrr*", color=0x11ff11)
                    await ctx.send(embed=emb)

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                emb = discord.Embed(
                    title="Please choose a valid intiger between 1 and 9 (inclusive) and an unmarked title",
                    color=0x1111ff)
                await ctx.send(embed=emb)
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the `c!tictactoe` command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a player to play with... you cant play alone that is sad... :(")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


@client.command(help='| Makes a poll with yes or no choices')
async def poll(ctx, *, text):
    if "|" not in text:
        await ctx.send("There need to be 2 sets of text seperated by **`|`**")
    else:
        title, message = text.split("|")
        with open("LOG.txt", "a") as log:
            log.write("\n")
            log.write(
                f"{ctx.author} made a poll with title as {title} and discription as {message}")
        emb = discord.Embed(
            title=f'{title}', description=f'{message}', color=0x0062ff)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')


@client.command(help='| dm someone')
async def dm(ctx, user: discord.Member, *, msg):
    msg = await ctx.channel.fetch_message(ctx.message.id)
    await msg.delete()
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(f"{ctx.author} dmmed {user} with the content: {msg}")
    await user.send(f"{ctx.author} said: {msg}")
    emb = discord.Embed(title='DM has been sent!',
                        timestamp=datetime.datetime.utcnow(), color=0x0000ff)
    emb.set_footer(
        text=f'Requested by: {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command(help="| Confess stuff", aliases=["confess", "confessions"])
async def confession(ctx, *, confessions=None):
    if confessions is None:
        await ctx.send("You need something to confess")
    msg = await ctx.channel.fetch_message(ctx.message.id)
    await msg.delete()
    emb = discord.Embed(title="Confessions...",
                        description="To confess do .confession <your confession>",
                        color=random.choice(colors_dir))
    emb.add_field(name="||▇▇▇|| confessed:", value=f"**{confessions}**")
    await ctx.send(embed=emb)


@client.command(help="| Warn a member with levels of intensity")
async def warn(ctx, member: discord.Member, level, *, message):
    with open("LOG.txt", "a") as log:
        log.write("\n")
        log.write(
            f"{ctx.author} warned {member} intensity: {level} and with the reason: {message}")
    await member.send(
        f"⚠You were warned with a level of `{level}` in **{ctx.guild}** for the reason: **{message}**')")
    emb = discord.Embed(title='Warning sent', description=f'✔ {member} has been warned',
                        timestamp=datetime.datetime.utcnow())
    emb.set_footer(
        text=f'Requested by: {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command(help='| Credits to the madlads that made @CandyCane', aliases=['credits'])
async def credit(ctx):
    emb = discord.Embed(title='Credits', description=credits_message, color=0xff0084,
                        timestamp=datetime.datetime.utcnow())
    emb.add_field(name='Thanks!', value='You are truly madlads', inline=True)
    emb.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
    emb.set_footer(
        text=f'Requested by: {ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command(help='| cute gifs')
async def cute(ctx):
    rand_cute = random.choice(cute)
    await ctx.send(rand_cute)


@client.command(pass_context=True, no_pm=True, aliases=["flip"])
async def coinflip(ctx):
    emb = discord.Embed(title="Coin Flip...",
                        description="Flippoing your coin...", color=0x0000ff)
    emb.add_field(name="**It is**", value=str(random.choice(coin)))
    emb.set_thumbnail(
        url="https://thumbs.gfycat.com/KeenMeaslyCatbird-max-1mb.gif")
    await ctx.send(embed=emb)


@client.command(help='| Report a dead body')
async def report_body(ctx):
    await ctx.send('We need to get on this case right away...')
    await ctx.send(f'Thanks again **{ctx.author}** for reporting this body...')


@client.command(help='| This command displays info on a particular person', aliases=['userinfo'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        roles = [role for role in ctx.author.roles]
    else:
        roles = [role for role in member.roles]
    embed = discord.Embed(
        title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(
        text=f"Requested by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed.set_author(name="User Info: ")
    embed.add_field(name="ID:", value=member.id, inline=True)
    embed.add_field(name="User Name:", value=f"{member.name}", inline=True)
    embed.add_field(name="User Display Name:",
                    value=f"{member.display_name}", inline=True)
    embed.add_field(name="Discriminator:",
                    value=f"{member.discriminator}", inline=True)
    embed.add_field(name="Current Status:", value=str(
        member.status).title(), inline=True)
    embed.add_field(name="Current Activity:",
                    value=f"{str(member.activity.type).title().split('.')[1]}:- **{member.activity.name}**" if member.activity is not None else "None", inline=True)
    embed.add_field(name="Created At:", value=member.created_at.strftime(
        "%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
    embed.add_field(name="Joined At:", value=member.joined_at.strftime(
        "%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
    embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join(
        [role.mention for role in roles]), inline=True)
    embed.add_field(name="Top Role:", value=member.top_role, inline=True)
    embed.add_field(name="Bot?:", value=member.bot, inline=True)
    await ctx.send(embed=embed)
    return


@client.command(aliases=["server"])
async def serverInfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)


@client.command(help='| kill a specific person', aliases=['murder', 'endLife'])
async def kill(ctx, user: discord.Member):
    if user is None:
        await ctx.send('Please mention someone to kill')
    p1 = ctx.author.display_name
    story_line = [f"{p1} shot"]
    emb = discord.Embed(title='Murder Mystery',
                        description=f'\n{user} was murdered by *anonymous*', color=0xFF0000)
    emb.add_field(name='Murderer Status: ', value='Unknown', inline=True)
    await ctx.send(embed=emb)


@client.command(help="| Trash talk someone my dude...")
async def trashtalk(ctx, user: discord.Member = None):
    if user is None:
        ctx.send("You need someone to trash talk mornon...")
    rand_trashtalk = random.choice([f"Damn son! `{user.name}` is such a mornon am i right??",
                                    f"Does anyone even like `{user.name}`", "Go somewhere else you pathetic pleb...",
                                    f"`{user.name}` is such a looser", f"`{user.name}` has cooties!!!!",
                                    f"Like siriusly `{user.name}`?", f"I thought `{user.name}` was fine but now...",
                                    f"`{user.name}`'s brain cells gave up on him maybe he should give up on life..."])
    await ctx.send(f"{rand_trashtalk}")


@client.command(help='| f', aliases=['f'])
async def F(ctx):
    await ctx.send('f')


@client.command(help='| l', aliases=['l'])
async def L(ctx):
    await ctx.send('L')


@client.command(help='| rickroll ppl', hidden=True)
async def rickroll(ctx, member: discord.Member = None):
    if member is None:
        author = ctx.author
        await author.send('Mention someone to rickroll...')
        return
    else:
        await member.send('You have been rickrolled!!!')
        await member.send('https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983')
        msg = await ctx.channel.fetch_message(ctx.message.id)
        await msg.delete()
        return


@client.command(help='| The CandyCane Server', aliases=['Server', 'ccserver'])
async def ccServer(ctx):
    await ctx.send('Here is our discord server... ')
    await ctx.send('https://discord.gg/uRa2xqZCFj')


@client.command(help='| This will display a message to welcome CandyCane into the server')
async def new_server(ctx):
    await ctx.send('Hi @everyone,')
    await ctx.send('I am CandyCane, A general purpose bot with a sweet name. *(Sorry for the puns)*')
    await ctx.send('I hope we enjoy our time here on the server!!')
    await ctx.send('Here is our discord server! if you are interested...')
    await ctx.send('https://discord.gg/uRa2xqZCFj')
    await ctx.send('*you may get to propose your ideas and maybe have them accepted*')


@client.command(help='| This will make the bot appear offline', aliases=['off', 'finito'])
async def offline(ctx):
    emb = discord.Embed(title="Loggin off...",
                        description="Leaving...", color=0x111111)
    await ctx.send(embed=emb)
    await client.change_presence(status=discord.Status.offline, activity=None)


@client.command(help='| This will make the bot appear online if the server is online', aliases=['startup', 'start'])
async def online(ctx):
    emb = discord.Embed(title="Starting Servers...", color=0x01ff01)
    await ctx.send(embed=emb)
    await client.change_presence(status=discord.Status.online)


@client.command(help='| This will shutdown the server **DO NOT USE**', hidden=True, aliases=['SD', 'sd'])
async def SHUTDOWN(ctx):
    if ctx.author.id in devs:
        shutdown_code = input("SHUTDOWN CODE => ")
        if str(shutdown_code) == SHUTDOWN_CODE:
            with open("LOG.txt", "a") as log:
                log.write("\n")
                log.write(
                    f"-------------{ctx.author} USED SHUTDOWN COMMAND IN {ctx.guild}-------------")
            await ctx.send("**⚠WARNING⚠**")
            await ctx.send("USING THIS COMMAND WILL SHUTDOWN THE SERVER")
            await client.change_presence(status=discord.Status.offline, activity=None)
            channel = client.get_channel(return_channel)
            emb = discord.Embed(title="**ALERT**", description="Some one used the **SHUTDOWN** command", color=0x0000ff,
                                timestamp=datetime.datetime.utcnow())
            emb.add_field(
                name=ctx.athor, value=f"{ctx.author} used the **SHUTDOWN** command in {ctx.guild}")
            await channel.send(embed=emb)
            await client.logout()
            sys.exit(0)
        else:
            return
    else:
        await ctx.send("no u")


'''---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------'''


@client.command(help='| Check your balance', aliases=['bal', 'b'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []
    em = discord.Embed(title=f"{ctx.author}`s Inventory")
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    emb = discord.Embed(title=f"{ctx.author.name}`s balance", color=random.choice(colors_dir),
                        timestamp=datetime.datetime.utcnow())
    emb.set_thumbnail(url=ctx.author.avatar_url)
    emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    emb.add_field(name=":purse: Wallet: ",
                  value=f"{str(wallet_amt)} :coin: ", inline=False)
    emb.add_field(name=":bank: Bank:",
                  value=f"{str(bank_amt)} :coin: ", inline=False)
    emb.add_field(name="Inventory:", value="Items: ")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        emb.add_field(name="    -Items:",
                      value=f"{name}     - Amount = `{amount}`")
    emb.set_footer(text=f"{ctx.author}'s Balance",
                   icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command(help='| Withdraw money from the bank')
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    elif amount in maximum:
        user = ctx.author
        users = await get_bank_data()
        amt = users[str(user.id)]["wallet"]
        await update_bank(ctx.author, amt)
        await update_bank(ctx.author, -amt, "bank")
        await ctx.send(f"You withdrew {amt} :coin:'s! *(my advice.. use it wisely...)*")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("you don't have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive!")
        return
    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, "bank")
    await ctx.send(f"You withdrew {amount} :coin:'s! *(my advice.. use it wisely...)*")


@client.command(help='| Deposit money to the bank', aliases=['dep'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    elif amount in maximum:
        user = ctx.author
        users = await get_bank_data()
        amt = users[str(user.id)]["wallet"]
        await update_bank(ctx.author, -amt)
        await update_bank(ctx.author, amt, "bank")
        await ctx.send(f"You deposited {amt} :coin:`s ! *(Good job saving up!)*")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("you don't have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive!")
        return
    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, "bank")
    await ctx.send(f"You deposited {amount} :coin:`s ! *(Good job saving up!)*")


@client.command(help='| Send money to another member', aliases=['send'])
async def give(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    elif amount in maximum:
        user = ctx.author
        users = await get_bank_data()
        amt = users[str(user.id)]["wallet"]
        await update_bank(ctx.author, -amt)
        await update_bank(ctx.author, amt, "bank")
        await ctx.send(f"You sent {amt} :coin:`s to @{member}")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("you don't have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive!")
        return
    await update_bank(ctx.author, -1 * amount, "wallet")
    await update_bank(member, amount, "wallet")
    await ctx.send(f"You sent {amount} :coin:`s to {member}")


@client.command(help='| Steal money from another member', aliases=['steal'])
async def rob(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)
    robbers_bank = await update_bank(ctx.author)
    if bal[0] < 100:
        await ctx.send(f"Dude, @{member} is dirt poor stop wasting your time... It is so not worth it!")
        return
    crime_status = random.choice([1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    losing = random.randrange(robbers_bank[0], robbers_bank[1])
    if crime_status == 1:
        await ctx.send(f"You got caught and lost {losing}:coin:'s")
        await update_bank(ctx.author, -losing, "bank")
        return
    earning = random.randrange(0, bal[0])
    await update_bank(ctx.author, earning, "wallet")
    await update_bank(member, -1 * earning, "wallet")
    await ctx.send(f"You robbed {member} and got {earning}:coin:`s")


@client.command(name="use")
async def use(ctx, item, amount=1):
    member = ctx.author
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    res = await use_sell_this(ctx.author, item, amount)
    rand_ded = random.choice(yes_or_no)
    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} item in your bag.")
            return
        if res[1] == 3:
            await ctx.send(f"{member.mention}You don't have the item  in your bag.")
            return
    if item in un_usable:
        await ctx.send("You can't use this item :thinking:")
        await ctx.send("You can only use items that have the `Tool` or `Food` description")
        return
    if item == 'watch':
        t = datetime.time()
        emb = discord.Embed(
            title='Time', description=f"The current time is:- **{t}**", color=0x00ff00)
        await ctx.send(embed=emb)
        return
    if item == 'pizza':
        em = discord.Embed(title="🍕 Pizza ─ EFFECTS",
                           description='You have a chance of dying from obesity...')
        em.add_field(name='r u ded??', value=rand_ded, inline=True)
        await ctx.send(embed=em)
        users[str(user.id)]['bag'].pop([i['item']
                                        for i in users[str(user.id)]['bag']].index('pizza', 0))
        return
    if item == 'cookie':
        em = discord.Embed(title="🍪 Cookie ─ EFFECTS",
                           description='You ate da cookie')
        em.add_field(name='r u ded??', value=rand_ded, inline=True)
        await ctx.send(embed=em)
        users[str(user.id)]['bag'].pop([i['item']
                                        for i in users[str(user.id)]['bag']].index('cookie', 0))
        return
    if item == 'car':
        destination = ['mall', 'park', 'subway',
                       'chki cheese *idontwantogetcopyrighted*', 'End of space and time...']
        em = discord.Embed(title=f"You drive to the {random.choice(destination)}",
                           description='When you arrived there you realised that it was closed due to the current '
                                       'times...\n Then you committed suicide cuz u embarrassed... also because you '
                                       "died you lost the car... ded ppl don't have cars *or i think so...*")
        await ctx.send(embed=em)
        return
    if item == 'gun':
        em = discord.Embed(title="Gunpoint",
                           description="You used it to threaten a person but then they jumped the "
                                       "gun as in literally jumped on it breaking your hand and the gun "
                                       "costing you 50 buck as a hospital charge")
        await update_bank(ctx.author, -50)
        await ctx.send(embed=em)
        return
    if item == 'laptop':
        emb = discord.Embed(title="You used ur laptop", description="You coded a bot to get you unlimited money but "
                                                                    "that plan backfired cuz ur bot was so efficient "
                                                                    "that it exploded ur laptop! \n Also did i "
                                                                    "mention you made 100 bucks?? cuz u did")
        await update_bank(ctx.author, +100)
        await ctx.send(embed=emb)
        return


async def use_sell_this(user, item_name):
    item_name = item_name.lower()
    name_ = None
    for item in main_shop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            break
    if name_ is None:
        return [False, 1]
    users = await get_bank_data()
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t is None:
            return [False, 3]
    except:
        return [False, 3]
    with open("json/mainbank.json", "w") as f:
        json.dump(users, f)
    return [True, "Worked"]


@client.command(help="|CHEAT")
async def activate(ctx, *, stuff):
    await ctx.send(f"Activated `{stuff}`")


@client.command(help='| Give your money to charity... *(a way to get rid of money)*', aliases=['charity'])
async def donate(ctx, amount=None):
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    elif amount in maximum:
        user = ctx.author
        users = await get_bank_data()
        amt = users[str(user.id)]["wallet"]
        await update_bank(ctx.author, -amt)
        await ctx.send(f"You donated {amt} :coin:'s! *+15 karma*")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("you don't have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive!")
        return
    await update_bank(ctx.author, -1 * amount)
    await ctx.send(f"You donated {amount} :coin:'s! *+15 karma*")


@client.command(help='| You can buy items form the shop for coins in your wallet', aliases=['store'])
async def shop(ctx):
    em = discord.Embed(title="Shop Items", color=0x00FF00)
    type_of_shop = random.choice(
        [main_shop, main_shop, varied_shop, main_shop, main_shop,
         main_shop, main_shop, main_shop, main_shop, main_shop,
         main_shop, main_shop, main_shop, main_shop, main_shop,
         main_shop, main_shop, main_shop, main_shop, main_shop])
    for item in type_of_shop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name=name, value=f"${price} | {desc}")
    await ctx.send(embed=em)


@client.command(help='| Buy items from the shop')
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)
    res = await buy_this(ctx.author, item, amount)
    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return
    await ctx.send(f"You just bought {amount} {item}")


@client.command(help='| Check your inventory', aliases=['inv', 'bag'])
async def inventory(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []
    em = discord.Embed(title=f"{ctx.author}`s Inventory")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        em.add_field(name=name, value=amount)
    await ctx.send(embed=em)


@client.command(hidden=True)
@commands.cooldown(1, 30, BucketType.user)
async def code(ctx, redeem_code):
    user = ctx.author
    if redeem_code is None:
        msg = await ctx.channel.fetch_message(ctx.message.id)
        await msg.delete()
        await user.send("Please enter a valid code to redeem your money")
        return
    if redeem_code in code:
        msg = await ctx.channel.fetch_message(ctx.message.id)
        await msg.delete()
        await open_account(ctx.author)
        redeemed_money = random.randrange(50, 100)
        await user.send(f'You earned {redeemed_money}:coin: from the redeem code!')
        await update_bank(ctx.author, redeemed_money)
        return


@client.command(hidden=True)
@commands.cooldown(1, 30, BucketType.user)
async def cryptocurr(ctx, msg):
    if msg is None:
        the_code = random.choice(cryptocurr)
        emb = discord.Embed(
            title="Decrypt this:", description=the_code, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=emb)
        return
    elif msg in decrypted_:
        await open_account(ctx.author)
        caught = random.choice([1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        if caught == 1:
            msg = await ctx.channel.fetch_message(ctx.message.id)
            await msg.delete()
            await ctx.send("You did not earn anything and you had to pay for mining")
            bal = await update_bank(ctx.author)
            earning = random.randrange(0, bal[0])
            await update_bank(ctx.author, - earning)
            return
        else:
            msg = await ctx.channel.fetch_message(ctx.message.id)
            await msg.delete()
            money = random.randrange(100, 1000)
            await ctx.send(f"You earned {money}:coin:'s")
            await update_bank(ctx.author, + money)
            msg = await ctx.channel.fetch_message(ctx.message.id)
            await msg.delete()
            return
    else:
        the_code = random.choice(cryptocurr)
        emb = discord.Embed(title="Invalid code",
                            description=f"That was an invalid code try decrypting this: \n{the_code}",
                            timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=emb)
        return


@client.command(help="| Gamble your money *(DON'T GAMBLE KIDS...)*", aliases=['slots'])
@commands.cooldown(1, 15, BucketType.user)
async def gamble(ctx, amount=None):
    await open_account(ctx.author)
    amount = int(amount)
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    elif amount < 10:
        await ctx.send("Amount must be positive or more than 10!")
        return
    elif amount > 10000000:
        await ctx.send("Amount must be less than 10000000")
        return
    bal = await update_bank(ctx.author)
    if amount > bal[0]:
        await ctx.send("you don't have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive!")
        return
    my_num = random.randrange(0, 10)
    user_num = random.randrange(0, 10)
    emb = discord.Embed(title="Gamble", description=f"You bet {amount}", color=random.choice(colors_dir),
                        timestamp=datetime.datetime.utcnow())
    emb.add_field(name=f"{ctx.author} rolled:", value=f"{user_num}")
    emb.add_field(name="CandyCane rolled:", value=f"{my_num}")
    await ctx.send(embed=emb)
    win_or_loose = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2])
    if user_num == my_num:
        await ctx.send("**🎉YOU HIT THE JACKPOT!!!!🎉**")
        await update_bank(ctx.author, amount * 10)
        return
    elif win_or_loose == 1:
        await ctx.send("Although gambling is bad you made a little money...")
        await update_bank(ctx.author, amount * 2)
        return
    else:
        await ctx.send("This is why I say **DON'T GAMBLE**")
        await update_bank(ctx.author, -amount)
        return


@client.command(help='| Invest in places and earn money', aliases=['investment'])
@commands.cooldown(1, 5, BucketType.user)
async def invest(ctx, amount):
    if amount is None:
        await ctx.send("Please enter the amount")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("you don't have that much money")
        return
    if amount < 120:
        await ctx.send("You amount must either be positive or above 120 :coin:`s")
        return
    await open_account(ctx.author)
    good_emoji = ["💹", "📈"]
    success = f'''{random.choice(good_emoji)}Your investment was successful... and your reputation solid also your 
    earnings were thrice the :coin:`s you put in '''
    fail = f'''📉Due to market volatility and the current circumstance your investment in a company`s share did not 
    pay off and you lost all your money... '''
    some_where_in_the_middle = f'''📊The market was not as stable as the season due to the current time being an off 
    season you made a marginal profit of twice the :coin:`s you put in '''
    investment_possibilities = random.choice(
        [success, fail, some_where_in_the_middle])
    if investment_possibilities is success:
        await update_bank(ctx.author, 3 * amount)
        await update_bank(ctx.author, -amount)
        emb = discord.Embed(title=f'Investment Results for {ctx.author}',
                            description=f"Here are your investment results {ctx.author.mention}",
                            color=random.choice(colors_dir),
                            timestamp=datetime.datetime.utcnow())
        emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        emb.add_field(name="**You investment Report:**",
                      value=f"{investment_possibilities}")
        await ctx.send(embed=emb)
    if investment_possibilities is fail:
        await update_bank(ctx.author, -1 * amount)
        emb = discord.Embed(title=f'Investment Results for {ctx.author}',
                            description=f"Here are your investment results {ctx.author.mention}",
                            color=random.choice(colors_dir),
                            timestamp=datetime.datetime.utcnow())
        emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        emb.add_field(name="**You investment Report:**",
                      value=f"{investment_possibilities}")
        await ctx.send(embed=emb)
    if investment_possibilities is some_where_in_the_middle:
        await update_bank(ctx.author, 2 * amount)
        await update_bank(ctx.author, -amount)
        emb = discord.Embed(title=f'Investment Results for {ctx.author}',
                            description=f"Here are your investment results {ctx.author.mention}",
                            color=random.choice(colors_dir),
                            timestamp=datetime.datetime.utcnow())
        emb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        emb.add_field(name="**You investment Report:**",
                      value=f"{investment_possibilities}")
        await ctx.send(embed=emb)


@client.command(help='| See all the available jobs')
async def joblist(ctx):
    emb = discord.Embed(title='Available jobs', description=f'{joblist}',
                        timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=emb)


@client.command(help="| See how long the cooldown for commands are!", aliases=["c"])
async def C(ctx):
    emb = discord.Embed(title="Cooldowns",
                        description="Cooldowns for all the commands",
                        color=random.choice(colors_dir))
    emb.add_field(name="**`.work <job>`**", value="100 seconds")
    emb.add_field(name="**`.gamble`**", value="15 seconds")
    emb.add_field(name="**`.beg`**", value="5 seconds")
    emb.add_field(name="**`.invest`**", value="5 seconds")
    await ctx.send(embed=emb)


@client.command(help='| Work to earn money', aliases=["w"])
@commands.cooldown(1, 100, BucketType.user)
async def work(ctx, job=None):
    await open_account(ctx.author)
    if job is None:
        await ctx.send("Please provide a job")
        await ctx.send("To see available jobs do `.joblist`")
        return
    applicable_job_list = ['detective', 'police',
                           'fire_fighter', 'bus_driver', 'dentist', 'doctor']
    if job in applicable_job_list:
        rand_code = random.choice(code)
        if job == 'bus_driver':
            give_or_not = random.choice(
                [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
            if give_or_not == 2:
                earnings = random.randrange(350, 400)
                job_emb = discord.Embed(
                    title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
                await ctx.send(embed=job_emb)
                await update_bank(ctx.author, earnings)
                return
            if give_or_not == 1:
                user = ctx.author
                await user.send(f"While working you got a redeem code... to redeem do `.code {rand_code}`")
                earnings = random.randrange(350, 400)
                job_emb = discord.Embed(
                    title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
                await ctx.send(embed=job_emb)
                await update_bank(ctx.author, earnings)
                return
        if job == 'police':
            earnings = random.randrange(500, 750)
            job_emb = discord.Embed(
                title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
            await ctx.send(embed=job_emb)
            await update_bank(ctx.author, earnings)
            return
        if job == 'detective':
            earnings = random.randrange(900, 1000)
            job_emb = discord.Embed(
                title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
            await ctx.send(embed=job_emb)
            await update_bank(ctx.author, earnings)
            return
        if job == 'fire_fighter':
            earnings = random.randrange(500, 650)
            job_emb = discord.Embed(
                title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
            await ctx.send(embed=job_emb)
            await update_bank(ctx.author, earnings)
            return
        if job == 'dentist':
            earnings = random.randrange(625, 725)
            job_emb = discord.Embed(
                title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
            await ctx.send(embed=job_emb)
            await update_bank(ctx.author, earnings)
            return
        if job == 'doctor':
            earnings = random.randrange(1000, 1001)
            job_emb = discord.Embed(
                title=f"{ctx.author.name} earned {earnings}:coin:'s", color=0x00ff00)
            await ctx.send(embed=job_emb)
            await update_bank(ctx.author, earnings)
            return
    else:
        await ctx.send('That is not a valid job role, \nTo see available jobs do `.joblist`')


@client.command(help='| Earn money by begging')
@commands.cooldown(1, 5, BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    person = random.choice(people)
    user = ctx.author
    users = await get_bank_data()
    earnings = random.randrange(101)
    what_happens = [1, 2, 2, 2, 1]
    wh = random.choice(what_happens)
    if wh == 2:
        await ctx.send(f"`{person}` gave you {earnings} coins!!")
        users[str(user.id)]["wallet"] += earnings
        with open("json/mainbank.json", "w") as f:
            json.dump(users, f)
        await update_bank(ctx.author)
        return
    if wh == 1:
        situations = ["said **'Get the hell out of my sight'**", "someone else stole my heart to help mankind..",
                      "said GET A FRICKING JOB YOU *femaledog*", "eh...", f"/kill {ctx.author} for begging"]
        situation = random.choice(situations)
        await ctx.send(f"`{person}` {situation}")
        return
    else:
        return


@client.command()
async def sell(ctx, item, amount=1):
    await open_account(ctx.author)
    res = await sell_this(ctx.author, item, amount)
    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your bag.")
            return
    await ctx.send(f"You just sold {amount} {item}.")


'''--Helper Commands--'''


async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in varied_shop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if item_name == "aztec_coin":
                price = 1000001
            if price is None:
                price = 0.8 * item["price"]
            break
    if name_ is None:
        return [False, 1]
    cost = price * amount
    users = await get_bank_data()
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t is None:
            return [False, 3]
    except:
        return [False, 3]
    with open("json/mainbank.json", "w") as f:
        json.dump(users, f)
    await update_bank(user, cost, "wallet")
    return [True, "Worked"]


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in varied_shop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break
    if name_ is None:
        return [False, 1]
    cost = price * amount
    users = await get_bank_data()
    bal = await update_bank(user)
    if bal[0] < cost:
        return [False, 2]
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t is None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("json/mainbank.json", "w") as f:
        json.dump(users, f)
    await update_bank(user, cost * -1, "wallet")
    return [True, "Worked"]


async def open_account(user):
    with open("json/mainbank.json", "r") as f:
        users = json.load(f)
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 100
        users[str(user.id)]["bank"] = 10000

    with open("json/mainbank.json", "w") as f:
        json.dump(users, f)
        return True


async def get_bank_data():
    with open("json/mainbank.json", "r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("json/mainbank.json", "w") as f:
        json.dump(users, f)
    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal


@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, MissingRequiredArgument):
        await ctx.send("⚠️MRA⚠️")
        await ctx.send("Hmm buddy seems though you are missing an important argumnet")
        await ctx.send("For more info do: **`c!error MRA`**")
        return
    if isinstance(exc, MissingRole):
        await ctx.send("⚠️MR⚠️")
        await ctx.send("You seem to have a missing role :thinking: ")
        await ctx.send("For more info do: **`c!error MR`**")
        return
    if isinstance(exc, MissingPermissions):
        await ctx.send("⚠️MP⚠️")
        await ctx.send("For more info do: **`c!error MP`**")
        return
    elif isinstance(exc, CommandNotFound):
        return
    elif isinstance(exc, BadArgument):
        await ctx.send("⚠️BA⚠️")
        await ctx.send("Damn son that is a bad argument if i have ever seen one!")
        await ctx.send("For more info do: **`c!error BA`**")
        return
    elif isinstance(exc, ArgumentParsingError):
        await ctx.send("⚠️APE⚠️")
        await ctx.send("Nothing can be done about this other than pray the devs fix this")
        await ctx.send("For more info do: **`c!error APE`**")
        return
    elif isinstance(exc, CommandOnCooldown):
        await ctx.send(f"⚠️COC⚠️")
        await ctx.send("For more info do: **`c!error COC`**")
        await ctx.send("For more info do: **`c!c`**")
        return
    elif isinstance(exc, BotMissingRole):
        await ctx.send("⚠️BMR⚠️")
        await ctx.send("For more info do: **c!error BMR**")
        return
    else:
        raise exc


"======================================================================================================================"


async def ch_pr():
    await client.wait_until_ready()
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(status=discord.Status.online,
                                     activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(10)


client.loop.create_task(ch_pr())

client.run(bot_token)
