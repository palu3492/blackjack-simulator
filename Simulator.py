from Deck import Deck
from Dealer import Dealer
from Player import Player
from Shoe import Shoe
from DiscardPile import DiscardPile
from Rules import Rules
import time

number_of_games = 10000
games_played = 0
number_of_players = 4
players = []
number_of_decks = 6
shoe = Shoe(number_of_decks)
discard_pile = DiscardPile()

# Add each deck to the shoe
for deck_count in range(number_of_decks):
    shoe.add_deck(Deck())
# Shuffle shoe or decks?
shoe.shuffle()

# Create dealer and give them the shoe
dealer = Dealer(shoe, discard_pile)

# Load in rules and give them to each player
rules = Rules()

# Add each player to game (add to players list)
for player_count in range(number_of_players):
    players.append(Player(rules))

def game_over():
    # Discard all hands
    dealer.discard_hands(players)
    # Check who busted and who didn't
    # Players take care of money here
    #  Have the players check each of there hands to see if they won or lost
    # Also dealer (casino) should add up there money
    # if dealer had blackjack then bets are refunded for those who didn't bust
    # maybe set variable in player and dealer for difdferent winnings

start_time = time.time()
for game in range(number_of_games):
    # Deal out the cards
    dealer.deal_cards(players)
    # All the players and dealer make their plays
    if not dealer.has_blackjack():
        # Dealer has blackjack
        # Check which players have 21
        # Players with 21 take there bet back
        # Players without 21 lose there bet
        # Dealer add losers bets
        for player in players:
            player.dealer_blackjack()
    else:
        # Dealer does not have blackjack
        for player in players:
            player_move = ""
            while player_move != "S":
                dealers_card = dealer.get_up_card()
                player_move = player.make_move(dealers_card, 0)
                if player_move == "H":
                    # Player hit
                    dealer.deal_card_to_player(player)
            if player_move == "D":
                # double down
                # affects betting not hand
                # doubles the bet
                # get only one card (has to stand)
                dealer.deal_card_to_player(player)
                break
            if player_move == "P":
                # split
                # player now has two hands
                # update variable for player
                # deal card to each hand
                # each card gets original bet (double bet overall)
                # loop through hands and get players move for each (do this in player maybe)

                player.add_hand()
                # player_move = ""
                # while player_move != "S" and not player.is_bust():
                #     player_move = player.make_move(dealers_card, 0)
                #     player_move = player.make_move(dealers_card, 1)
                break

    # games_played += 1
    game_over()

# print(str(games_played) + " games played")
end_time = time.time()
print(end_time - start_time)


# if players first two cards are ace and facecard then blackjack and dealer does not have blackjack then player gets 1.5 bet
# if dealer has blackjack, he wins, all other players with blackjack tie else lose
# if the dealers face up card is a ten or ace then he checks his face down card to see if he has blackjack
#
# the dealer loops through each player and asks them if they want to hit or stand and contiues to asks until they stand or bust
# if the player busts when they have a ace then the ace turns into an 11 and they can conitue standing or hitting until they bust
# after the dealer has served every player he turns up his down card, if he has 17 or more he stands else hits and continues to until bust
# if the player gets a pair then he can choose to treat each card as there own hand and play them out as if they were each one hand, the dealer settles one hand at a time
# if the player gets a blackajack off a pair he is not paid double (on a split)
# pairs of double get one card and then they have to stand
# if the the first two cards dealt to a player are 9,10, or 11 then he can double down where the player doubel there bet but gets one card face down that they don't get flipped untill all players' bets are setteld
# if the first card a dealer gets is a ace then the players can add a sidebets, side bets are returned to the player in double if the dealer's other card is a ten else they lose the side bet
# if the dealer stands at 21 then he still pays anyone who has 21, if he stands whenever he pays any player with higher card, if dealer and player both stand and tie then no bets are paid or collected
# each discarded card sits in a pile until shuffle time when the dealer collects all cards and reshuffles them