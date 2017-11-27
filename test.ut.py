#! /usr/bin/env python
from blackjack import Game
import unittest

class testGame(unittest.TestCase):
  def test1(self):
    ''' Cards generated deck are dealt in the correct order ''' 
    self.game = Game(None)
    cards = self.game.deck[0:4]
    self.game.dealCards()
    playerHand = self.game.player.hand
    dealerHand = self.game.dealer.hand
    self.assertEqual(playerHand[0], cards[0])
    self.assertEqual(dealerHand[0], cards[1])
    self.assertEqual(playerHand[1], cards[2])
    self.assertEqual(dealerHand[1], cards[3])
 
  def test2(self):
    ''' Cards from provided deck are dealt in the correct order '''
    self.listOfCards = "DA, D4, HK, SK, S5, S9, D10"
    self.game = Game(self.listOfCards)
    cards = self.game.deck[0:4]
    self.game.dealCards()
    playerHand = self.game.player.hand
    dealerHand = self.game.dealer.hand
    self.assertEqual(playerHand[0], cards[0])
    self.assertEqual(dealerHand[0], cards[1])
    self.assertEqual(playerHand[1], cards[2])
    self.assertEqual(dealerHand[1], cards[3])

  def test3(self):
    '''Player gets Blackjack'''
    self.listOfCards = "DA, D4, HK, SK, S5, S9, D10"
    self.game = Game(self.listOfCards)
    self.assertEqual(self.game.player.score, 0)
    self.game.dealCards()
    self.game.player.hasBlackjack()
    self.assertEqual(self.game.player.score, 21)
    self.assertEqual(self.game.winner, self.game.player)

  def test4(self):
    ''' Player loses as the first two cards gives a score > 21 '''
    self.listOfCards = "DA, D4, H3, SK, S8, S9, D10"
    self.game = Game(self.listOfCards)
    self.game.dealCards()
    self.game.player.hit(self.game.deck)
    self.assertTrue(self.game.player.score > 21)
    self.assertEqual(self.game.winner, self.game.dealer)

  def test5(self):
    ''' Player stops drawing cards once score is > 17 '''
    self.listOfCards = "D5, D4, H6, SK, S5, S2, D2, H7"
    self.game = Game(self.listOfCards)
    self.game.dealCards()
    self.player = self.game.player
    self.game.player.hit(self.game.deck)
    self.assertTrue(self.player.score > 17)
    self.assertTrue(self.player.score < 21)

  def test6(self):
    ''' Dealer gets highest score and wins the game '''
    self.listOfCards = "D5, D7, H6, S8, S5, S2, D3, H3"
    self.game = Game(self.listOfCards)    
    self.game.dealCards()
    self.assertIsNone(self.game.winner)
    self.game.playGame()
    self.assertTrue(self.game.player.score < self.game.dealer.score)
    self.assertEqual(self.game.winner, self.game.dealer)

  def test7(self):
    ''' Generated deck of cards contains 52 unique elements '''
    self.game = Game(None)    
    self.assertEqual(len(set(self.game.deck)), 52)
    
if __name__ == '__main__':
    unittest.main()