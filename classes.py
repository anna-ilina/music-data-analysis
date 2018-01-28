# Class containing information on tracks

# todo: using name.encode("ascii", "replace") when printing causes some characters (ie the 'o' in "MO") to be replace with '?'
#	is there a better encoding?

#todo: add 'danceablity' or 'tempo' attributes to Track class?

class Artist():
	def __init__(self):
		self.name = ""
		self.URI = ""
		self.numFollowers = None
		self.popularity = None
		self.genres = []

	def __init__(self, name, URI = ""):
		self.name = name
		self.URI = URI
		self.numFollowers = None
		self.popularity = None
		self.genres = []

	def __repr__(self):
		return "<Artist name:%s URI:%s numFollowers:%s popularity:%s genres: %s" \
		% (self.name.encode("ascii", "replace"), 
			self.URI, self.numFollowers, self.popularity, str(self.genres))


class Album():
	def __init__(self):
		self.name = ""
		self.URI = ""
		#self.genres = []
		#self.isSingle = None

	def __init__(self, name, URI):
		self.name = name
		self.URI = URI
		#self.genres = []
		#self.isSingle = None

	def __repr__(self):
		return "<Album name:%s URI:%s>" % (self.name.encode("ascii", "replace"), self.URI)


class Track():  
	def __init__(self):
		self.name = ""
		self.URI = ""
		self.artists = []			# list of Artist objects
		self.numArtists = None
		self.album = None			# Album object
		self.popularity = None		# popularity rating out (0-100), based on Spotify algorithm taking
									#    into account number of listens and how recent these listens were
		self.durationMs = None		# track duration in milliseconds
		self.availableMarkets = [] 	# list of countries where track is available
		self.energy = None
		self.tempo = None
		self.acousticness = None
		self.instrumentalness = None
		self.timeSignature = None
		self.danceablity = None
		self.key = None
		self.mode = None			# Major is represented by 1 and minor is 0.
		self.valence = None			# A measure from 0.0 to 1.0 describing the musical positiveness conveyed 
									# 	by a track. Tracks with high valence sound more positive (e.g. happy, 
									# 	cheerful, euphoric), while tracks with low valence sound more negative 
									# 	(e.g. sad, depressed, angry).

	def __repr__(self):
		return "<Track name:%s URI:%s artists:%s album:%s popularity:%s durationMs:%s availableMarkets:%s " \
		"energy:%s tempo: %s acousticness:%s instrumentalness:%s timeSignature:%s danceablity:%s key:%s " \
		"mode:%s valence:%s>"% (self.name.encode("ascii", "replace"), self.URI, self.artists, self.album,
			self.popularity, self.durationMs, self.availableMarkets, self.energy, self.tempo, self.acousticness,
			self.instrumentalness, self.timeSignature, self.danceablity, self.key, self.mode, self.valence)

