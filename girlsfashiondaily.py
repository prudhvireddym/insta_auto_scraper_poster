import os
from instabot import Bot 
import random
import shutil

bot = Bot() 


username ="girlsfashiondaily"
password =""
path = os.getcwd()+"\\media\\girlsfashiondaily"
scraper_cmnd ="instagram-scraper fashionexe,instaglamday,lokoutfit,womenstyleusa --latest --maximum 2 --media-metadata"

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
    caption ="💃 Tag someone who would love this\n\n-\nFollow us Today! 👉🏼 @girlsfashiondaily\nFollow us Today! 👉🏼 @girlsfashiondaily\n-\n\n📷 Repost from @"+account+"\n#makeup #instafashion #hairstyle #fashionstyle #ilovefashion #professionalmakeup #fashionhair #fashionwoman #simplemakeup #newfashion #fashionaddicted #bridalhairstyle #blackhairstyles #makeupandhairdo #hairstylesforwomen #makeupusa #voguefashion #lovehairstyle #newlookfashion #womanfashionstyle #makeupeffects #ecofashionista #welovemakeup #fashionstyles4love #tasteformakeup #makeupjob #youcammakeup #basicmakeup #fashionproject"
    bot.upload_photo(i,caption = caption)


upload(username,password,path)
