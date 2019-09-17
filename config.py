# All settings for everything in simulator
simulator_settings = {
    'number_of_games': 100000
}
# settings for each individual game (might want to split these up)
# all game settings apply to the simulator because all game settings are reused each time the simulator starts a new game
game_settings = {
    # General -----------------------------------------
    'number_of_decks': 6,
    # If im doing a number I could either only allow ints in a range or have drop down
    'number_of_players': 4, # 1-7 [1,2,3,4,5,6,7][5]
    # Player loses ONLY original bet against dealer BJ (BJs are 1.5x)
    'player_bj_bet': False,
    # Plastic insert shoe card for shuffle (could go into a shuffle settings)
    'shoe_insert': True,
    # Double down -----------------------------------------
    # Double down on which totals: Any first two cards, any hard total, any soft total,  9-11 only,  10-11 only, 11 only, 9 only, 8 only, A9 only, A8 only
    'allow_dd_on_total': ['any', 'never', 'hard', 'soft', '', ''],
    # Ace always counts as 1 when doubling: Yes or no
    'dd_ace_is_one': False,
    # Double down after how many cards dealt: 2 cards, 3 cards, any amount of cards
    'dd_after_amount_delt': ['2', '3', 'any'],
    # Double down after split: Yes or no
    'dd_after_split': True,
    # Redouble: Yes or no (Double again after drawing a card on the first double)
    'redouble': True,
    # Discard double cards: Yes or no
    'discard_dd': False,
    # Hit after Double Down: Yes or no (This rule does not actually exist)
    'dd_hit': False
}
'''
Double down --
Double down on which totals: Any first two cards, any hard total, any soft total,  9-11 only,  10-11 only, 11 only, 9 only, 8 only, A9 only, A8 only
Ace always counts as 1 when doubling: Yes or no
Double down after how many cards dealt: 2 cards, 3 cards, any amount of cards
Double down after split: Yes or no
Redouble: Yes or no (Double again after drawing a card on the first double)
Discard double cards: Yes or no
Hit after Double Down*: Yes or no (This rule does not actually exist)


Split --
Resplit # of times: 1, 2, 3, 4, 5, 6, infinite
Resplit Aces: Yes or no
No Ace Splits: Yes or no
Multiple draw after split Aces: Yes or no
Blackjack on split aces: Yes or no
Split tens must be same value (exact pairs): Yes or no
Split any time (pair together still): Yes or no
Split any 16 (don't need pair): Yes or no
Discards split: Yes or no
No 4, 5 or Ten splits: Yes or no


Insurance --
Insurance when dealer has a ace: Yes or no
Insurance when dealer has a ten: Yes or no
Insurance only when player has blackjack: Yes or no
Insurance for full amount: Yes or no

Surrender Rules --
Late surrender: Yes or no (Get half of bet back. Only when dealer does not have blackjack)
Early surrender: Yes or no (Get half of bet back. Before dealer checks if they have blackjack)
Early Surrender vs. 10: Yes or no (Not sure what this is)
Surrender any number of cards: Yes or no
Surrender after Double: Yes or no
Insure then surrender: Yes or no
Surrender after split: Yes or no

Win/Play Variations --
Player 21 ties dealer 10 up Blackjack: Yes or no (Dealer would have to check for blackjack after hands settled)
Dealer wins tied: 17, 17 - 19, everything
Number of cards unbusted wins: 5, 6, 7 (Obviously 5 would include 6 and 7)
Player 22 counts as 21: Yes or no
Dealer ten up exposes hole card: Yes or no

Card Handling Variations --
Cards dealt face down: Yes or no
No dealer hole card dealt until hands are settled: Yes or no (Few bet changes are associated with this)
Double Down dealt face up: Yes or no (Maybe move this to double down section)
Burn cards after each shoe shuffle: Yes or no / 5 or 6 (Look in to this, is there a normal amount of cards to be burned?)
Burn card before each round: Yes or no (Look up if this burnt card is ever shown)
Dealer shows burn cards: Yes or no (Maybe add a option for number of burn cards after a shuffle)
Dealer peeks on 10: Yes or no (I think this may conflict other rules)
Dealer peeks on Ace: Yes or no (I think this may conflict other rules)

Bonuses Variations -- (Look for conflicts here, also each option needs a 'no bonus' option)
Suited AJ pays 2 to 1: Yes or no (Pay 2:1 instead of the normal 3:2)
Any ace and a jack of hearts pays 2 to 1: Yes or no
3 sevens pays: 2 to 1, 3 to 2
Three suited sevens pays 10 to 1: Yes or no
Blackjack pays: 3 to 2,  6 to 5, 2 to 1, no bonus
Five card 21 pays 2 to 1: Yes or no
Six card 21 pays 2 to 1: Yes or no
Split tens then draw ace is BJ: Yes or no (Maybe move to split section)
Split aces then draw ten is BJ: Yes or no
Blackjack ties are paid one-half the bet instead of pushing: Yes or no
Suited 678 pay 2 to 1: Yes, no, only if win
Blackjack rounded up: Yes or no

'''
dealer_settings = {
    'hit_soft_17': True
}
player_settings = {
    'play_rules': 'rules/basicStrategy.csv' # Strategy the player is using
}
