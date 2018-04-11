import requests 
import json
import os
from authorizationInformation import watson_service_credentials

#NOTE: Watson NLU doesn't support sentiment analysis for Spanish, so we force it to interpret lyrics as english
# for some songs this will likely yield innaccurate results for songs which are in spanish or spanish+english
# cite: https://console.bluemix.net/docs/services/natural-language-understanding/language-support.html#spanish
#   todo: count how many songs in dataset are spanish

#2010s      87
#2000s      97
#1990s      97
#1980s      100
#1970s      92
#1960s      90

def quantifyEmotion(text):
    auth = (watson_service_credentials['username'], watson_service_credentials['password'])
    url = "https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-03-16"
    data = {
      "html": text,
      "language": "en",
      "features": {
        "emotion": {}
      }
    }
    data = json.dumps(data)
    headers = {"Content-Type": "application/json"}

    r = requests.post(url, headers=headers, data=data, auth=auth)
    #print(r.text)
    emotions = r.json()['emotion']['document']['emotion'] 
    #print(emotions)
    # ^^ something like {u'anger': 0.041796, u'joy': 0.563273, u'sadness': 0.32665, u'fear': 0.033387, u'disgust': 0.022637}
    return emotions

def main():
    targetDir = "billboard2017_lyrics" # this directory has text files with lyrics to songs from a playlist
    numSongLyricsAnalyzed = 0
    noLyrics = []
    outFile = open(targetDir+"_lyrics_analysis.csv", "wb")
    outFile.write("folderName, fileName, length (chars), rank, anger, joy, sadness, fear, disgust\n")
    for lyricsFile in os.listdir(targetDir):
        print(lyricsFile)
        if lyricsFile.endswith(".txt"):
            with open(os.path.join(targetDir, lyricsFile)) as inFile:
                rank = os.path.splitext(os.path.basename(lyricsFile))[0]
                lines = inFile.readlines()
                lyrics = " ".join(lines)
                lyrics = lyrics.strip()
                lyrics = lyrics.replace("\n", " ")
                lyrics = lyrics.decode('ascii','ignore')
                length = len(lyrics)
                print(os.path.join(targetDir, lyricsFile))
                print(rank)
                print(lyrics)
                print("")
                

                if lyrics == "" or lyrics.isspace() or lyrics == "NA\n" or length < 10:
                    noLyrics.append(rank)
                    pass
                else:
                    emotions = quantifyEmotion(lyrics)
                    print(emotions)
                    #emotions = {u'anger': 0.041796, u'joy': 0.563273, u'sadness': 0.32665, u'fear': 0.033387, u'disgust': 0.022637}
                    anger = emotions['anger']
                    joy = emotions['joy']
                    sadness = emotions['sadness']
                    fear = emotions['fear']
                    disgust = emotions['disgust']
                    numSongLyricsAnalyzed += 1
                    outFile.write("{},{},{},{},{},{},{},{},{}\n".format(targetDir, lyricsFile, 
                        length, rank, anger, joy, sadness, fear, disgust))
    outFile.close()
    print(numSongLyricsAnalyzed)
    print(noLyrics)

if __name__ == '__main__':
    main()
