# This script is to show the odds of my hand to make sure my chances are good as the deck continiously get smaller and smaller.
# The point of BJ is to get 21. There are numerous combinations of 21 and the best way to get it (or to get closest to 21) is to
# Make sure that your deck has high cards all around. This means you'll need to keep track of all the cards in the deck and figure out
# When the best time to hit or stay will be.

# Defining the criterion
# 52 cards total. 13 in each suit, 4 suits.
# Suit names = Diamond, Clubs, Spades, Hearts
number_of_decks = 1
number_of_players = 2
Deck_of_cards = {
    'H_Ace': 1,'H_Two': 2,'H_Three': 3,'H_Four': 4,
    'H_Five': 5,'H_Six': 6,'H_Seven': 7,'H_Eight': 8,
    'H_Nine': 9,'H_Ten': 10,'H_Jack': 10,'H_Queen': 10,
    'H_King': 10,'H_Aceuh': 11,
    'D_Ace': 1, 'D_Two': 2, 'D_Three': 3, 'D_Four': 4,
    'D_Five': 5, 'D_Six': 6, 'D_Seven': 7, 'D_Eight': 8,
    'D_Nine': 9, 'D_Ten': 10, 'D_Jack': 10, 'D_Queen': 10,
    'D_King': 10, 'D_Aceuh': 11,
    'C_Ace': 1, 'C_Two': 2, 'C_Three': 3, 'C_Four': 4,
    'C_Five': 5, 'C_Six': 6, 'C_Seven': 7, 'C_Eight': 8,
    'C_Nine': 9, 'C_Ten': 10, 'C_Jack': 10, 'C_Queen': 10,
    'C_King': 10, 'C_Aceuh': 11,
    'S_Ace': 1, 'S_Two': 2, 'S_Three': 3, 'S_Four': 4,
    'S_Five': 5, 'S_Six': 6, 'S_Seven': 7, 'S_Eight': 8,
    'S_Nine': 9, 'S_Ten': 10, 'S_Jack': 10, 'S_Queen': 10,
    'S_King': 10, 'S_Aceuh': 11
}


