from urlib import request
# variables

artist = 'Taylor Swift'
song_title = 'Delicate'
keywords = {'drink'}

url = 'https://api.lyrics.ovh/v1/'+ artist + '/' + title

#fetch lyrics
response = request.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']

# determine how many keywords there in lyircs
statstics = {}

for keyword in keywords:
    statstics[keyword] = lyrics.count(keyword)

print(statstics)
