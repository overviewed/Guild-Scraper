import os, sys, discord, time
from discord.ext import commands
from pystyle import Colors, Colorate
from colored import fg
p = fg('#8c00ff')
r = '\x1b[38;5;196m'

if sys.platform == "linux":
    clear = lambda: os.system("clear")
else:
    clear = lambda: os.system("cls")


tokentype = input(f"{p}Are you using a Bot or User token <bot/user>: ")
while tokentype !="bot" and tokentype != "user":
  print(f"\x1b[38;5;196mInvalid option")
  tokentype = input(f"\x1b[38;5;196mBot or User token <bot/user>: ")
  
token = input(f'''{p}ENTER TOKEN : ''')

if tokentype == "bot":
  type = "Bot"
  headers = {'Authorization': f'{token}'}
elif tokentype == "user":
  type = "Human"
  headers = {'Authorization': f'Bot {token}'}

intents = discord.Intents.all()
if type == 'Human':
  client = commands.Bot(command_prefix=">>", case_insensitive=False, self_bot=True, intents=intents)
else:
  client = commands.Bot(command_prefix=">>", case_insensitive=False, intents=intents)

@client.event
async def on_connect():
    clear()
    print(Colorate.Vertical(Colors.purple_to_blue,
'''
███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████╗██║     ██████╔╝███████║██████╔╝█████╗  
╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  
███████║╚██████╗██║  ██║██║  ██║██║     ███████╗
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝''', ))
    print(f"{p}Logged in as {client.user}")
    try:
        os.remove("Scraped/Members.txt")
        os.remove("Scraped/Channels.txt")
        os.remove("Scraped/Roles.txt")
    except:
        pass

    while True:
      try:
        guild_id = int(input(f'{p}Guild ID: '))
        break
      except ValueError:
        print(f"{r}Invalid Value")
        continue
    for guild in client.guilds:
      if guild.id == guild_id:
        members = await guild.chunk()
        members_ = 0
        f = open("Scraped/Members.txt", "a+")
        for member in members:
          f.write(f"{member.id}\n")
          members_ += 1
        print(f"{p}Scraped {members_} Members")

        channels = 0
        f = open("Scraped/Channels.txt", "a+")
        for channel in guild.channels:
          f.write(f"{channel.id}\n")
          channels += 1
        print(f"{p}Scraped {channels} Channels")

        roles = 0
        f = open("Scraped/Roles.txt", "a+")
        for role in guild.roles:
          f.write(f"{role.id}\n")
          roles += 1
        print(f"{p}Scraped {roles} Roles")
        print(f"{p}Scraping complete")
        time.sleep(3)
        os._exit(0)
      else:
        print(f"{r}I couldn't fetch this guild")
        os._exit(0)

if type == "Human":
  try:
    client.run(token, bot=False)
  except:
    print(f"{r}Invalid Token")
    os._exit(0)
elif type == "Bot":
  try:
    client.run(token, bot=True)
  except:
    print(f"{r}Invalid Token")
    os._exit(0)