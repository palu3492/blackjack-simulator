from Deck import Deck
from Dealer import Dealer
from Player import Player
from Shoe import Shoe
from DiscardPile import DiscardPile
from Rules import Rules
import time

number_of_games = 1000
games_played = 0
number_of_players = 4
players = []
number_of_decks = 6
shoe = Shoe(number_of_decks)
discard_pile = DiscardPile()

double_down = split = hit =0

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
    players.append(Player(rules, player_count+1))


def player_actions(player, hand_number, dealer_up_card):
    global split, double_down, hit
    player_move = "H"
    # Give the player cards as long as they keep hitting
    while player_move == "H" and not player.get_hands()[hand_number].is_bust():
        player_move = player.make_move(dealer_up_card, hand_number)
        if player_move == "H":
            # Hit
            hit += 1
            dealer.deal_card_to_player(player, hand_number)
    if player_move == "D":
        # Double down
        double_down += 1
        # Give 1 card to hand
        dealer.deal_card_to_player(player, hand_number)
        # Double bet
        player.get_hands()[hand_number].double_down()
    elif player_move == "P":
        # Split
        split += 1
        # Hand splits into two hands, each hand gets original bet
        player.split_hand(hand_number)
        # Deal card to each hand
        dealer.deal_card_to_player(player, hand_number)
        player_actions(player, hand_number, dealer_up_card)
        # take second card out of first hand and put it in second
        dealer.deal_card_to_player(player, hand_number+1)
        player_actions(player, hand_number+1, dealer_up_card)


def dealer_actions():
    dealer_move = "H"
    # Give the player cards as long as they keep hitting
    while dealer_move == "H" and not dealer.get_hand().is_bust():
        dealer_move = dealer.make_move()
        if dealer_move == "H":
            # Hit
            dealer.deal_card_to_dealer()


def game_over():
    dealer_hand = dealer.get_hand()
    dealer_total = dealer_hand.get_hand_total()
    print("Dealer: " + str(dealer_total))
    if dealer_hand.is_ace_in_hand() and dealer_hand.get_soft_total() <= 21:
        dealer_total = dealer_hand.get_soft_total()

    # Dealer and players take or give there bets
    for player in players:
        hands = player.get_hands()
        for hand in hands:
            # If player busted on this hand
            if hand.is_bust():
                dealer.hand_won(True, hand)
                player.hand_won(False, hand)
            else:
                hand_total = hand.get_hand_total()
                print("Player " + str(player.get_player_id()) + ": " + str(hand_total))
                # if hand.is_ace_in_hand() and hand.get_soft_total() <= 21:
                #     hand_total = hand.get_soft_total()

                # If dealer has blackjack and hand is blackjack then its a push
                if dealer.has_blackjack() and player.has_blackjack(hand):
                    # Push (wipe bet on hand)
                    pass
                # If dealer busted or player is closer to 21
                elif dealer_hand.is_bust() or hand_total > dealer_total:
                    # Player gets paid 3:2 when they have blackjack
                    if player.has_blackjack(hand):
                        hand.blackjack_multiplier()
                    player.hand_won(True, hand)
                    dealer.hand_won(False, hand)
                else:
                    player.hand_won(False, hand)
                    dealer.hand_won(True, hand)

    # Discard all hands
    dealer.discard_hands(players)
    print("------")



def run_simulation():
    global games_played
    for game in range(number_of_games):
        games_played += 1
        # Deal out the cards
        dealer.deal_cards(players)
        # All the players and dealer make their plays
        if dealer.has_blackjack():
            # Dealer has blackjack
            # Check which players push
            for player in players:
                player.dealer_blackjack()
        else:
            # Dealer does not have blackjack
            dealer_up_card = dealer.get_up_card()
            for player in players:
                player_actions(player, 0, dealer_up_card)
            dealer_actions()


        game_over()

start_time = time.time()
run_simulation()


def print_winnings():
    for player in players:
        player.print_winnings()
        print('------------------------')
    dealer.print_winnings()


print_winnings()

# print(str(games_played) + " games played")
# print(str(double_down) + " double down")
# print(str(split) + " split")
# print(str(hit) + " hit")
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