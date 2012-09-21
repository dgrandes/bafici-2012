import sqlite3
import jackie
import csv

class FilmTuple():
	def __init__(self, tokens):
		self.id = tokens[0]
		section_csv = tokens[1:3]
		self.sections = []
		for s in section_csv:
			if s != '0' and s != 'NULL':
				self.sections.append(s)

		self.title = tokens[4]
		self.title_es = tokens[5]
		self.title_en = tokens[6]
		self.title_orig = tokens[7]

		csv_countries = tokens[8:11]
		self.countries = []
		for c in csv_countries:
			if c != '0':
				self.countries.append(c)

		self.year =  tokens[12]
		self.synopsis_es = tokens[13]
		self.synopsis_en = tokens[14]
		self.tagline = tokens[16]
		self.duration = tokens[15]
		self.film_format = tokens[17]

		csv_directors = tokens[21:35]
		self.directors = []
		for d in csv_directors:
			if d != '0' and d !='NULL':
				self.directors.append(d)
		self.cast = tokens[37]
		self.prodteam = tokens[38]
		self.published = tokens[39]
		self.youtube = tokens[55]
		self.url_ticket = tokens[56]
		self.created_ts = tokens[63]
		self.updated_ts = tokens[64]


class FilmsManager(jackie.Jackie):

	def parseTuple(self, tokens):
		return FilmTuple(tokens)

	def getTableDesc(self):
		film_table = '''CREATE TABLE films(id int, title text, title_es text, title_en text, title_orig text, year int,  synopsis_es text, synopsis_en text, tagline text, duration int, cast text, prodteam text, published boolean, youtube text, url_ticket text, created_ts date, updated_ts date)'''

		film_countries = '''CREATE TABLE film_countries(id_film int, id_country int)'''

		film_directors = '''CREATE TABLE film_directors(id_film int, id_director int)'''

		film_sections = '''CREATE TABLE film_sections(id_film int, id_section int)'''

		return [film_table, film_countries, film_directors, film_sections]

	def insertTuple(self, tuple):
		insert = '''INSERT into films(id, title, title_es, title_en, title_orig, year, synopsis_en, synopsis_es, tagline, duration, cast, prodteam, published, youtube, url_ticket, created_ts, updated_ts) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
		self.c.execute(insert,(tuple.id, tuple.title, tuple.title_es, tuple.title_en, tuple.title_orig, tuple.year, tuple.synopsis_es, tuple.synopsis_en, tuple.tagline, tuple.duration, tuple.cast, tuple.prodteam, tuple.published, tuple.youtube, tuple.url_ticket, tuple.created_ts, tuple.updated_ts))
	
		insert_films_countries = '''INSERT into film_countries(id_film, id_country) values(?,?)'''
		for c in tuple.countries:
			self.c.execute(insert_films_countries,(tuple.id, c))

		insert_films_directors = '''INSERT into film_directors(id_film, id_director) values(?,?)'''
		for d in tuple.directors:
			self.c.execute(insert_films_directors, (tuple.id, d))

		insert_film_sections = '''INSERT into film_sections(id_film, id_section) values(?,?)'''
		for s in tuple.sections:
			self.c.execute(insert_film_sections, (tuple.id, s))

	def loadData(self):
		csv = "bafici-2012/20120416-bafici12-produccion-01-opendata-2012_films.csv"
		db_name = "bafici.db"
		self.populateDB(csv, db_name)

if __name__ == "__main__":
	c = FilmsManager()
	c.loadData()
	