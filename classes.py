# Class containing information on tracks

# todo: using name.encode("ascii", "replace") when printing causes some characters (ie the 'o' in "MO") to be replace with '?'
#	is there a better encoding?

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
		return "<Artist name:%s URI:%s numFollowers:%s> popularity:%s genres: %s" % (self.name.encode("ascii", "replace"), 
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
		#self.albumGenres = []		# todo: spotipy does not seem to return genre. Perhaps it is returning
									#   the simplified Album object?
		#self.artistGenres = []
		#self.tempo = None

	def __repr__(self):
		return "<Track name:%s URI:%s artists:%s album:%s popularity:%s durationMs:%s availableMarkets:%s>" \
		% (self.name.encode("ascii", "replace"), self.URI, self.artists, self.album, self.popularity, self.durationMs, self.availableMarkets)

