from PyLyrics import *
import os

#could also look at musixmatch api for lyrics

def main():
	# lyricsDir = "billboard2017_lyrics"
	year = 2016
	with open("songsBillboard2017.csv", "r") as inFile:
		with open("lyricsBillboard2017.csv", "w") as outFile:
			outFile.write("Rank,Song,Artist,Year,Lyrics\n")
			songs = []
			lines = inFile.readlines()
			countSuccesses = 0
			rank = 0
			for line in lines[1:]:	#skip header
				rank += 1
				lyrics = ""
				line = line.split(",")
				songName = line[0]
				songArtist = line[1]
				songs.append((songName, songArtist))
				try:
					lyrics = PyLyrics.getLyrics(songArtist, songName)
					countSuccesses += 1
				except:
					try: 
						bracketIndex = songName.find('(')	
						if bracketIndex != -1:
							songName = songName[:bracketIndex]
						bracketIndex = songName.find('-')	
						if bracketIndex != -1:
							songName = songName[:bracketIndex]
						songName = songName.strip() # remove whitespace
						#print(songName)
						songName = songName.replace("''", "'") #get rid of double brackets	
						if songName[0] == "'":
							songName = songName[1:] #get rid of quotes surrounding song title
						if songName[-1] == "'":
							songName = songName[:-1] #get rid of quotes surrounding song title
						#songName = songName.title() #capitalize first letter of each word
						#print(songName)
						#print(songArtist)
						lyrics = PyLyrics.getLyrics(songArtist, songName)
						countSuccesses += 1
					except:
						print ("Unable to get lyrics for song " + songName + " by " + songArtist)
				# if lyrics != "":
				# 	with open(os.path.join(lyricsDir, songName + ".txt"),'w') as outFile:
				# 		outFile.write(lyrics)
				lyrics = lyrics.replace("\n", "")
				lyrics = lyrics.replace(",", "")
				outFile.write(",".join([str(rank), songName, songArtist, str(year), lyrics]) + "\n")

	print ("countSuccesses = " + str(countSuccesses))


if __name__ == '__main__':
    main()