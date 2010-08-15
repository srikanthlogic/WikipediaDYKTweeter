import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
from xml.etree import ElementTree
import string
import time
from configobj import ConfigObj
import tweepy
import bitlyapi

class WikipediaDYKTweeter:

	gd_client = gdata.spreadsheet.service.SpreadsheetsService()
	spreadSheetKey = ''
	workSheetId = ''
	config = ConfigObj('WPDYK.cfg')

	def PostTweet(self,tweetText):
		auth = tweepy.OAuthHandler(self.config['TWITTER']['CONSUMER_KEY'], self.config['TWITTER']['CONSUMER_SECRET'])
		auth.set_access_token(self.config['TWITTER']['ACCESS_KEY'], self.config['TWITTER']['ACCESS_SECRET'])
		api = tweepy.API(auth)
		status = api.update_status(tweetText)
		tweetURL = 'http://twitter.com/DYKIndia/status/' + str(status.id)
		return tweetURL

	def GetCurrentHookRowNumber(self,queryFeed):
		CurrentRow = 0
		today = time.strftime("%d-%m-%Y")
		for e in queryFeed.entry:
			c = time.strptime(e.content.text,"%m/%d/%Y")
			if time.strftime("%d-%m-%Y",c) == today :
				CurrentRow = e.title.text.rsplit('B')[1]
	 	return CurrentRow

	def GetQueryFeedForGrid(self,rowNumMin,rowNumMax,colNumMin,colNumMax):
		print 'Entering GetQueryFeedForGrid' 
		query = gdata.spreadsheet.service.CellQuery()
		query['min-col'] = colNumMin
		query['max-col'] = colNumMax
		query['min-row'] = rowNumMin
		query['max-row'] = rowNumMax
		print 'before queryFeed'
		queryFeed = self.gd_client.GetCellsFeed(self.spreadSheetKey,self.workSheetId,query=query)
		return queryFeed

	def UpdateCell(self,row, col, CellText):
	  	entry = self.gd_client.UpdateCell(row=row, col=col, inputValue=CellText, 
	      		key=self.spreadSheetKey, wksht_id=self.workSheetId)
	  	if isinstance(entry, gdata.spreadsheet.SpreadsheetsCell):
	    		return 0

	def LoadWorkSheet(self): 
		print 'Entering LoadWorkSheet'
		self.gd_client.email = self.config['GDOCS']['GMAIL_ID']
		self.gd_client.password = self.config['GDOCS']['PASSWORD']
		self.gd_client.source = self.config['GDOCS']['SOURCE']
		self.gd_client.ProgrammaticLogin()
		print 'logged in'
		spreadSheetsfeed = self.gd_client.GetSpreadsheetsFeed()  
		self.spreadSheetKey = spreadSheetsfeed.entry[0].id.text.split('/')[-1] 
		#entry[0] will give the only spreadsheet in the account.
		#last part of the feed URL contains the key

		workSheetFeed = self.gd_client.GetWorksheetsFeed(self.spreadSheetKey)
		self.workSheetId = workSheetFeed.entry[2].id.text.split('/')[-1]
		return 0

	def MainMethod(self):
		self.LoadWorkSheet()
		queryFeed = self.GetQueryFeedForGrid('2','100','2','2')
		CurrentRow = self.GetCurrentHookRowNumber(queryFeed)
		if CurrentRow == 0:
			print "Error Finding Today's Hook"
			return 1
			#exit

		queryFeed = self.GetQueryFeedForGrid(CurrentRow,CurrentRow,'2','6')
	
		hookText = queryFeed.entry[2].content.text
		print hookText , 'is the hook text'
		hookLongURL = queryFeed.entry[4].content.text
		hookShortURL = self.BitlyShorten(hookLongURL)

		tweetText = hookText + ' ' + hookShortURL
		print tweetText
		tweetURL = self.PostTweet(tweetText)
		print 'Updating to docs'
		self.UpdateCell(CurrentRow,'7',hookShortURL)
		self.UpdateCell(CurrentRow,'8',tweetText)
		self.UpdateCell(CurrentRow,'9',tweetURL)
		print 'Script Complete'
		return 0

	def BitlyShorten(self,ActualURL):
	    	b = bitlyapi.BitLy(self.config['BITLY']['API_USER'],self.config['BITLY']['API_KEY'])
	    	shortURL =  b.shorten(longUrl=ActualURL,domain='j.mp')
	    	return str(shortURL['url'])	

if __name__ == "__main__":
	wpDYKTweeter = WikipediaDYKTweeter()
	wpDYKTweeter.MainMethod()

