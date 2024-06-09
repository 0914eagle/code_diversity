
def solve(barbarians, rounds):
    # Initialize a dictionary to store the count of consecutive substrings for each barbarian
    barbarian_counts = {i: 0 for i in range(1, len(barbarians) + 1)}

    # Iterate over each round
    for round in rounds:
        # If the round is of type 1, show the word to all barbarians
        if round[0] == 1:
            word = round[1]
            for i in range(1, len(barbarians) + 1):
                if word in barbarians[i - 1]:
                    barbarian_counts[i] += 1
        # If the round is of type 2, ask the question to the barbarian with the given label
        else:
            barbarian_label = round[1]
            yield barbarian_counts[barbarian_label]

# Test the function with some sample inputs and outputs
barbarians = ["a", "bc", "abc"]
rounds = [(1, "abca"), (2, 1), (2, 3)]
result = list(solve(barbarians, rounds))
print(result)  # Should print [1, 1]

barbarians = ["a", "bc", "abc"]
rounds = [(1, "abca"), (2, 1), (2, 3), (1, "def"), (2, 2)]
result = list(solve(barbarians, rounds))
print(result)  # Should print [1, 1, 0]

