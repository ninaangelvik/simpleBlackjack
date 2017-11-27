# simpleBlackjack
A simple python implementation of the game Blackjack

GAME  
To run the game:  
./blackjack.py  

Optional command line arguments:  
-file  

Usage:  
-file=path/to/file.txt

The -file argument takes in a reference to a file containing a deck of cards.  
The file must contain a list of the follwing format:  

CA, D4, H7, SJ, ... ,S5, S9  

If no file is provided, the game will initialize a new shuffled deck of 52 unique cards.  

TESTS  
To run tests:  
./test.ut.py -b  
