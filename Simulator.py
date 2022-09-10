from Deck import Deck
from Dealer import Dealer
from Player import Player
from Shoe import Shoe
from DiscardPile import DiscardPile
from PlayerStrategy import PlayerStrategy
from HouseRules import HouseRules
import time
import config
from Game import Game


class Simulator:
    """
    Simulates games of Blackjack, played out based on the set configuration.
    Everything about a game of Blackjack is simulated from how the shoe is put together
    to each player's betting and card counting strategy.
    Each individual hand of Blackjack is played out in the Game class.
    """

    def __init__(self):
        self.number_of_games = 0
        self.number_of_decks = 0
        self.number_of_players = 0
        self.shoe = None
        self.discard_pile = DiscardPile()
        self.house_rules = HouseRules()
        self.players = []
        self.dealer = None

    # Public

    def run_simulation(self):
        self.set_up_simulator()
        self.create_shoe()
        self.create_dealer()
        self.create_players()
        # Plays all the games of Blackjack
        for i in range(self.number_of_games):
            game = Game(self.shoe, self.discard_pile, self.dealer, self.players)
            game.play_game()

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

    # Private
    def set_up_simulator(self):
        """Loads in the simulator config and sets up the sim based on those settings"""
        self.log_config()
        self.number_of_games = config.simulator_settings['number_of_games']
        self.number_of_decks = config.game_settings['number_of_decks']
        self.number_of_players = config.game_settings['number_of_players']

    def create_dealer(self):
        """Create dealer and give them the shoe"""
        self.dealer = Dealer(self.shoe, self.discard_pile)

    def create_shoe(self):
        """Creates each card in the shoe and shuffles it"""
        self.shoe = Shoe(self.number_of_decks)
        # Add each deck to the shoe
        for deck_count in range(self.number_of_decks):
            self.shoe.add_deck(Deck())
        # Shuffle shoe or decks?
        # May want to move this to the start game function
        self.shoe.shuffle()

    def create_players(self):
        """Creates each player for the sim and sets their playing strategies"""
        # Load in rules and give them to each player
        player_strategy = PlayerStrategy()
        # Players at the table (will be used for every game)
        for player_count in range(self.number_of_players):
            self.players.append(Player(player_strategy, player_count + 1, self.house_rules))

    def log_config(self):
        simulator_settings = config.simulator_settings
        game_settings = config.game_settings
        config_string = f"Simulator Configuration\n" \
                        f"----------------------------------------------\n" \
                        f"Simulator:\n" \
                        f"  Games being played: {simulator_settings['number_of_games']}\n" \
                        f"Gameplay:\n" \
                        f"  Number of decks: {game_settings['number_of_decks']}\n" \
                        f"  Number of players: {game_settings['number_of_players']}\n" \
                        f"  Player loses against Blackjack: {game_settings['player_bj_bet']}\n" \
                        f"  Shoe insert: {game_settings['shoe_insert']}\n" \
                        f"  Allow double down: {game_settings['allow_dd_on_total']}\n" \
                        f"  Double down ace is one: {game_settings['dd_ace_is_one']}\n" \
                        f"  Double down after: {game_settings['dd_after_amount_delt']}\n" \
                        f"  Double down split: {game_settings['dd_after_split']}\n" \
                        f"  Double down again: {game_settings['redouble']}\n" \
                        f"  Double down discard: {game_settings['discard_dd']}\n" \
                        f"  Double down hit: {game_settings['dd_hit']}\n"
        print(config_string)


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
