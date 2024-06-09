
def solve(barbarians, rounds):
    # Initialize a dictionary to store the number of consecutive substrings for each barbarian
    barbarian_substrings = {i: 0 for i in range(1, len(barbarians) + 1)}

    # Iterate through each round
    for round in rounds:
        # If the round is of type 1, show the word to Tarzan
        if round[0] == 1:
            word = round[1]
            # Iterate through each barbarian
            for i in range(1, len(barbarians) + 1):
                # If the barbarian's word is a substring of the shown word, increment their number of consecutive substrings
                if barbarians[i - 1] in word:
                    barbarian_substrings[i] += 1
        # If the round is of type 2, ask Tarzan a question about the number of consecutive substrings for the barbarian with the given label
        elif round[0] == 2:
            label = round[1]
            # Return the number of consecutive substrings for the barbarian with the given label
            yield barbarian_substrings[label]

def main():
    # Read the number of barbarians and their words from stdin
    num_barbarians = int(input())
    barbarians = [input() for _ in range(num_barbarians)]

    # Read the number of rounds from stdin
    num_rounds = int(input())
    rounds = [(int(input()), input()) for _ in range(num_rounds)]

    # Solve the problem and print the results
    for result in solve(barbarians, rounds):
        print(result)

if __name__ == "__main__":
    main()

