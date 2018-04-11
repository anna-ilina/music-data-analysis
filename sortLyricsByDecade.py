import os

decades = ["1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
for d in decades:
	if not os.path.exists(d):
		os.makedirs(d)


with open("assembledLyrics.csv", "rb") as inFile:	#this contains lyrics from 1960 - 2017
	lines = inFile.readlines()
	for line in lines[1:]: 	#ignore header
		line = line.split(",")
		year = int(line[3])
		rank = line[0]
		lyrics = line[4]
		if year >= 1960 and year < 1970:
			with open(os.path.join("1960s", rank + ".txt"), "wb") as outFile:
				outFile.write(lyrics)
		elif year < 1980:
			with open(os.path.join("1970s", rank + ".txt"), "wb") as outFile:
				outFile.write(lyrics)
		elif year < 1990:
			with open(os.path.join("1980s", rank + ".txt"), "wb") as outFile:
				outFile.write(lyrics)
		elif year < 2000:
			with open(os.path.join("1990s", rank + ".txt"), "wb") as outFile:
				outFile.write(lyrics)
		elif year < 2010:
			with open(os.path.join("2000s", rank + ".txt"), "wb") as outFile:
				outFile.write(lyrics)
		elif year < 2020:
			with open(os.path.join("2010s", rank + ".txt"), "wb") as outFile:
					outFile.write(lyrics)
