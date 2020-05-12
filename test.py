import main

def testGetShortDefinition(testcase = 'testWordList.txt'):
	f = open(testcase,'r')
	g = open("log.txt","w")

	for line in f:
		word = line[:-1]
		page = main.getPage(word)
		shortDef = main.getShortDefinition(page)
		g.write(word+" - "+shortDef+"\n")
		
	g.close()
	f.close()
