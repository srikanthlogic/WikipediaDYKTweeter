WikipediaDYKTweeter

DYKHookScrapper.py:- This script aims to populate DYK hooks by scrapping them from the talk page of DYK articles outputs to a csv file.

WikiDYKTweeter.py:-  This script reads from Google docs spreadsheet where Tweet queue is maintained, creates short  URLs using bit.ly and posts the tweet to twitter

Prerequisites:
1. Python 2.6 with mwclient ( http://mwclient.sourceforge.net ) 
2. source.txt containing list of DYK articles which can be obtained by CatScan like tools. ( http://toolserver.org/~magnus/catscan_rewrite.php )
3. Python modules of tweepy,bitlyapi,GDataSpreadsheet API, ElementTree

Usage:
1. $python DYKHookScrapper.py /path/to/sourceList.txt /path/to/OutputFile.txt
2. Upload the Outputfile into Google Docs maintaining the same format as in http://bit.ly/WikiDYKTweeterFormat
3. Modify config.ini with required details
4. $python WikiDYKTweeter.py

TODO:
1. Make it more configurable.
	a. Spreadsheet ID, Worksheet ID must be written to config file by seperate script
	b. Column definitions should be customizable and be configurable
2. Enable logging
3. Make the DYKHookScrapper more comprehensive covering all present patterns
