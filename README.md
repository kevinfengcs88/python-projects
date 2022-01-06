# python-projects
Python is an incredibly powerful language, and with its easy readability and useful packages, it's no wonder that it's one of the most popular coding languages. I found
Python to be a great language to implement my ideas for various problems.

## [MorseCode](https://github.com/kevinfengcs88/python-projects/blob/main/MorseCode.py), [Morse](https://github.com/kevinfengcs88/python-projects/blob/main/Morse.py), and [AdvancedMorseCode](https://github.com/kevinfengcs88/python-projects/blob/main/AdvancedMorseCode.py) (Morse Code Translator)
**_The Morse Code Translator encrypts English letters into Morse code sequences and decrypts Morse code into English letters._**

These projects were all created when I first learned Morse code, mainly utilizing the mnemonics that Michael "Vsauce" Stevens teaches in this [video](https://www.youtube.com/watch?v=HY_OIwideLg).
I created my own translator for Morse code, which can both translate Morse code to English letters and English letters to Morse code. It interprets '.' characters as
short signals or "dits," and interprets '-' characters as long signals or "dahs." Both MorseCode and Morse ask the user whether they would like to encrypt English letters 
into Morse code or decrypt Morse code into English letters, with Morse more stably exiting from the command prompt window that an .exe file opens. AdvancedMorseCode does not
require the user to specify "encrypt" or "decrypt," and simply translates according to the input appropriately.

## [kahoot.py](https://github.com/kevinfengcs88/python-projects/blob/main/kahoot.py) (Kahoot Bot)
**_The Kahoot Bot floods a Kahoot! game with however many bots are specified._**

You probably already know about the popular quiz-based learning game, [Kahoot!](https://kahoot.it/), which is used in schools to assess students' understanding of topics
(or just to play a fun game during class). The premise is simple: a room is set up to run a specific quiz, which players can join by entering that room's specific game PIN.
Once everyone joins, the host can begin the game, which consists of a series of multiple choice questions. Players a rewarded a set number of points for getting a question correct, with a direct relationship between the time it took to answer a question and the number of points deducted from that set number as a time penalty. 

As innocent as it is, Kahoot! has been the target of a number of "troll" projects, namely Kahoot! botting, in which dummy players flood a 
room upon being given a valid game PIN. It can be
pretty funny to see hundreds of players flood the game in a relatively harmless prank, and it used to be pretty easy to do: just search up something like "kahoot bot,"
click on a link, and enter the game PIN. Though there were hundreds of different botting programs available for free, one decided to become a paid service, and as you
would expect, the rest followed suit. Without a free option to flood Kahoot! games, I decided to create one myself.

This Python script utilizes the same HTML parsing API that my [Old School RuneScape price scraper](https://github.com/kevinfengcs88/osrs-projects/blob/main/sheets.py) uses:
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). It takes in the number of bots you would like to flood the game, the game PIN, and generates
unique, gibberish names for the bots and enters them into the game.
