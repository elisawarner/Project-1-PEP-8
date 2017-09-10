## Do not change import statements.
import unittest
from SI507F17_project1_cards import *


## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
class Test_Card(unittest.TestCase):
	def test_string_method1(self):
		a_Card = Card(1,3)
		self.assertEqual(a_Card.__str__(), "3 of Clubs", "testing string method Card with number value")
	def test_suit(self):
		a_Card = Card(1,3)
		self.assertEqual(a_Card.suit,"Clubs","testing suit variable")
	def test_rank_num(self):
		a_Card = Card(1,3)
		self.assertEqual(a_Card.rank_num,3,"testing rank_num variable")
	def test_rank(self):
		a_Card = Card(1,12)
		self.assertEqual(a_Card.rank,"Queen","testing rank variable")
	def test_rank(self):
		a_Card = Card(1,12)
		self.assertEqual(a_Card.rank_num,12,"testing rank_num variable")
	# Error #1: Doesn't give face value of cards
	def test_string_method2(self):
		a_Card = Card(2,1)
		self.assertEqual(a_Card.__str__(), "Ace of Hearts", "testing string method of Card with face value")

class Test_Deck(unittest.TestCase):
	def test_Deck1(self):
		a_Deck = Deck()
		self.assertEqual(type(a_Deck.cards),type([1,2,3]),"testing cards variable is a list")
	def test_Deck2(self):
		a_Deck = Deck()
		Deck_string = a_Deck.__str__()
		self.assertIn("3 of Hearts",Deck_string,"testing string method of Deck with number value")
	def test_Deck3(self):
		a_Deck = Deck()
		Deck_string = a_Deck.__str__()
		self.assertEqual(len(Deck_string.split('\n')),52,"testing number of cards in the deck")
	def test_Deck4(self):
		a_Deck = Deck()
		a_Deck.deal_hand(2)
		self.assertEqual(len(a_Deck.cards),50,"testing deal_hand removes cards from deck")
	def test_Deck4(self):
		a_Deck = Deck()
		a_Deck.pop_card(2)
		self.assertEqual(len(a_Deck.cards),51,"testing that pop_card removes cards from deck")
	# Error #2: sort_cards does not sort remaining cards in deck: gives full deck length
	def test_Deck5(self):
		a_Deck = Deck()
		a_Deck.deal_hand(3)
		a_Deck.sort_cards()
		self.assertEqual(len(a_Deck.cards),49,"testing that sort_cards sorts only remaining cards in deck")
	# Error #1: must reference Cards method, doesn't give face value of card
	def test_Deck6(self):
		a_Deck = Deck()
		Deck_string = a_Deck.__str__()
		self.assertIn("Ace of Hearts",Deck_string,"testing string method of Deck with face value")
	def test_Deck7(self):
		a_Deck = Deck()
		self.assertEqual(len(a_Deck.deal_hand(5)),5,"testing length of deal_hand")
	def test_Deck7(self):
		a_Deck = Deck()
		self.assertEqual(len(a_Deck.deal_hand(52)),52,"testing maximum length that deal_hand can take from deck")
	# Error #3: deal_hand cannot handle taking out large values from deck
	def test_Deck8(self):
		a_Deck = Deck()
		self.assertEqual(len(a_Deck.deal_hand(30)),30,"testing large inputs for deal_hand to take from deck")
	def test_Deck9(self):
		a_Deck = Deck()
		self.assertEqual(len(a_Deck.deal_hand(20)),20,"testing medium inputs for deal_hand to take from deck")


class Test_play_war_game(unittest.TestCase):
	def test_return(self):
		self.assertEqual(type(play_war_game(testing=True)),type((1,2)),"testing that return is a tuple")

unittest.main(verbosity=2)
