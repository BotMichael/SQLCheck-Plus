# SQLCheck-Plus

Demo: 
F:
cd F:\cu-mscs\course-notes\6156-SE\project\SQLCheck-Plus
python3 create_synthetic_db.py
python3 main.py ./exp/synthetic.sqlite




python3 main.py ./exp/The-History-of-Baseball.sqlite


sqlcheck.exe -f .\schemas\synthetic.sql  > .\SQLCheck-results\output_synthetic.txt

----------------------------------------

sqlcheck.exe -f .\schemas\The-History-of-Baseball.sql  > .\SQLCheck-results\output_The-History-of-Baseball.txt

sqlcheck.exe -f .\schemas\Pitchfork-Reviews.sql  > .\SQLCheck-results\output_Pitchfork-Reviews.txt


sqlcheck.exe -f .\schemas\Pitchfork-Reviews.sql -v > .\SQLCheck-results\output_Pitchfork-Reviews-verbose.txt


sqlcheck.exe -f .\schemas\FPA_FOD_20170508.sql  > .\SQLCheck-results\output_FPA_FOD_20170508.txt

sqlcheck.exe -f .\schemas\FPA_FOD_20170508-novirtual.sql  > .\SQLCheck-results\output_FPA_FOD_20170508-novirtual.txt

===> SQLCheck cannot process unvirtual statement - so need to manually remove those statements

sqlcheck.exe -f .\schemas\FPA_FOD_20170508-onlyCreate.sql > .\SQLCheck-results\output_FPA_FOD_20170508-onlyCreate.txt


sqlcheck.exe -f .\schemas\basketball.sql  > .\SQLCheck-results\output_basketball.txt
# need to remove quotation marks to run SQLCheck properly
sqlcheck.exe -f .\schemas\basketball2.sql  > .\SQLCheck-results\output_basketball2.txt

sqlcheck.exe -f .\schemas\Twitter-US-Airline-Sentiment.sql  > .\SQLCheck-results\output_Twitter-US-Airline-Sentiment.txt



Datasets:

<!-- 2016 US Election
https://www.kaggle.com/datasets/benhamner/2016-us-election -->

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

------------------------


The History of Baseball
https://www.kaggle.com/datasets/seanlahman/the-history-of-baseball

------------------------ deliverable code
<!-- python3 main.py ./exp/2016_US_Election.sqlite -->




python3 main.py ./exp/Hillary_Clinton_s_Emails.sqlite
python3 main.py ./exp/mental_health.sqlite
python3 main.py ./exp/NIPS_Papers.sqlite
python3 main.py ./exp/Pitchfork-Reviews.sqlite 0.001
python3 main.py ./exp/SF_Salaries.sqlite

python3 main.py ./exp/Twitter-US-Airline-Sentiment.sqlite
python3 main.py ./exp/US_Baby_Names.sqlite
python3 main.py ./exp/US_Consumer_Finance_Complaints.sqlite
python3 main.py ./exp/The-History-of-Baseball.sqlite

--------------

F:
cd F:\cu-mscs\course-notes\6156-SE\project\SQLCheck-Plus
sqlcheck.exe -f ./exp/synthetic.sql > ./exp/output_synthetic.txt



---- (put in paper)
worth noticing that when violate "Generic Primary Key" AP, it's also likely that the schema design violates "Foreign Key Does Not Exist" AP. For instance, NIPS_papers dataset id问题