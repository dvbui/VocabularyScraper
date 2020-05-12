
import requests
# Input: a string
# Output: a webpage in string
def getPage(word):
	link = "https://www.vocabulary.com/dictionary/"+word
	page = requests.get(link)
	return page.content
	
