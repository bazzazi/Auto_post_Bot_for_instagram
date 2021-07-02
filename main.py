###############           #########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #



# Auto post Bot for instagram
# By Mohammad Ali Bazzazi
# by only drag and drop, post an image or video in your inta account Easily
# Don't forget to follow me
# enjoy  :)

# import Libraries
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, time, pyttsx3
from instabot import Bot

import info     # which has insta username and password

# create an instance of Bot
bot = Bot()
# login to insta account
bot.login(username=info.USERNAME, password=info.PASSWORD)

# create file handler class
class File_handler(FileSystemEventHandler):

    # define on_modified method (if src path changes this method will run)
    def on_modified(self, event):

        # say to user file detected
        self.speech("File detected")

        # check and list all from_folder's files
        for filename in os.listdir(from_folder):

            # file(image or video) path
            src = from_folder + "/" + filename

            # say to user to enter caption
            self.speech("please type your Caption")
            mycaption = input("Please type your Caption: ")


            # post image which is in src path (if you want to post video, replace upload_video with upload_photo)
            # remember image extension should be .jpg
            bot.upload_photo(src, caption=mycaption)

            # say success
            self.speech("upload successful")

            # move file in src path, into to_folder path, and remove .REMOVE_ME extension.
            os.rename(src + ".REMOVE_ME", to_folder + "/" + filename.removesuffix(".REMOVE_ME"))

    # define speech method
    def speech(self, word):
        # initialize engine
        engine = pyttsx3.init()
        # set reading speed
        engine.setProperty('rate', 120)
        # read word
        engine.say(word)
        engine.runAndWait()


# path to folder 1 (origin)
from_folder = "path of folder 1"

# path to folder 2 (destination)
to_folder = "path of folder 2"


# create instances
handler = File_handler()
observer = Observer()

# set schedule
observer.schedule(handler, from_folder, recursive=True)


observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
