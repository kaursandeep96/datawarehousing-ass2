# datawarehousing-ass2
# TWITTER TWEET EXTRACTION:
## Steps performed to extract the data from Twitter:
Created the app on Twitter and saved its security credentials.
Checking for preinstalled Python3 using command:
```sh
python3 -V
```
Installed pip package manager using command:
```sh
sudo apt-get install -y python3-pip
```
Installed tweepy using:
```sh
pip3 install tweepy
```
Python program was written in order to create sample app, OAuth connection, retrieve the data from the profile for example retrieving the trends on Twitter.
The extracted data or tweets were saved in to csv file.
The csv file has four fields: Id, User, Created_at, Text.

## SENTIMENT ANALYSIS:
The sentiment analysis was performed with the help of python library. The library used was Text Blob. The library was used in the python program. First, program reads the extracted tweets from the csv created previously. The fetched tweets from csv file were cleaned by using Regular Expression(re) library. Now the cleaned data was analysed for sentiments using text blob library. Naïve Bayes classifiers is used by TextBlob to achieve the positive and negative reviews on the data. Its sentiment classifier calculates the polarity between the range of -1.0 and 1.0 where -1.0 is negative, 0.0 is neutral and 1.0 is positive. The screenshot of the program is provided for all the above explained steps. Then again retrieved data was converted in to csv file using the same program. The file included the three fields: Twitter_tweet, sentiment, sentiment_score. The algorithm calculated the sentiments on basis of texts and provided the accurate results.

## LOADING DATA INTO ELASTIC SEARCH DATABASE:
The output captured in previous step was then loaded into Elastic Search database using Elastic Search API. The data loaded must contain three attributes: Twitter tweet, Sentiment, Sentiment Score. To complete this step, we used python program which imported the helper and elastic search libraries from Elastic Search library. This library uses the elastic search method for bulk insertion of data. The screenshot of program for loading the data in to Elastic Search is provided below:

## ETL as a BATCH PROCESS:
The shell scripting was created using Linux Shell commands which included the script for performing all the three programs used for extraction of tweets, performing sentiment analysis and finally loading the data into Elastic Search database.
