# Could explore:
# - most popular songs by year


songs = {}
availableLyrics = {}
countMissingLyrics = 0
numSongs = 0

with open('assembledLyrics.csv', 'rb') as inFile:
	lines = inFile.readlines()
	numSongs = len(lines) - 1
	for line in lines[1:]: 	#ignore header
		line = line.split(',')
		year = line[3]
		if year in songs:
			songs[year] += 1
		else:
			songs[year] = 1			
		lyrics = line[4]
		if lyrics == "NA" or lyrics == "NA\n" or lyrics.isspace():
			countMissingLyrics += 1
			#print(lyrics)
		else:
			if year in availableLyrics:
				availableLyrics[year] += 1
			else:
				availableLyrics[year] = 1

	print lines[2].split(",")

#songs = sorted(songs)

for key in sorted(songs):
	print("%s %s") % (key, songs[key])

print numSongs
print countMissingLyrics
print countMissingLyrics / float(numSongs)

for key in sorted(availableLyrics):
	print("%s %s") % (key, availableLyrics[key])
