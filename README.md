# SQLCheck-Plus

exp folder is for storing SQLite files

milestone-assignments folder contains the milestone assignments (initial proposal, revised proposal, progress report, final report, demo ppt slides)

the py files are the source code for SQLCheck+

sqlcheck.exe is from https://github.com/jarulraj/sqlcheck

manual labeling + rq2 result.pdf contains the manually labeled dataset and RQ2's result tables


------------------------ datasets links

18,393 Pitchfork Reviews
https://www.kaggle.com/datasets/nolanbconaway/pitchfork-data

Twitter US Airline Sentiment
https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment

SF Salaries
https://www.kaggle.com/datasets/kaggle/sf-salaries

US Consumer Finance Complaints
https://www.kaggle.com/datasets/kaggle/us-consumer-finance-complaints

US Baby Names
https://www.kaggle.com/datasets/kaggle/us-baby-names

Mental Health in the Tech Industry
https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry

NIPS Papers
https://www.kaggle.com/datasets/benhamner/nips-papers

Hillary Clinton's Emails
https://www.kaggle.com/datasets/kaggle/hillary-clinton-emails

The History of Baseball
https://www.kaggle.com/datasets/seanlahman/the-history-of-baseball

------------------------ Reproduce Work:
download a SQLite file and put in exp folder,

in terminal enter: python3 main.py ./exp/<filename>.sqlite <optional threshold>

Final Paper code: (all using default threshold 0.15 while PitchforkReviews uses 0.001)


python3 main.py ./exp/Hillary_Clinton_s_Emails.sqlite

python3 main.py ./exp/mental_health.sqlite

python3 main.py ./exp/NIPS_Papers.sqlite

python3 main.py ./exp/Pitchfork-Reviews.sqlite 0.001

python3 main.py ./exp/SF_Salaries.sqlite

python3 main.py ./exp/Twitter-US-Airline-Sentiment.sqlite

python3 main.py ./exp/US_Baby_Names.sqlite

python3 main.py ./exp/US_Consumer_Finance_Complaints.sqlite

python3 main.py ./exp/The-History-of-Baseball.sqlite

