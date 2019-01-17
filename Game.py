from Deck import Deck
from Card import Card
from Dealer import Dealer
from Player import Player
from Shoe import Shoe
from DiscardPile import DiscardPile
import time

number_of_games = 100000
number_of_players = 1
players = []
number_of_decks = 1
shoe = Shoe()
number_of_cards = 52 * number_of_decks
discard_pile = DiscardPile()

# Add each deck to the shoe
for deck_count in range(number_of_decks):
    shoe.add_deck(Deck())
shoe.shuffle()

# Create dealer and give them the shoe
dealer = Dealer(shoe)

# Add each player to game (add to players list)
for player_count in range(number_of_players):
    players.append(Player())

def game_over():
    #add player and dealer hands to discard pile
    #clear player
    for player in players:
        discard_pile.add_cards(player.get_hand())
        player.set_hand([])

#start_time = time.time()
for game in range(number_of_games):

    dealer.deal_cards(players)

    # This is where all the players make their decisions about the game
    for player in players:
        player_move = ""
        if not player.is_bust() or player_move != "S":
            player_move = player.make_move(dealer.get_hand())
            if player_move == "S":
                pass
            else:
                player.add_card_to_hand(dealer.deal_card_to_palyer(player))



    game_over()


#end_time = time.time()
#print(end_time - start_time)


#if players first two cards are ace and facecard then blackjack and dealer does not have blackjack then player gets 1.5 bet
#if dealer has blackjack, he wins, all other players with blackjack tie else lose
#if the dealers face up card is a ten or ace then he checks his face down card to see if he has blackjack

#the dealer loops through each player and asks them if they want to hit or stand and contiues to asks until they stand or bust
#if the player busts when they have a ace then the ace turns into an 11 and they can conitue standing or hitting until they bust
#after the dealer has served every player, he turns up with face card, if he has 17 or more he stands else hits and continues to until bust
#if they player gets a pair then he can choose to treat each as there own hand and play them out as if they were each one hand, the dealer settles one hand at a time
#if the player gets a blackajack off a pair he is not paid double
#pairs of double get one card and then they have to stand
#if the the first two cards dealt to a player are 9,10, or 11 then he can double down where the player doubel there bet but gets one card face down that they don't get flipped untill all players' bets are setteld
#if the first card a dealer gets is a ace then the players can add a sidebets, side bets are returned to the player in double if the dealer's other card is a ten else they lose the side bet
#if the dealer stands at 21 then he still pays anyone who has 21, if he stands whenever he pays any player with higher card, if dealer and player both stand and tie then no bets are paid or collected
#each discarded card sits in a pile until shuffle time when the dealer collects all cards and reshuffles them



# while True:
#     for deck_count in range(number_of_decks):
#         dealer.add_deck(Deck())
#     for player_count in range(number_of_players):
#         dealer.add_deck(Player())