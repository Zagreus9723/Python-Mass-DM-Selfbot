import discum, random, time
from rich import console, print
bot = discum.Client(token=input('ur token: '), log=False)
memberz = []
guildz = input("Please input guild ID: ")
channel = input("Please input a channel ID in that guild: ")
messag = input("Please input your message: ")
timez = input("How long between DMs: ")
@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guildz, channel) 
    if bot.gateway.finishedMemberFetching(guildz):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()
bot.gateway.run()
for memberID in bot.gateway.session.guild(guildz).members:
    print(memberID)
    memberz.append(memberID)
for x in memberz:
    try:
        rand = random.randint(0,20)
        if rand == 20:
            print(f'Sleeping for 45 seconds to prevent rate-limiting.')
            time.sleep(45)
            print(f'Done sleeping!')
        time.sleep(int(timez))
        newDM = bot.createDM([f"{x}"]).json()["id"]
        bot.sendMessage(newDM, f"{messag}")
        print(f'DMed {x}.')
    except Exception as E:
        print(E)
        print(f'Couldn\'t DM {x}.')
