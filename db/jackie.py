import sqlite3
import csv


class Jackie():

	def parseCountry(self, line):
		tokens = self.tokenize(line)
		self.id = tokens[0]
		self.code = tokens[1]
		self.iso = tokens[2]
		self.iso2 = tokens[3]
		self.name_es = tokens[4]
		self.name_en = tokens[5]
		self.isdefault = tokens[6]
		return


	def tokenize(self, line):
		return line.replace("\"","").split(",")

	def connect(self, db_name):
		self.conn = sqlite3.connect(db_name)

	def getTableDesc(self):
		raise("Implement this")

	def createTables(self):
		self.c = self.conn.cursor()
		tables = self.getTableDesc()
		for t in tables:
			self.c.execute(t)

	def commit(self):
		self.conn.commit()

	def openCursor(self):
		self.c = self.conn.cursor()

	def close(self):
		self.c.close()

	def insertTuple(self, country):
		raise("Implement this")

	def parseTuple(self, tokens):
		raise("Nooo")

	def populateDB(self, csv_filename, db_name):
		f = open(csv_filename, "r")
		self.connect(db_name)
		self.createTables()
		firstLine = True
		with open(csv_filename, 'rb') as csvfile:
			filereader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for line in filereader:
				if firstLine:
					firstLine = False
					continue
				utokens = map(lambda x: x.decode('utf-8'), line)
				tuple = self.parseTuple(utokens)
				self.insertTuple(tuple)	
		self.commit()
		self.close()			

import country 
import places 
import sections
import films
import directors

if __name__ == "__main__":
	country.CountryManager().loadData()
	directors.DirectorManager().loadData()
	films.FilmsManager().loadData()
	sections.SectionsManager().loadData()
	places.PlacesManager().loadData()
	

	