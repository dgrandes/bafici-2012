import sqlite3
import jackie

class CountryTuple():
	def __init__(self, tokens):
		self.id = tokens[0]
		self.code = tokens[1]
		self.iso = tokens[2]
		self.iso2 = tokens[3]
		self.name_es = tokens[4]
		self.name_en = tokens[5]
		self.isdefault = tokens[6]

class CountryManager(jackie.Jackie):

	def parseTuple(self, tokens):
		return CountryTuple(tokens)

	def getTableDesc(self):
		return ['''CREATE TABLE countries (id int, country_code int, iso_code text, iso_code_2 text, name_es text, name_en text, isdefault boolean)''']

	def insertTuple(self, tuple):
		insert = '''INSERT into countries(id, country_code, iso_code, iso_code_2, name_es, name_en, isdefault) values(?,?,?,?,?,?,?)'''
		self.c.execute(insert,(tuple.id, tuple.code, tuple.iso, tuple.iso2, tuple.name_es, tuple.name_en, tuple.isdefault))
	
	def loadData(self):
		csv = "bafici-2012/20120416-bafici12-produccion-01-opendata-2012_countries.csv"
		db_name = "bafici.db"
		self.populateDB(csv, db_name)	

if __name__ == "__main__":
	c = CountryManager()
	c.loadData()