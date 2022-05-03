CREATE TABLE papers (
    id INTEGER PRIMARY KEY,
    year INTEGER,
    title TEXT,
    event_type TEXT,
    pdf_name TEXT,
    abstract TEXT,
    paper_text TEXT);
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT);
CREATE TABLE paper_authors (
    id INTEGER PRIMARY KEY,
    paper_id INTEGER,
    author_id INTEGER);