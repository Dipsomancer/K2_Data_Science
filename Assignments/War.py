from random import shuffle
import itertools

#Start Game

class NewGame:

    def __init__(self):

    #Create a deck

        class Deck:

            def __init__(self):
                RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q','K','A']
                SUITS = ['C','D','H','S']
                self.CARDS = list(itertools.product(RANKS, SUITS))
                shuffle(self.CARDS)

            def DealCard(self):
                return self.CARDS.pop()

            def ShowRemainingCards(self):
                return self.CARDS

        #Create Player's hand

        class PlayersHand:

            def __init__(self, STARTINGHAND=26):
                self.HAND = []
                self.STARTINGHAND = STARTINGHAND
                for i in range (self.STARTINGHAND):
                    self.HAND.append(DECK.DealCard())

            def ShowHand(self):
                return self.HAND

        #Finish Initializing Game - Create Deck, Hand Size, and Hands

        DECK = Deck()

        CARDS = int(input('What would you like the hand size to be? '))

        PLAYERSHAND = PlayersHand(CARDS)

        COMPUTERSHAND = PlayersHand(CARDS)

        class Round:

            def __init__(self):

                #Take the top card from each players hand

                self.CARDLOOKUP = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':11, 'Q':12, 'K':13, 'A':14}
                self.RANKLOOKUP = {2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 'J':'Jack', 'Q':'Queen', 'K':'King', 'A':'Ace'}
                self.SUITLOOKUP = {'S':'Spades', 'H':'Hearts', 'D':'Diamonds', 'C':'Clubs'}

                PLAYERSCARD = PLAYERSHAND.HAND[0]
                COMPUTERSCARD = COMPUTERSHAND.HAND[0]

                #Start Round logic

                #If player wins, move top player card and computer's card to bottom of the player's deck

                if self.CARDLOOKUP[PLAYERSCARD[0]] > self.CARDLOOKUP[COMPUTERSCARD[0]]:
                    PLAYERSHAND.HAND.append(COMPUTERSHAND.HAND.pop(0))
                    PLAYERSHAND.HAND.append(PLAYERSHAND.HAND.pop(0))
                    print('You won with the %s of %s vs. the %s of %s' % (self.RANKLOOKUP[PLAYERSCARD[0]], self.SUITLOOKUP[PLAYERSCARD[1]], self.RANKLOOKUP[COMPUTERSCARD[0]], self.SUITLOOKUP[COMPUTERSCARD[1]]))
                    print('The computer has %s cards' % (len(COMPUTERSHAND.HAND)))
                    print('You have %s cards' % (len(PLAYERSHAND.HAND)))
                #If computer wins, move top computer card and player's card to bottom of the computer's deck

                elif self.CARDLOOKUP[PLAYERSCARD[0]] < self.CARDLOOKUP[COMPUTERSCARD[0]]:
                    COMPUTERSHAND.HAND.append(PLAYERSHAND.HAND.pop(0))
                    COMPUTERSHAND.HAND.append(COMPUTERSHAND.HAND.pop(0))
                    print('The computer won with the %s of %s vs. the %s of %s' % (self.RANKLOOKUP[COMPUTERSCARD[0]], self.SUITLOOKUP[COMPUTERSCARD[1]], self.RANKLOOKUP[PLAYERSCARD[0]], self.SUITLOOKUP[PLAYERSCARD[1]]))
                    print('The computer has %s cards' % (len(COMPUTERSHAND.HAND)))
                    print('You have %s cards' % (len(PLAYERSHAND.HAND)))
                #In case of a tie, each player moves the top card to the back of the deck, and play continues

                else:
                    COMPUTERSHAND.HAND.append(COMPUTERSHAND.HAND.pop(0))
                    PLAYERSHAND.HAND.append(PLAYERSHAND.HAND.pop(0))
                    print('Tie!')
                    print('The computer has %s cards' % (len(COMPUTERSHAND.HAND)))
                    print('You have %s cards' % (len(PLAYERSHAND.HAND)))

        #Start Game logic loop that will create rounds

        class GameLogic:

            def __init__(self):
                while len(PLAYERSHAND.HAND) > 0 and len(COMPUTERSHAND.HAND) > 0:
                    Round()
                else:
                    if len(PLAYERSHAND.HAND) == 0:
                        print('Sorry, you lost :/')
                    if len(COMPUTERSHAND.HAND) == 0:
                        print('You won!')

        GameLogic()

NewGame()
