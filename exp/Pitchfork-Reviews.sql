CREATE TABLE reviews (
	reviewid INTEGER,
	title TEXT,
	artist TEXT,
	url TEXT,
	score REAL,
	best_new_music INTEGER,
	author TEXT,
	author_type TEXT,
	pub_date TEXT,
	pub_weekday INTEGER,
	pub_day INTEGER,
	pub_month INTEGER,
	pub_year INTEGER);
CREATE TABLE artists (
	reviewid INTEGER, artist TEXT);
CREATE TABLE genres (
	reviewid INTEGER, genre TEXT);
CREATE TABLE labels (
	reviewid INTEGER, label TEXT);
CREATE TABLE years (
	reviewid INTEGER, year INTEGER);
CREATE TABLE content (
	reviewid INTEGER, content TEXT);