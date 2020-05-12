import main
import json

def testGetDefinition(testcase = 'testWordList.txt'):
	f = open(testcase,'r')
	g = open("log.txt","w")

	for line in f:
		word = line[:-1]
		page = main.getPage(word)
		shortDef = main.getShortDefinition(page)
		longDef = main.getLongDefinition(page)
		g.write(word+" - "+shortDef+" - "+longDef+"\n")
		
	g.close()
	f.close()

def testToJSON(testcase = 'testWordList.txt'):
	f = open(testcase,'r')
	g = open("initial.json","w")

	json_dict = {}
	for line in f:
		word = line[:-1]
		json_dict[word] = {}
		page = main.getPage(word)
		shortDef = main.getShortDefinition(page)
		longDef = main.getLongDefinition(page)
		synonym = main.getSynonym(page)
		typeOf = main.getTypeOf(page)
		antonym = main.getAntonym(page)
		
		json_dict[word]["short"] = shortDef
		json_dict[word]["long"] = longDef
		json_dict[word]["synonym"] = synonym
		json_dict[word]["antonym"] = antonym
		json_dict[word]["typeof"] = typeOf
	
	g.write(json.dumps(json_dict, indent = 4))
	
	f.close()
	g.close()
