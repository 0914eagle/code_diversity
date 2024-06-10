
def get_winner(hand):
    # Initialize the winner as None
    winner = None

    # Define the suits and ranks of the cards
    suits = ["S", "H", "D", "C"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

    # Define the slots for each player
    slots = [[], []]
    for i in range(10):
        slots[0].append(ranks[i])
        slots[1].append(ranks[i])

    # Loop through each card in the hand
    for card in hand:
        # Get the suit and rank of the card
        suit = card[1]
        rank = card[0]

        # Check if the card is a Jack
        if rank == "J":
            # If the card is a Jack, check if it can fill any of the slots
            for i in range(10):
                if slots[0][i] == "J" or slots[1][i] == "J":
                    # If the card can fill a slot, fill it and break
                    slots[0][i] = rank
                    slots[1][i] = rank
                    break
        else:
            # If the card is not a Jack, check if it can fill any of the slots
            for i in range(10):
                if slots[0][i] == rank or slots[1][i] == rank:
                    # If the card can fill a slot, fill it and break
                    slots[0][i] = rank
                    slots[1][i] = rank
                    break

    # Check if either player has won
    for i in range(10):
        if slots[0][i] == "J" or slots[1][i] == "J":
            # If either player has a Jack, they have not won
            continue
        elif slots[0][i] == ranks[i] and slots[1][i] == ranks[i]:
            # If both players have the same rank in the same slot, they have won
            winner = "Theta"
            break
        else:
            # If one player has a rank and the other does not, the other player has won
            winner = "Theta" if slots[0][i] != ranks[i] else "Friend"
            break

    # Return the winner
    return winner

def main():
    hand = input("Enter the shuffled deck: ")
    print(get_winner(hand))

if __name__ == '__main__':
    main()

