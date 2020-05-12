# VocabularyScraper
Yet Another Unofficial Application Programming Interface for Vocabulary.com
## Features
- Get the short and the long main definition of a word
- Get a list of synonyms, antonyms, and "type of" words of a word
- This API cannot get Usage Examples.
## Prerequisites
- Python 3
```
pip3 install beautifulsoup4
pip3 install requests
pip3 install json
```
## How to Use
- Install the prerequisites
- Clone this repository
- In your program, add
```
import vocs
```
and use the following functions
### vocs.getPage(word)
- word: a string 
- Return value: a string which is the page content before Javascript codes are run :(
### vocs.getShortDefinition(content)
- content: a string which is the return value of getPage(word)
- Return value: a string which is the short definition
### vocs.getLongDefinition(content)
- Similar to getShortDefinition(content)
### vocs.getSynonym(content)
- content: a string which is the return value of getPage(word)
- Return value: an array of strings that are the synonyms of the given word
- Similar functions: getAntonym(content), getTypeOf(content)
### vocs.getJSON(word)
- word: a string 
- Return value: a string which is a JSON dictionary containing the information of the word with the following format
```
{
    "short": "Adjacent means close to or near something. You may consider the people up and down your street to be neighbors, but your next-door neighbor is the person who lives in the house or apartment adjacent to yours.",
    "long": "Adjacent can refer to two things that touch each other or have the same wall or border. And the adjective is often followed by the preposition to: Her office is adjacent to mine. This word is from Latin adjacere \"to lie near,\" from the prefix ad- \"to\" plus jacere \"to lie, throw.\"",
    "synonym": [
        "conterminous",
        "contiguous",
        "neighboring",
        "connected",
        "next",
        "side by side",
        "close",
        "near",
        "nigh"
    ],
    "antonym": [],
    "typeof": []
}
```
