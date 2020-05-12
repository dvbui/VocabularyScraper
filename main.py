from bs4 import BeautifulSoup
import requests
# Input: a string
# Output: a webpage in string
def getPage(word):
	link = "https://www.vocabulary.com/dictionary/"+word
	page = requests.get(link)
	return page.content
	
# Input: 
#	content - webpage in string
# Output:
#	short definition in string if it exists
#	otherwise, empty string
def getShortDefinition(content):
	soup = BeautifulSoup(content)
	shortDefDiv = soup.findAll("p", {"class": "short"})
	if (len(shortDefDiv)==0):
		return ""
	assert len(shortDefDiv)==1
	shortDefDiv = shortDefDiv[0]
	return shortDefDiv.get_text()

