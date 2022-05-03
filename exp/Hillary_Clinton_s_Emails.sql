CREATE TABLE Emails (
    Id INTEGER PRIMARY KEY,
    DocNumber TEXT,
    MetadataSubject TEXT,
    MetadataTo TEXT,
    MetadataFrom TEXT,
    SenderPersonId INTEGER,
    MetadataDateSent TEXT,
    MetadataDateReleased TEXT,
    MetadataPdfLink TEXT,
    MetadataCaseNumber TEXT,
    MetadataDocumentClass TEXT,
    ExtractedSubject TEXT,
    ExtractedTo TEXT,
    ExtractedFrom TEXT,
    ExtractedCc TEXT,
    ExtractedDateSent TEXT,
    ExtractedCaseNumber TEXT,
    ExtractedDocNumber TEXT,
    ExtractedDateReleased TEXT,
    ExtractedReleaseInPartOrFull TEXT,
    ExtractedBodyText TEXT,
    RawText TEXT);
CREATE TABLE Persons (
    Id INTEGER PRIMARY KEY,
    Name TEXT);
CREATE TABLE Aliases (
    Id INTEGER PRIMARY KEY,
    Alias TEXT,
    PersonId INTEGER);
CREATE TABLE EmailReceivers (
    Id INTEGER PRIMARY KEY,
    EmailId INTEGER,
    PersonId INTEGER);