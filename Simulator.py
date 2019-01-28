from Deck import Deck
from Dealer import Dealer
from Player import Player
from Shoe import Shoe
from DiscardPile import DiscardPile
from Rules import Rules
import time


class Simulator:

    def __init__(self):
        self.number_of_games = 100000
        number_of_players = 4 # 1-7
        self.players = []
        number_of_decks = 6
        self.shoe = Shoe(number_of_decks)
        self.discard_pile = DiscardPile()

        # Add each deck to the shoe
        for deck_count in range(number_of_decks):
            self.shoe.add_deck(Deck())
        # Shuffle shoe or decks?
        self.shoe.shuffle()

        # Create dealer and give them the shoe
        self.dealer = Dealer(self.shoe, self.discard_pile)

        # Load in rules and give them to each player
        rules = Rules()

        # Add each player to game (add to players list)
        for player_count in range(number_of_players):
            self.players.append(Player(rules, player_count+1))

    def player_actions(self, player, hand_number, dealer_up_card):
        # print("-Hand " + str(hand_number+1) + ": ")
        player_move = "H"
        # Give the player cards as long as they keep hitting
        while player_move == "H" and not player.get_hands()[hand_number].is_bust():
            player_move = player.make_move(dealer_up_card, hand_number)
            # print(player_move)
            if player_move == "H":
                # Hit
                self.dealer.deal_card_to_player(player, hand_number)
        if player_move == "D":
            # Double down
            # Give 1 card to hand
            self.dealer.deal_card_to_player(player, hand_number)
            # Double bet
            player.get_hands()[hand_number].double_down()
        elif player_move == "P":
            # Split
            # Hand splits into two hands, each hand gets original bet
            print(hand_number)
            player.split_hand(hand_number)
            # Deal card to each hand
            self.dealer.deal_card_to_player(player, hand_number)
            new_hand_number = len(player.get_hands())-1
            self.dealer.deal_card_to_player(player, new_hand_number)
            self.player_actions(player, hand_number, dealer_up_card)
            self.player_actions(player, new_hand_number, dealer_up_card)

    def dealer_actions(self):
        dealer_move = "H"
        # Give the player cards as long as they keep hitting
        while dealer_move == "H" and not self.dealer.get_hand().is_bust():
            dealer_move = self.dealer.make_move()
            if dealer_move == "H":
                # Hit
                self.dealer.deal_card_to_dealer()

    def game_over(self):
        dealer_hand = self.dealer.get_hand()
        dealer_total = dealer_hand.get_hand_total()
        # print("Dealer: " + str(dealer_total))

        # Dealer and players take or give there bets
        for player in self.players:
            hands = player.get_hands()
            for hand in hands:
                hand_total = hand.get_hand_total()
                # If the player busts, then the dealer does not need to risk a bust
                if hand.is_bust():
                    self.dealer.hand_won(True, hand)
                    player.hand_won(False, hand)
                    # print("Player " + str(player.get_player_id()) + ": " + str(hand_total) + "  BUST")
                else:
                    # print("Player " + str(player.get_player_id()) + ": " + str(hand_total))

                    # If dealer has blackjack and hand is blackjack then its a push
                    win = True
                    if hand_total == dealer_total:
                        # Push (wipe bet on hand)
                        pass
                    # If dealer busted or player is closer to 21
                    elif dealer_hand.is_bust() or hand_total > dealer_total:
                        # Player gets paid 3:2 when they have blackjack
                        if hand.is_blackjack() and not player.is_split():
                            hand.blackjack_multiplier()
                        player.hand_won(True, hand)
                        self.dealer.hand_won(False, hand)
                    else:
                        player.hand_won(False, hand)
                        self.dealer.hand_won(True, hand)
                        win = False
                    # if win:
                    #     print("Player " + str(player.get_player_id()) + ": " + str(hand_total) + "  WIN")
                    #     pass
                    # else:
                    #     print("Player " + str(player.get_player_id()) + ": " + str(hand_total) + "  LOSE")
                    #     pass

        # Discard all hands
        self.dealer.discard_hands(self.players)
        # print("------")



    def run_simulation(self):
        for game in range(self.number_of_games):
            # Place bets before deal
            # Deal out the cards
            self.dealer.deal_cards(self.players)
            # All the players and dealer make their plays
            if self.dealer.has_blackjack():
                # Dealer has blackjack
                # Check which players push
                for player in self.players:
                    player.dealer_blackjack()
            else:
                # Dealer does not have blackjack
                dealer_up_card = self.dealer.get_up_card()
                player_count = 0
                for player in self.players:
                    player_count += 1
                    # print("Player " + str(player_count)+": ")
                    self.player_actions(player, 0, dealer_up_card)
                    self.dealer_actions()

            self.game_over()

    def print_winnings(self):
        player_count = 0
        print()
        for player in self.players:
            player_count += 1
            print("Player " + str(player_count) + ":")
            player.print_winnings()
            print('------------------------')
        print("DEALER:")
        self.dealer.print_winnings()



# print(str(games_played) + " games played")
# print(str(double_down) + " double down")
# print(str(split) + " split")
# print(str(hit) + " hit")



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
