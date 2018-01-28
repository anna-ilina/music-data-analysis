import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import unidecode
from classes import *
from authorizationInformation import CLIENT_ID, CLIENT_SECRET
# import json

#todo: change playlist to "Canada Top 50"
#todo: functions read data from csv

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
    trackURIs = []
    artistURIs = []
    #counter = 1
    for item in trackItems:
        t = Track()
        t.name = item['track']['name']
        t.URI = item['track']['uri']
        trackURIs.append(t.URI)
        t.popularity = item['track']['popularity']
        t.durationMs = item['track']['duration_ms']
        t.availableMarkets = item['track']['available_markets']
        t.album = Album(item['track']['album']['name'], item['track']['album']['uri'])
        artists = []
        for artist in item['track']['artists']:
            artists.append(artist['uri'])
        t.artists = artists # list of artist URIs,later replaced with artist objects
        t.numArtists = len(artists)
        tracks.append(t)
    #     if counter % 5 == 0:
    #         print "finished getting track data for %s/%s tracks" % (counter, numTracks)
    #     counter += 1
    # print "finished getting track data for %s/%s tracks" % (counter - 1, numTracks)
    
    audio_features = spotify.audio_features(trackURIs)
    for i in range(len(tracks)):
        # Get audio features for track. Assuming playlist has at most 50 tracks, 
        # since .audio_features takes a list of URIs for at most 50 tracks
        if tracks[i].URI != audio_features[i]['uri']:
            print("ID of track and audio feature don't match")
            exit(1)
        tracks[i].energy = audio_features[i]['energy']
        tracks[i].tempo = audio_features[i]['tempo']
        tracks[i].acousticness = audio_features[i]['acousticness']
        tracks[i].instrumentalness = audio_features[i]['instrumentalness']
        tracks[i].timeSignature = audio_features[i]['time_signature']
        tracks[i].danceability = audio_features[i]['danceability']
        tracks[i].key = audio_features[i]['key']
        tracks[i].mode = audio_features[i]['mode'] 
        tracks[i].valence = audio_features[i]['valence']
        # tracks[i].speechiness = audio_features[i]['speechiness']
        # tracks[i].loudness = audio_features[i]['loudness']
        # tracks[i].liveness = audio_features[i]['liveness']

        #Get artist information for track
        # To speed up function, could get all artists at once and use number of
        # artists per track to parse after
        artistURIsCurrentTrack = tracks[i].artists
        artistsMoreDetails = spotify.artists(artistURIsCurrentTrack)
        artists = []
        for artist in artistsMoreDetails['artists']:
            a = Artist(artist['name'], artist['uri'])
            a.genres = artist['genres']
            a.popularity = artist['popularity']
            a.numFollowers = artist['followers']['total']
            artists.append(a)
        tracks[i].artists = artists

        if (i+1) % 5 == 0:
            print "finished getting track data for %s/%s tracks" % (i+1, numTracks)

    return tracks

def printTracks(tracks):
    for i in range(len(tracks)):
        print(tracks[i])
        print ""

def writeToCSV(filename,tracks):
        with open(filename, 'wb') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['Song', 'First artist', 'Number of artists', 'Number of Followers First Artist','Popularity', 'Genres', 'Album', 'Available Markets', 'Duration in MS', 'Energy', 'Tempo', 'Acousticness', 'Instrumentalness', 'Time Signature', 'Danceability', 'Key', 'Mode', 'Valence'])
                for i in range(len(tracks)):
                        #Get song name
                        song = tracks[i].name
                        #Replace weird characters
                        song = unidecode.unidecode(song)
                        #replace comma because this is csv and it screws things up
                        song = song.replace(',', ';')

                        #do the same for artist
                        artists = tracks[i].artists[0].name
                        artists = unidecode.unidecode(artists)
                        artists = artists.replace(',', ';')

                        #Num artists
                        numArtists = tracks[i].numArtists

                        #Number followers
                        numFollowers = tracks[i].artists[0].numFollowers
                        
                        #Popularity
                        popularity = tracks[i].artists[0].popularity

                        #genres
                        genres = str(tracks[i].artists[0].genres)
                        if genres == '[]':
                                genres = 'NA'
                        genres = genres.replace(',', ';')
                       # genresList = []
                        #for g in genres:
                                #print(g)
#                                g = g.replace(',',';')
#                                genresList = genresList.append(g)

                        #album name
                        album = tracks[i].album.name
                        album = unidecode.unidecode(album)
                        album = album.replace(',',';')

                        #song info
                        availableMarkets = str(tracks[i].availableMarkets)
                        availableMarkets = availableMarkets.replace(',',';')

                        durationMs = tracks[i].durationMs
                        energy = tracks[i].energy
                        tempo = tracks[i].tempo
                        acousticness = tracks[i].acousticness
                        instrumentalness = tracks[i].instrumentalness
                        timeSignature = tracks[i].timeSignature
                        danceability = tracks[i].danceability
                        key = tracks[i].key
                        mode = tracks[i].mode
                        valence = tracks[i].valence
                        
                        #Duration, number artists
                        writer.writerow([song, artists, numArtists, numFollowers, popularity, genres, album, availableMarkets, durationMs, energy, tempo, acousticness, instrumentalness, timeSignature, danceability, key, mode,valence])
                        
                
def main():
    canadaHotHitsPlaylistURI = "37i9dQZF1DWXT8uSSn6PRy"
    user = "Spotify"
    tracks = getTrackDataFromPlaylist(canadaHotHitsPlaylistURI, user, CLIENT_ID, CLIENT_SECRET)

    printTracks(tracks[:3])

    writeToCSV('songs.csv', tracks)


if __name__ == '__main__':
    main()
