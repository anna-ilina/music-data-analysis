import requests 
import json
import os
from authorizationInformation import watson_service_credentials

#NOTE: Watson NLU doesn't support sentiment analysis for Spanish, so we force it to interpret lyrics as english
# for some songs this will likely yield innaccurate results for songs which are in spanish or spanish+english
# cite: https://console.bluemix.net/docs/services/natural-language-understanding/language-support.html#spanish
#   todo: count how many songs in dataset are spanish

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
    emotions = r.json()['emotion']['document']['emotion'] 
    # ^^ something like {u'anger': 0.041796, u'joy': 0.563273, u'sadness': 0.32665, u'fear': 0.033387, u'disgust': 0.022637}
    return emotions


def main():

    with open("assembledLyricsWithEmotions.csv", "wb") as outFile:
        with open("assembledLyrics.csv", "rb") as inFile:
            lines = inFile.readlines()
            inFileHeader = lines[0].strip()
            outFileHeader = inFileHeader + "," + ','.join(['anger', 'joy', 'sadness', 'fear', 'disgust']) + "\n"
            outFile.write(outFileHeader)

            for line in lines[1:]:         # skip header
                line = line.strip()         # remove whitespace
                splitLine = line.split(",")
                lyrics = splitLine[4]
                lyrics = lyrics.strip()
                lyrics = lyrics.replace("\n", " ")
                lyrics = lyrics.decode('ascii','ignore')

                anger = "NA"
                joy = "NA"
                sadness = "NA"
                fear = "NA"
                disgust = "NA"

                if lyrics == "" or lyrics.isspace() or lyrics == "NA" or len(lyrics) < 100:
                    pass
                else:
                    try:
                        emotions = quantifyEmotion(lyrics)
                        print(emotions)
                        anger = emotions['anger']
                        joy = emotions['joy']
                        sadness = emotions['sadness']
                        fear = emotions['fear']
                        disgust = emotions['disgust']
                    except:
                        print(line)
                        print("Watson NLU failed to get emotions for these lyrics!")    #This didn't fail for any of 5798 songs tested

                outFile.write(line + "," + ','.join([str(x) for x in [anger, joy, sadness, fear, disgust]]) + "\n")


if __name__ == '__main__':
    main()
