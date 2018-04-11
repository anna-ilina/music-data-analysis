with open("AssembledLyrics.csv", "rb") as inFile:
	with open("AssembledLyricsCleaned.csv", "wb") as outFile:
		lines = inFile.readlines()
		outFile.write(lines[0])	#write header
		for line in lines[1:]:
			lineSplit = line.split(",")
			lyrics = lineSplit[4]
			if lyrics == "NA" or lyrics == "NA\n" or lyrics.isspace():
				pass 
			else:
				outFile.write(line)