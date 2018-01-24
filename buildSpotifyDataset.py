# Anna Ilina 23 2017

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from classes import *
from authorizationInformation import CLIENT_ID, CLIENT_SECRET


def getTrackDataFromPlaylist(playlistName, playlistOwner, clientID, clientSecret):

	# set authorization credentials
	clientCredentialsManager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
	spotify = spotipy.Spotify(client_credentials_manager = clientCredentialsManager) # spotify client object

	# get information (JSON format) on the "Canada Hot Hits" album
	results = spotify.user_playlist(playlistOwner, playlistName)

	# get track data
	numTracks = results["tracks"]["total"]
	trackItems = results["tracks"]["items"]

	print "Playlist name: " + results['name']
	print "Description: " + results['description']
	print "Number of followers: " + str(results['followers']['total'])
	print "Number of tracks: " + str(numTracks)
	print ""

	tracks = []
	counter = 1
	for item in trackItems:
		t = Track()
		t.name = item['track']['name']#.encode("cp850")
		t.URI = item['track']['uri']
		t.popularity = item['track']['popularity']
		t.dureationMs = item['track']['duration_ms']
		t.availableMarkets = item['track']['available_markets']
		t.album = Album(item['track']['album']['name'], item['track']['album']['uri'])
		artists = []
		for artist in item['track']['artists']:
			a = Artist(artist['name'], artist['uri'])
			artistMoreDetails = spotify.artist(artist['uri'])
			a.genres = artistMoreDetails['genres']
			a.popularity = artistMoreDetails['popularity']
			a.numFollowers = artistMoreDetails['followers']['total']
			artists.append(a)
		t.artists = artists
		tracks.append(t)
		if counter % 5 == 0:
			print "finished getting data for %s/%s tracks" % (counter, numTracks)
		counter += 1
	print "finished getting data for %s/%s tracks" % (counter, numTracks)
	
	return tracks

def printTracks(tracks):
	for i in range(len(tracks)):
		print(tracks[i])
		print ""

def main():
	canadaHotHitsPlaylistURI = "37i9dQZF1DWXT8uSSn6PRy"
	user = "Spotify"
	tracks = getTrackDataFromPlaylist(canadaHotHitsPlaylistURI, user, CLIENT_ID, CLIENT_SECRET)
	printTracks(tracks)

if __name__ == '__main__':
	main()