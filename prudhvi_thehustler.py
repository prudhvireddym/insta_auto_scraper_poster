import os
from instabot import Bot 
import random
import shutil

bot = Bot() 


username ="prudhvi_thehustler"
password =""
path = os.getcwd()+"\\media\\prudhvi_thehustler"
scraper_cmnd ="instagram-scraper savetoinvest,d_inspiration_vibes,investingsimplified,age_of_attitude,illionare_codes,billionaresage --latest --maximum 2 --media-metadata"

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
    caption ="💲 What are your goals for 2020?\n\n-\nFollow me Today! 👉🏼 @prudhvi_thehustler\nFollow me Today! 👉🏼 @prudhvi_thehustler\n-\n\n📷 Repost from @"+account+"\n#entrepreneur #motivation #motivationalquotes #entrepreneurship #investment #investing #investor #youngentrepreneur #entrepreneurgoals #mymotivation #instamotivation #entrepreneurialmindset #motivation💪 #entrepreneurmind #youngentrepreneurs #successmotivation #motivationnation #entrepreneurtip #investnow #bestinvestment #instaentrepreneur #impactinvesting #savetoinvest #motivationforsuccess #investmentplan #motivationisthekey #findyourmotivation #entrepreneursrock #dailymotivation #extrememotivation"
    bot.upload_photo(i,caption = caption)


upload(username,password,path)
