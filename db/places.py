import sqlite3
import jackie

class PlacesTuple():
	def __init__(self, tokens):
		self.id = tokens[0]
		self.title = tokens[1]
		self.abbrev = tokens[2]
		self.address = tokens[3]
		self.city = tokens[4]
		self.phone = tokens[5]
		self.bus = tokens[6]
		self.subway = tokens[7]
		self.train = tokens[8]
		self.rooms = tokens[9]
		self.published = tokens[12]
		self.filepic = tokens[13]
		

class PlacesManager(jackie.Jackie):

	def parseTuple(self, tokens):
		return PlacesTuple(tokens)

	def getTableDesc(self):
		return ['''CREATE TABLE places (id int, title text, abbrev text, address text, city text, phone text, bus text, subway text, train text, rooms text, published boolean, filepic text)''']

	def insertTuple(self, tuple):
		insert = '''INSERT into places(id, title, abbrev, address, city, phone, bus, subway, train, rooms, published, filepic) values(?,?,?,?,?,?,?,?,?,?,?,?)'''
		self.c.execute(insert,(tuple.id, tuple.title, tuple.abbrev, tuple.address, tuple.city, tuple.phone, tuple.bus, tuple.subway, tuple.train, tuple.rooms, tuple.published, tuple.filepic))
	
	def loadData(self):
		csv = "bafici-2012/20120416-bafici12-produccion-01-opendata-2012_places.csv"
		db_name = "bafici.db"
		self.populateDB(csv, db_name)

if __name__ == "__main__":
	c = PlacesManager()
	c.loadData()
	