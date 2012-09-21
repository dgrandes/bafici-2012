import sqlite3
import jackie
import csv

class DirectorTuple():
	def __init__(self, tokens):
		self.id = tokens[0]
		self.name = tokens[1]
		self.bio_es = tokens[2]
		self.bio_en = tokens[3]
		self.published = tokens[4]
		self.filepic = tokens[5]
		self.created_ts = tokens[6]
		self.updated_ts = tokens[7]

class DirectorManager(jackie.Jackie):

	def parseTuple(self, tokens):
		return DirectorTuple(tokens)

	def getTableDesc(self):
		return ['''CREATE TABLE directors (id int, name text, bio_es text, bio_en text, published int, filepic text, created_ts date, updated_ts date)''']

	def insertTuple(self, tuple):
		insert = '''INSERT into directors(id, name, bio_es, bio_en, published, filepic, created_ts, updated_ts) values(?,?,?,?,?,?,?,?)'''
		self.c.execute(insert,(tuple.id, tuple.name, tuple.bio_es, tuple.bio_en, tuple.published, tuple.filepic, tuple.created_ts, tuple.updated_ts))

	def loadData(self):
		csv = "bafici-2012/20120416-bafici12-produccion-01-opendata-2012_directors.csv"
		db_name = "bafici.db"
		self.populateDB(csv, db_name)	

if __name__ == "__main__":
	c = DirectorManager()
	c.loadData()
	