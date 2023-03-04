import os, sys, time, threading, json
try:
    from colorama import Fore, Style
    import httpx
except ImportError:
    sys.exit("down-4ever | Failed to import requirements, please run `pip install -r requirements.txt`.")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)

print_slow(Fore.BLUE + """\

                                                                                                                                                                                                                 
            dddddddd                                                                                                                                                                                             
            d::::::d                                                                                                  444444444                                                                                  
            d::::::d                                                                                                 4::::::::4                                                                                  
            d::::::d                                                                                                4:::::::::4                                                                                  
            d:::::d                                                                                                4::::44::::4                                                                                  
    ddddddddd:::::d    ooooooooooo wwwwwww           wwwww           wwwwwwwnnnn  nnnnnnnn                        4::::4 4::::4      eeeeeeeeeeee  vvvvvvv           vvvvvvv eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  dd::::::::::::::d  oo:::::::::::oow:::::w         w:::::w         w:::::w n:::nn::::::::nn                     4::::4  4::::4    ee::::::::::::ee v:::::v         v:::::vee::::::::::::ee  r::::rrr:::::::::r  
 d::::::::::::::::d o:::::::::::::::ow:::::w       w:::::::w       w:::::w  n::::::::::::::nn                   4::::4   4::::4   e::::::eeeee:::::eev:::::v       v:::::ve::::::eeeee:::::eer:::::::::::::::::r 
d:::::::ddddd:::::d o:::::ooooo:::::o w:::::w     w:::::::::w     w:::::w   nn:::::::::::::::n --------------- 4::::444444::::444e::::::e     e:::::e v:::::v     v:::::ve::::::e     e:::::err::::::rrrrr::::::r
d::::::d    d:::::d o::::o     o::::o  w:::::w   w:::::w:::::w   w:::::w      n:::::nnnn:::::n -:::::::::::::- 4::::::::::::::::4e:::::::eeeee::::::e  v:::::v   v:::::v e:::::::eeeee::::::e r:::::r     r:::::r
d:::::d     d:::::d o::::o     o::::o   w:::::w w:::::w w:::::w w:::::w       n::::n    n::::n --------------- 4444444444:::::444e:::::::::::::::::e    v:::::v v:::::v  e:::::::::::::::::e  r:::::r     rrrrrrr
d:::::d     d:::::d o::::o     o::::o    w:::::w:::::w   w:::::w:::::w        n::::n    n::::n                           4::::4  e::::::eeeeeeeeeee      v:::::v:::::v   e::::::eeeeeeeeeee   r:::::r            
d:::::d     d:::::d o::::o     o::::o     w:::::::::w     w:::::::::w         n::::n    n::::n                           4::::4  e:::::::e                v:::::::::v    e:::::::e            r:::::r            
d::::::ddddd::::::ddo:::::ooooo:::::o      w:::::::w       w:::::::w          n::::n    n::::n                           4::::4  e::::::::e                v:::::::v     e::::::::e           r:::::r            
 d:::::::::::::::::do:::::::::::::::o       w:::::w         w:::::w           n::::n    n::::n                         44::::::44 e::::::::eeeeeeee         v:::::v       e::::::::eeeeeeee   r:::::r            
  d:::::::::ddd::::d oo:::::::::::oo         w:::w           w:::w            n::::n    n::::n                         4::::::::4  ee:::::::::::::e          v:::v         ee:::::::::::::e   r:::::r            
   ddddddddd   ddddd   ooooooooooo            www             www             nnnnnn    nnnnnn                         4444444444    eeeeeeeeeeeeee           vvv            eeeeeeeeeeeeee   rrrrrrr            
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 
                    """)

time.sleep(1)

print(Style.RESET_ALL)
print("down-4ever | Loaded")

if os.path.getsize('proxies.txt') == 0:
    sys.exit(Fore.RED + "down-4ever | You have no proxies. You need to add proxies in the proxies.txt file, otherwise down-4ever won't work. Read the github page if you don't understand.") 

if os.path.getsize('config.json') == 0:
    sys.exit(Fore.RED + "down-4ever | Your config.json file is empty/doesn't exist, so I don't know what to do. Read the Getting Started page on our Github repo if you don't understand.") 

f = open('config.json')
data = json.load(f)

if data["url"] == "Up-4ever url here":
    sys.exit(Fore.RED + "down-4ever | Your config.json file exists, but needs to be updated. Please read the github page and update the file.")

if data["proxytype"] == "proxy type, input socks4, socks5, http, or https":
    sys.exit(Fore.RED + "down-4ever | Your config.json file exists, but needs to be updated. Please read the github page and update the file.")

if data["threads"] == "thread count. should be a high number to run fast, beware it will slow down your pc the higher the number.":
    sys.exit(Fore.RED + "down-4ever | Your config.json file exists, but needs to be updated. Please read the github page and update the file.")

if "https://upload-4ever.com" not in data["url"]:
    sys.exit(Fore.RED + "down-4ever | Your config.json file is OK, but your url isn't an upload-4ever.com link. Remember to not input a shortlink, but the full download link.")

# def hit():
#     print("hi")

threads = data["threads"]

# while True:
#     if threading.active_count() <= threads:
#         threading.Thread(target=hit).start()

sys.exit(Fore.RED + "down-4ever | Couldn't download backbone assets.")