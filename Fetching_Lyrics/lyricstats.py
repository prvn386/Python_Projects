from urlib import request
# variables

artist = 'Taylor Swift'
song_title = 'Delicate'
keywords = {'drink'}

url = 'https://api.lyrics.ovh/v1/'+ artist + '/' + title

#fetch lyrics
response = request.get(url)
