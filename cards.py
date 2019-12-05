import random
import sys

list_of_suits = ['Spades','Clubs','Hearts','Diamonds']
list_of_faces = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10,'Jack','Queen','King']

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit


class Deck:
    def __init__(self):
        self.deck = []

    def generate_deck(self):
        for suit in list_of_suits:
            for face in list_of_faces:
                card = Card(face, suit)
                self.deck.append(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        suit = self.deck[0].suit
        face = self.deck[0].face
        card = Card(face, suit)
        self.deck.pop(0)
        return card


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.hand = []


class Dealer:
    def __init__(self):
        self.hand = []


class BlackJack:
    def __init__(self):
        self.player = Player(input('Who is playing?  '))
        self.dealer = Dealer()
        self.deck = []

    def make_deck(self):
        shuffled_deck = Deck()
        shuffled_deck.generate_deck()
        shuffled_deck.shuffle_deck()
        self.deck = shuffled_deck

    def count_hand(self, hand):
        value = 0
        royalty_cards = ['Jack','Queen','King']
        for card in hand:
            if card.face in royalty_cards:
                value += 10
            elif card.face == 'Ace':
                value += 1
            else:
                value += card.face
        return value

    def game(self):
        self.player.hand.append(self.deck.draw_card())
        self.player.hand.append(self.deck.draw_card())
        self.dealer.hand.append(self.deck.draw_card())
        self.dealer.hand.append(self.deck.draw_card())
        while True:
            player_score = self.count_hand(self.player.hand)
            for card in self.player.hand:
                print(card.suit, card.face)
            print("{}'s score is {}".format(self.player.player_name, player_score))
            if player_score > 21:
                print('you bust! too bad! Dealer Wins!')
                sys.exit()
            hit_or_stay = input('do you want to hit or stay? (H/S) ')
            if hit_or_stay.upper() == 'H':
                self.player.hand.append(self.deck.draw_card())
            elif hit_or_stay.upper() == 'S':
                break
            else:
                print('That is not a correct response, please try again')
        while True:
            dealer_score = self.count_hand(self.dealer.hand)
            for card in self.dealer.hand:
                print(card.suit, card.face)
            print('Dealers score is {}'.format(dealer_score))
            if dealer_score < 17:
                self.dealer.hand.append(self.deck.draw_card())
                dealer_score = self.count_hand(self.dealer.hand)
                for card in self.dealer.hand:
                    print(card.suit, card.face)
                print('Dealers score is {}'.format(dealer_score))
            elif dealer_score > 21:
                print('Dealer bust! You win!')
                sys.exit()
            else:
                break
        if player_score > dealer_score:
            print('{} scored higher, {} win!'.format(self.player.player_name, self.player.player_name))
        elif dealer_score >= player_score:
            print('Dealer Wins!')

# This code runs the game
black_jack = BlackJack()
black_jack.make_deck()
black_jack.game()






