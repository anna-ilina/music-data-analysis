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

#Get counts for missing songs per year (out of 100)
print ("Get count for missing songs per year (out of 100)")
for key in sorted(songs):
	print("%s %s") % (key, songs[key])

#Get counts for missing song lyrics per year (out of 100)
print ("\nGet counts for missing song lyrics per year (out of 100)")
for key in sorted(availableLyrics):
	print("%s %s") % (key, availableLyrics[key])

print ("\nNumber of songs in our 1960-2017 dataset: " + str(numSongs))
print ("Number of songs with missing lyrics in our 1960-2017 dataset: " + str(countMissingLyrics))
print ("Percentage of songs with missing lyrics in our 1960-2017 dataset: " + str(countMissingLyrics / float(numSongs)))
