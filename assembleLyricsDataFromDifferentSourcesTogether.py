# get 1960-1964 data from: https://github.com/mikkelkrogsholm/billboard
# get 1965-2015 data from: https://www.kaggle.com/rakannimer/billboard-lyrics/data
# get 2016-2017 data from: get 2016-2017 top 100 billboard songs from spotify web api, get lyrics from PyLyrics (lyrics.wikia.com)

# Want excel format to be: 
# rank, song, artist, year, lyrics

outFilename = "assembledLyrics.csv"
with open(outFilename, "wb") as outFile:
	outFile.write("Rank,Song,Artist,Year,Lyrics\n")


	# Get 1960-1964 lyrics:
	with open("billboard_lyrics_1960-2016.csv", "rb") as inFile:
		lines = inFile.readlines()
		for line in lines[1:]: 	#ignore header
			line = line.split(",")
			rankInt = int(line[0])
			if rankInt % 100 == 0:
				rank = str(100)		# otherwise multiples of 100 will go to 0
			else:
				rank = str(rankInt % 100)
			#rank = rank if int(rank) < 100 else str((int(rank) % 100) + 1)
			#rank = str(int(line[0]) % 100) + 1
			#rank = "1" if rank == "0" else rank 	#otherwise mod turns 100 --> 0
			title = line[1]
			artist = line[2]
			year = line[3]
			lyrics = line[4]
			if int(year) > 1964:	# import only 1960-1964 lyrics from this dataset
				break
			outFile.write(",".join([rank, title, artist, year, lyrics]))
		
	# Get 1965-2015 lyrics:
	#import all songs from this dataset
	with open("billboard_lyrics_1964-2015.csv", "rb") as inFile:
		lines = inFile.readlines()
		for line in lines[1:]: 	#ignore header; 
			line = line.split(",")
			outFile.write(",".join(line[:-1]) + "\n") # exclude last column from this datasource

	# Get 2016 lyrics:
	#import all songs from this dataset
	with open("lyricsBillboard2016.csv", "rb") as inFile:
		lines = inFile.readlines()
		for line in lines[1:]: 	#ignore header; 
			outFile.write(line)

	# Get 2017 lyrics:
	#import all songs from this dataset
	with open("lyricsBillboard2017.csv", "rb") as inFile:
		lines = inFile.readlines()
		for line in lines[1:]: 	#ignore header; 
			outFile.write(line)
