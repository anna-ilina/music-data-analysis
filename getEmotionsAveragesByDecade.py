import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

emotions1960s = pd.read_csv("1960s_lyrics_analysis.csv", sep='\s*,\s*', engine='python')
emotions1970s = pd.read_csv("1970s_lyrics_analysis.csv", sep='\s*,\s*', engine='python')
emotions1980s = pd.read_csv("1980s_lyrics_analysis.csv", sep='\s*,\s*', engine='python')
emotions1990s = pd.read_csv("1990s_lyrics_analysis.csv", sep='\s*,\s*', engine='python')
emotions2000s = pd.read_csv("2000s_lyrics_analysis.csv", sep='\s*,\s*', engine='python')
emotions2010s = pd.read_csv("2010s_lyrics_analysis.csv", sep='\s*,\s*', engine='python')
# print(emotions1960s.head())
# print(emotions1960s['joy'][:5])

def getAverages(decade, decadeDescription,outFile):
	print(decadeDescription)
	outFile.write(decadeDescription)
	for emotion in ['anger', 'joy', 'sadness', 'fear', 'disgust']:
		print(emotion)
		mean = np.mean(decade[emotion])
		median = np.median(decade[emotion])
		stdev = np.std(decade[emotion])
		outFile.write("," + str(median))
		# print("mean={}".format(mean))
		# print("median={}".format(median))
		# print("stdev={}".format(stdev))
	print("")
	outFile.write("\n")


outFile = open("emotionsByDecade_median.csv", "wb")
outFile.write("decade,anger,joy,sadness,fear,disgust\n")

getAverages(emotions1960s, "1960s", outFile)
getAverages(emotions1970s, "1970s", outFile)
getAverages(emotions1980s, "1980s", outFile)
getAverages(emotions1990s, "1990s", outFile)
getAverages(emotions2000s, "2000s", outFile)
getAverages(emotions2010s, "2010s", outFile)

outFile.close()

# for decade in [emotions1960s, emotions1970s, emotions1980s, emotions1990s, emotions2000s, emotions2010s]:
# 	for emotion in ['anger', 'joy', 'sadness', 'fear', 'disgust']:
# 		mean = np.mean(decade[emotion])
# 		median = np.median(decade[emotion])
# 		stdev = np.std(decade[emotion])


	# avgAnger = np.mean(decade['anger'])
	# avgJoy = np.mean(decade['joy'])
	# avgSadness = np.mean(decade['sadness'])
	# avgFear = np.mean(decade['fear'])
	# avgDisgust = np.mean(decade['disgust'])
	# print([avgAnger, avgJoy, avgSadness, avgFear, avgDisgust])




#{u'anger': 0.041796, u'joy': 0.563273, u'sadness': 0.32665, u'fear': 0.033387, u'disgust': 0.022637}

