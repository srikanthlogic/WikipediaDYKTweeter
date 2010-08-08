import mwclient
import re
import sys

def unwikify(Hook):
	rmChar = ['[','{','}',']','.','\'']
	for s in rmChar:
		Hook = Hook.replace(s,'')
	Hook = Hook.replace(', ',',')
        return Hook

def GetDYKHook(PageName):
	site = mwclient.Site('en.wikipedia.org')
	page = site.Pages.get(PageName)
	text = page.edit()
	hook = re.findall('\.\.\..*.\}\}',re.findall('\|entry\=\.\.\..*.\}\}',text).__str__())
	return hook

def main():
	srcPath = sys.argv[1]
	destPath = sys.argv[2]
        sourceFile = open(srcPath,'r')
        outputFile = open(destPath,'a')
        for line in sourceFile:
	    print 'Processing: ' + str(line.splitlines()[0])
            outputFile.write(line.splitlines()[0].__str__() + ',' + unwikify(GetDYKHook(('Talk:'+line).splitlines()[0]).__str__()))
            outputFile.write('\n')
        sourceFile.close()
        outputFile.close()

if __name__ == "__main__":
	main()
