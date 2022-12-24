from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time, os, sys, json

wt = (
    """                                                
  [[ye]]*   )                              (        
[[re]]` )  /(    )        (      )         )\    )  
 [[ye]]( )(_))( /(   (    )\    (      (  ((_)( /(  
[[re]](_(_()) )(_))  )\ )((_)   )\  '  )\  _  )(_)) 
[[gr]]|_   _|((_)_  _(_/( (_) _((_))  ((_)| |((_)_  
  [[gr]]| |  / _` || ' \))| || '  \()/ _ \| |/ _` | 
  |_|  \__,_||_||_| |_||_|_|_| \___/|_|\__,_| 
             [[re]][erfan4lx][[ye]]
        [[re]][https://erfan4lx.com][[ye]]
        [[re]][youtube.com/erfan4lx][[ye]]
  
  github.com/erfan4lx  
  instagram.com/_erfan4lx_
  t.me/erfan4lx
    """
)

print(wt)
time.sleep(3)

COLORS = {
    "re": "\u001b[31;1m",
    "gr": "\u001b[32m",
    "ye": "\u001b[33;1m",
}
re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
clearType = input('terminal or cmd. (t/c): ').lower()
if clearType == 't':
    clear = lambda:os.system('clear')
elif clearType == 'c':
    clear = lambda:os.system('cls')
else:
    print('Invalid input!!!')
    sys.exit()
    
if sys.version_info[0] < 3:
    telet = lambda :os.system('pip install -U telethon')
elif sys.version_info[0] >= 3:
    telet = lambda :os.system('pip3 install -U telethon')

telet()
time.sleep(1)
clear()

if os.path.isfile('erfan4lx_log.txt'):
    with open('erfan4lx_log.txt', 'r') as r:
        data = r.readlines()
    api_id = data[0]
    api_hash = data[1]

else:
    api_id = input('Enter api_id: ')
    api_hash = input('Enter api_hash: ')
    with open('erfan4lx_log.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('erfan4lx', api_id, api_hash)

async def main():
    chats = []
    channel = []
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=2000,
        hash=0
    ))
    chats.extend(result.chats)
    for a in chats:
        try:
            if True:
                channel.append(a)
        except:
            continue
    a = 0
    print(ye+'Choose a channel to scrape: ')
    for i in channel:
        print(gr+'['+str(a)+']', i.title)
        a += 1
    op = input(ye+'Enter a number: ')
    if op == '':
        print(ye+'Ok. skipping...')
        time.sleep(1)
        sys.exit()
    else: 
        pass
    opt = int(op)
    print('')
    print(ye+'[+] Fetching Members...')
    time.sleep(1)
    target_group = channel[opt]
    all_participants = []
    mem_details = []
    all_participants = await client.get_participants(target_group)
    for user in all_participants:
        try:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                firstname = user.first_name
            else:
                firstname = ""
            if user.last_name:
                lastname = user.last_name
            else:
                lastname = ""

            new_mem = {
                'uid': user.id,
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'access_hash': user.access_hash
            }
            mem_details.append(new_mem)
        except ValueError:
            continue
    
    with open('erfan4lx_members.txt', 'w') as w:
        json.dump(mem_details, w)
    time.sleep(1)
    print(ye+'Please wait.....')
    time.sleep(3)
    done = input(gr+'[+] Members scraped successfully.')
    await client.disconnect()
    print(wt)
    time.sleep(3)
    sys.exit()

with client:
    client.loop.run_until_complete(main())
