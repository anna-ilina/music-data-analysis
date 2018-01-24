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

	print "Album name: " + results['name']
	print "Description: " + results['description']
	print "Number of followers: " + str(results['followers']['total'])
	print "Number of tracks: " + str(numTracks)
	print ""

	tracks = []
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
			# todo: use href to crossreference artist, to get their genres, numFollowers, URI, etc.
			artists.append(a)
		t.artists = artists
		tracks.append(t)

	return tracks

def printTracks(tracks):
	for i in range(len(tracks)):
		# change enconding for names to cp850 when printing, so that "registered" sign does not cause error
		#print(tracks[i].name).encode("cp850") 
		print(tracks[i])
		print ""

def main():
	canadaHotHitsPlaylistURI = "37i9dQZF1DWXT8uSSn6PRy"
	user = "Spotify"
	tracks = getTrackDataFromPlaylist(canadaHotHitsPlaylistURI, user, CLIENT_ID, CLIENT_SECRET)
	printTracks(tracks)

if __name__ == '__main__':
	main()