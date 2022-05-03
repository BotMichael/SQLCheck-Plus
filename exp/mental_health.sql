CREATE TABLE Answer (
	AnswerText VARCHAR(10000) NULL,
	SurveyID INTEGER NULL,
	UserID INTEGER NULL,
	QuestionID INTEGER NULL
);
CREATE TABLE Question (
	questiontext VARCHAR(1000) NULL,
	questionid INTEGER NULL
);
CREATE TABLE Survey (
	SurveyID INTEGER NOT NULL,
	Description VARCHAR(255) NULL,
	PRIMARY KEY (SurveyID)
);