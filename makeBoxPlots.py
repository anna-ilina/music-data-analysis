import matplotlib.pyplot as plt
import numpy as np

#todo: make this program more generic

def makeBoxPlots(energy, acousticness, danceability, valence, instrumentalness):
	
	data = [energy, acousticness, danceability, valence, instrumentalness]
	plt.figure()
	plt.boxplot(data)
	x = np.arange(6)
	plt.xticks(x, ("", "energy", "acousticness", "danceability", "valence", "instrumentalness"))
	plt.title("Distribution of Several Attributes (Range 0-1) for Global Top 50 Songs")
	plt.show()