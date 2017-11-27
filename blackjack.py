#! /usr/bin/env python
import argparse
import random
import sys

class Card:
  def __init__(self, suite, value):
    self.suite = suite
    self.value = value
    self.numValue = self.getNumValue(self.value)

  def getNumValue(self, value):
    tens = ['J', 'Q', 'K'] 
    
    if value in tens:
      return 10
    elif value == 'A':
      return 11 
    else:
      return int(value)

class Player:
  def __init__(self, name, game):
    self.name = name
    self.score = 0;
    self.hand = []
    self.game = game
  
  def drawCard(self, deck):
    card = deck.pop(0)
    self.hand.append(card)
    self.score += card.numValue

  def hasBlackjack(self):
    if self.score == 21:
      print("%s got Blackjack!" % self.name)
      self.game.winner = self
      self.game.gameOver()
      return True 

  def hit(self, deck):
    while self.score < 17:
      self.drawCard(deck)

    if self.score > 21:
      self.game.winner = self.game.dealer
      self.game.gameOver()
      return False
    else:
      return True

class Dealer(Player):
  def hasBlackjack(self):
    if self.score == 22:
      print("%s got Blackjack!" % self.name)
      self.game.winner = self
      self.game.gameOver()
      return True

  def hit(self, deck, playerScore):
    while self.score <= playerScore:
      self.drawCard(deck)

    if self.score > 21:
      self.game.winner = self.game.player
      self.game.gameOver()
      return False
    else:
      return True

      

class Game:
  suites = ['C', 'D', 'H', 'S']
  values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
  def __init__(self, listOfCards):
    self.deck = self.initializeDeck(listOfCards)
    self.player = Player("Sam", self)
    self.dealer = Dealer("Dealer", self)
    self.winner = None  


  def initializeDeck(self, listOfCards):
    deck = []
    if listOfCards == None:
      for suite in self.suites:
        for value in self.values:
          deck.append(Card(suite, value))
          random.shuffle(deck)
    else:
      listOfCards = listOfCards.split(",")
      for x in listOfCards:
        x = x.strip()
        deck.append(Card(x[0], x[1:]))

    return deck

  def dealCards(self):
    for x in range(0,4):
      if x % 2 == 0:
        self.player.drawCard(self.deck)
      else:
        self.dealer.drawCard(self.deck)

  def gameOver(self):
    print("%s won!" % self.winner.name)
    print("%s: %s" % (self.player.name, self.printCards(self.player.hand)))
    print("%s: %s" % (self.dealer.name, self.printCards(self.dealer.hand)))

  ''' 
  Though it would be better to invoke sys.exit() once the game reaches gameOver() 
  than to check variables and return to main in playGame(), this would cause most of the tests 
  to fail as the program would exit and delete the variables before their values could be asserted. 
  '''
  def playGame(self):
    self.dealCards()

    if self.player.hasBlackjack():
      return

    if self.dealer.hasBlackjack():
      return
      
    if not self.player.hit(self.deck):
      return

    if not self.dealer.hit(self.deck, self.player.score):
      return 

    if self.player.score > self.dealer.score:
      self.winner = self.player
    else:
      self.winner = self.dealer

    self.gameOver()

  def printCards(self, cards):
    cardnames = []
    for card in cards:
      cardnames.append(card.suite+card.value)
    return (', ').join(cardnames)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument("-file", required=False)
  args = parser.parse_args()

  if args.file != None:
    file = open(args.file, 'r')
    listOfCards = file.read()
    file.close()
  else:
    listOfCards = None
  
  game = Game(listOfCards)
  game.playGame()

 