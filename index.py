import discum, random, time, json, os.path
from rich import console, print

data = None
if os.path.exists("data.json"):
    data = json.loads(open("data.json").read())
if data is not None and "token" in data.keys():
    token = data["token"]
else:
    token = input('ur token: ')
bot = discum.Client(token=token, log=False)
memberz = []
if data is not None and "guildid" in data.keys():
    guildz = data["guildid"]
else:
    guildz = input("Please input guild ID: ")
if data is not None and "channelid" in data.keys():
    channel = data["channelid"]
else:
    channel = input("Please input a channel ID in that guild: ")
if data is not None and "message" in data.keys():
    messag = data["message"]
else:
    messag = input("Please input your message: ")
if data is not None and "time" in data.keys():
    timez = data["time"]
else:
    timez = input("How long between DMs: ")


@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guildz, channel)
    if bot.gateway.finishedMemberFetching(guildz):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()


bot.gateway.run()
print("Starting add members.")
for memberID in bot.gateway.session.guild(guildz).members:
    memberz.append(memberID)
print("Starting to DM.")
for x in memberz:
    try:
        rand = random.randint(0, 20)
        if rand == 20:
            print(f'Sleeping for 45 seconds to prevent rate-limiting.')
            time.sleep(45)
            print(f'Done sleeping!')
        print(f"Preparing to DM {x}.")
        time.sleep(int(timez))
        newDM = bot.createDM([f"{x}"]).json()["id"]
        bot.sendMessage(newDM, f"{messag} DM bot by https://github.com/Apophis52/Python-Mass-DM-Selfbot/")
        print(f'DMed {x}.')
    except Exception as E:
        print(E)
        print(f'Couldn\'t DM {x}.')
