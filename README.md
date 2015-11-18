# JoTA
Job Trend Analyzer. 
Currently, the website was hosted on localhost. THe codedump can be installed on any external server and the website could be used.
The setup requires Amazon EMR, mapper and reducer programs and Usage of S3 bucket.
The respective names of S3 bucket, access key and the amazon EMR ssh connection needs to be modified in the files.
THe website requires the usage of database as well (we need to isntall MySQL DB).

On page load 
•	scrapy starts scraping, puts data into database and retrieves it from the database in the desired format to generate the input file for the mapper. 
•	This page gets uploaded to the S3 bucket and the streaming step begins (Mapper + Reducer). 
•	Reducer output gets downloaded in the current directory as output_folder and merge.py merges them to create locMergeFile.tsv

When Location Based Search is clicked:
•	D3 page is called with field = Location and locMergeFile.tsv.
•	If you click on the graph you get the corresponding listing in tabular format and simultaneously in the background the input file for mapper_skill is uploaded to S3.

When skill based Search is clicked:
•	D3 page is called with field = Location and skillMergeFile.tsv.
•	If you click on the graph you get the corresponding listing in tabular format, all the jobs under that skill is displayed in html pages, which in-turn contains links to the actual company-career websites.

Finally, the best-match feature will accept from the user, the top three skills and the location and would execute the algorithm in the background and outputs the JoTA Score and the best matches of the jobs for his profile. And, thus this simplifies his jobsearch process.

