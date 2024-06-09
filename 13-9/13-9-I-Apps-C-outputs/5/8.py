
def solve(n, s, predictions):
    # Initialize an array to store the counts of each prediction
    count = [0] * s

    # Iterate over each prediction
    for i in range(s):
        # Get the length of the current prediction
        length = len(predictions[i])

        # Initialize a set to store the unique symbols in the prediction
        symbols = set()

        # Iterate over each symbol in the prediction
        for j in range(length):
            # Add the symbol to the set
            symbols.add(predictions[i][j])

        # Iterate over each symbol in the set
        for symbol in symbols:
            # Initialize a count for the symbol
            count_symbol = 0

            # Iterate over each symbol in the prediction
            for j in range(length):
                # If the symbol is the same as the current symbol, increment the count
                if predictions[i][j] == symbol:
                    count_symbol += 1

            # Add the count to the total count
            count[i] += count_symbol

    # Sort the predictions by count in descending order
    sorted_predictions = sorted(range(s), key=lambda i: count[i], reverse=True)

    # Return the sorted predictions
    return [predictions[i] for i in sorted_predictions]

