# SQLCheck-Plus

------------------------ project synopsis

Data storage has become one of the most common features for web applications. While software developers design database schemas and program query statements to retrieve data, they may inevitably introduce database-access performance anti-patterns (AP) which not only violate basic design principles and best practices but also bring down the overall system performance. For instance, APs may cause redundant storage and increase applications’ response time. Besides, identifying APs and implementing fixes require much developers’ effort and are time-consuming. To understand and handle database-access performance issues, researchers have examined popular real-world web applications to extract and categorize common performance APs and evaluated the APs’ impacts on applications’ performance. Some studies propose SQL level APs detection and fix suggestion approaches. With using object-relational-mapping (ORM) frameworks, which are written in object-oriented programming languages to provide data model abstraction for developers to reduce the burden of CRUD operations, to build web applications become popular, some researchers have examined ORM-based applications and also found ORM level APs that affect performance. Some studies focus on mobile applications and analyze how APs affect energy consumption and may introduce security vulnerabilities. 

For my project, I developed SQLCheck+ to detect logical design and physical design related SQL-based APs. My motivation stemmed from the fact that the open-sourced SQLCheck [1] tool has a relatively high false-positive rate and is incompetent in detecting APs in many scenarios. After examining the false-positive cases from my midterm paper experiments, I found it solvable by implementing additional rule-based approaches and analyzing raw data’s contents. Additionally, although data analysis is proposed in SQLCheck, the open-sourced SQLCheck tool does not support inputting raw data. Furthermore, while SQLCheck only uses data analysis to help detect APs, SQLCheck+ performs data analysis both to identify potential APs and to verify SQLCheck’s reported APs to reduce the false-positive rate. After implementing SQLCheck+ and comparing it against SQLCheck over 9 popular Kaggle datasets, SQLCheck+ has shown a significantly high precision (True Positive/(True Positive + False Positive)).


------------------------ repo overview

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

