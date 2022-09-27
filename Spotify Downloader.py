import os

#playlist = input("Input the playlist link: ")

#song = input("Input the song link: ")

print("MADE WITH LOVE BY AL3xutzu34 <3")
input("Press Enter to enter in app")

def playlistdl():
    os.system(f"spotdl {playlist}")

def songdl():
    os.system(f"spotdl {song}")


while True:
    q = input("What do you want to add? \n 1) Playlist. 2) Song. [1/2]? : ")
    if q == "1":
        path = input("\nInput the music folder: ")
        move = input("\nWhat do you want to do with your existing files? \n\n 1) Move all the existing songs in a new/existing folder \n\n 2) Add the playlist contents and delete the old existing songs \n\n 3) Add the playlist contents to the folder without deleting all the existing songs \n\n Select [1/2/3]: ")
        if move == "1":
            os.chdir(path)
            foldersee = input("You want to see all the names of other folders in the directory? [1 = Yes 2 = No]: ")
            if foldersee == "1":
                directories = list(filter(os.path.isdir, os.listdir(path)))
                print(directories)
            playlistname = input('\n\nInput the name for the new folder\n(if the folder exists the existing songs will add to that folder)\n(use double commas ["] if you use space in the name): ')
            os.system(f"mkdir {playlistname}")
            os.system(f"move *.mp3 {playlistname}")
            playlist = input("\n\nInput the playlist link: ")
            playlistdl()
            break
        elif move == "2":
            os.chdir(path)
            playlist = input("\n\nInput the playlist link: ")
            deletecontents = os.listdir(path)
            for item in deletecontents:
                if item.endswith(".mp3"):
                    os.remove(os.path.join(path, item))
            playlistdl()
            break
        elif move == "3":
            os.chdir(path)
            playlist = input("\n\nInput the playlist link:")
            playlistdl()
            break
    elif q == "2":
        path = input("\n\nInput the music folder: ")
        song = input("\n\nInput the song link: \n")
        os.chdir(path)
        songdl()
        break