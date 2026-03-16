
'''
🧠 PRACTICE QUESTION (Python-Friendly Version)
🎧 Music Streaming App (Getters & Setters ONLY)

You are building a Music Streaming App.

The program will manage users and playlists.
You must use getters and setters to access and modify data.

⚠️ Do NOT access attributes directly outside the class.

🔹 PART 1: CLASS DEFINITIONS
1️⃣ Class: User
Attributes (keep them PRIVATE):
_username        # string
_email           # string
_is_premium      # boolean (default = False)

Methods you MUST implement:

Getters
get_username()        # returns username
get_email()           # returns email
is_premium()          # returns True or False


Setters
set_email(new_email)
    # only update if "@" is in new_email

set_premium(status)
    # status must be True or False

'''

class User():
    def __init__(self,username=None,email=None,premium=None):
        self.username=username
        self.email=email
        self.premium=premium
    
    def collectdata(self):
        self.username=input("pls enter username:")
        self.email=input("pls enter your email:")
        self.premium=input("do you have a premium account:")
        self.setpremium(self.premium)

    def setupdateemail(self):
        updateemail=input("pls enter your new email")
        if "@" in updateemail:
            self.email=updateemail
        else:
            print("Invalid email")
    
    def setpremium(self,value):
        if value=="yes":
            self.premium=True
        else:
            self.premium=False 
    
    def get_username(self):
        return self.username
    def get_email(self):
        return self.email
    def getispremium(self):
        return self.premium

'''
2️⃣ Class: Playlist
Attributes (PRIVATE):
_name       # string
_songs      # list of strings
_owner      # User object (HAS-A relationship)

Methods you MUST implement:

Getters

get_name()            # returns playlist name
get_song_count()      # returns number of songs
get_owner_username()  # returns owner's username (via getter)


Setters / Behaviour

add_song(song_name)
    # only add if song_name is not empty

remove_song(song_name)
    # only remove if song exists in list
'''
class Playlist():
    def __init__(self,owner,playlistname=None):
        self.playlistname=playlistname
        self.song=[]
        self.owner=owner
       
    def nameplaylist(self):
        self.playlistname=input("pls enter playlist name")
    
    def addsongname(self):
        songname=input("pls enter song name:")
        if songname == "":
            print("song can't be empty")
        else:
            self.song.append(songname)
            print(f"{songname} is added!")
        print(self.song)
        
    def removesongname(self):
        songname=input("pls enter a song name")
        if songname in self.song:
            self.song.remove(songname)
        print(f"{songname} was removed")
        print(self.song)

    
    def get_name(self):
        return self.playlistname
    def getsong_count(self):
        count=0
        for song in self.song:
            count+=1
        return count 
    def get_username(self,username):
        print(self.owner.getusername())
        
    
print("welcome to music streaming app")
options=["create user","create playlist","add song to playlist","view playlist"]
objects={}
playlists={}
while True:
    for i,option in enumerate(options):
        print(i+1,option)

    user=int(input("pls enter a number"))
    
    if user==1:
        person=User()
        person.collectdata()
        objects[person.username]=person
    
   
    elif user==2:
        playlist1=Playlist(person,None)
        playlist1.nameplaylist() 
        playlists[playlist1.get_name()]=playlist1
    
    elif user==3:
        playlistname= input("pls enter playlist name:")
        if playlistname in playlists:
            playlists[playlistname].addsongname()
        else:
            print("playlist not found")
    
    elif user==4:
        
        for name, playlist in playlists.items():
            print("Playlist name:", name)
            print("Owner:", playlist.owner.get_username())
            print("Songs:", playlist.song)
            break 



# user1=User()
# playlist1=Playlist("raj",user1)
# playlist1



