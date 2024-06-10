
import re

def get_winner(deck):
    # Initialize the deck and the players' hands
    deck = deck.upper()
    hand_theta = deck[:10]
    hand_friend = deck[10:20]
    deck = deck[20:]

    # Initialize the players' cards
    cards_theta = {}
    cards_friend = {}
    for i in range(1, 11):
        cards_theta[i] = hand_theta[i-1]
        cards_friend[i] = hand_friend[i-1]

    # Initialize the discard pile
    discard_pile = []

    # Initialize the game state
    state = "theta"

    # Play the game
    while len(deck) > 0:
        # Draw a card from the deck
        card = deck[0]
        deck = deck[1:]

        # Check if the card can be played
        if state == "theta":
            if card in cards_theta.values():
                continue
            if card in discard_pile:
                continue
            if card == "J" and len(cards_theta) < 10:
                continue
        else:
            if card in cards_friend.values():
                continue
            if card in discard_pile:
                continue
            if card == "J" and len(cards_friend) < 10:
                continue

        # Play the card
        if state == "theta":
            if card in cards_theta:
                cards_theta[card] = card
            else:
                discard_pile.append(card)
        else:
            if card in cards_friend:
                cards_friend[card] = card
            else:
                discard_pile.append(card)

        # Switch the game state
        state = "friend" if state == "theta" else "theta"

        # Check if a player has won
        if len(cards_theta) == 10:
            return "Theta wins"
        if len(cards_friend) == 10:
            return "Theta loses"

    # If the deck runs out of cards, the player with the most cards wins
    if len(cards_theta) > len(cards_friend):
        return "Theta wins"
    else:
        return "Theta loses"

def main():
    deck = input()
    print(get_winner(deck))

if __name__ == '__main__':
    main()

