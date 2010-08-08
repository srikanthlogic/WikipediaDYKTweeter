WikipediaDYKTweeter

This script aims to populate DYK hooks by scrapping them from the talk page of DYK articles outputs to a csv file.

Prerequisites:
1. Python 2.6 with mwclient ( http://mwclient.sourceforge.net ) 
2. source.txt containing list of DYK articles which can be obtained by CatScan like tools. ( http://toolserver.org/~magnus/catscan_rewrite.php )

Usage:
$python DYKHookScrapper.py /path/to/sourceList.txt /path/to/OutputFile.txt

TODO:
Script to read the GDocs TweetQueue spreadsheet, form bit.ly links, compose the tweet and post it.
