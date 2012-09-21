import sqlite3
import jackie

class SectionsTuple():
	def __init__(self, tokens):
		self.id = tokens[0]
		self.sections_group = tokens[1]
		self.name_es = tokens[2]
		self.name_en = tokens[3]
		self.desc_es = tokens[6]
		self.desc_en = tokens[7]
		self.published = tokens[8]
		

class SectionsManager(jackie.Jackie):

	def parseTuple(self, tokens):
		return SectionsTuple(tokens)

	def getTableDesc(self):
		return ['''CREATE TABLE sections (id int, sections_group int, name_es text, name_en text, desc_es text, desc_en text, published boolean)''']

	def insertTuple(self, tuple):
		insert = '''INSERT into sections(id, sections_group, name_es, name_en, desc_es, desc_en, published) values(?,?,?,?,?,?,?)'''
		self.c.execute(insert,(tuple.id, tuple.sections_group, tuple.name_es, tuple.name_en, tuple.desc_es, tuple.desc_en, tuple.published))
	
	def loadData(self):
		csv = "bafici-2012/20120416-bafici12-produccion-01-opendata-2012_sections.csv"
		db_name = "bafici.db"
		self.populateDB(csv, db_name)

if __name__ == "__main__":
	c = SectionsManager()
	c.loadData()
	