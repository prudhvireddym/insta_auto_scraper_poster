import os
from instabot import Bot 
import random
import shutil

bot = Bot() 


username ="travelbloggerdaily"
password =""
path = os.getcwd()+"\\media\\travelbloggerdaily"
scraper_cmnd ="instagram-scraper traveldecided,paradise.global,natureegeo,locations_unknown,explorerfervor,discovery_earth,tasteinhotels,luxurytravelandhotels --latest --maximum 2 --media-metadata"

def delete_folder(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
delete_folder(path)
os.chdir(path)
os.system(scraper_cmnd)

def upload(username,password,path):
    bot.login(username = username,  
          password = password) 

    root= path


    media = []
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            media.append(os.path.join(path, name))


    while True:
        i =random.choice(media)
        if "jpg" in i:
            break
    print(i)
    account = i.split("\\")[-2]
    print(account)
    caption ="🗺️ Guess the place?\n\n-\nFollow us Today! 👉🏼 @travelbloggerdaily\nFollow us Today! 👉🏼 @travelbloggerdaily\n-\n\n📷 Repost from @"+account+"\n\n#traveling #instatravel #travelgram #travelblogger #traveltheworld #mytravel #shetravels #worldphotography #lovetraveling #foodforthesoul #travelblogging #phototravel #borntotravel #travelinggram #gymfood #naturalphotography #livetotravel #travelisfun #weekendtravel"
    bot.upload_photo(i,caption = caption)


upload(username,password,path)
