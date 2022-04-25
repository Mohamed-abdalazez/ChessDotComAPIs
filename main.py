from chessdotcom import get_player_profile, get_player_game_archives

username = 'M-abdalazez' #Replace it with your username

def getInfo(username):
    data = get_player_profile(username).json;
    Info = open('Info.txt', 'w')
    print(data, file = Info)
    Info.close()


def getArchives(username):
    data = get_player_game_archives(username).json;
    Archives = open('Archives.txt', 'w')
    print(data, file = Archives)
    Archives.close()

getArchives(username)
getInfo(username)