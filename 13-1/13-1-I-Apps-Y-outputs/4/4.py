
def compare_cards(card1, card2):
    card_values = {
        1: "Weak",
        2: "Weak",
        3: "Weak",
        4: "Weak",
        5: "Weak",
        6: "Weak",
        7: "Weak",
        8: "Weak",
        9: "Weak",
        10: "Weak",
        11: "Weak",
        12: "Weak",
        13: "Strong"
    }
    card1_value = card_values[card1]
    card2_value = card_values[card2]
    if card1_value == card2_value:
        return "Draw"
    elif card1_value == "Strong":
        return "Alice"
    else:
        return "Bob"

def main():
    card1, card2 = map(int, input().split())
    outcome = compare_cards(card1, card2)
    print(outcome)

if __name__ == '__main__':
    main()

