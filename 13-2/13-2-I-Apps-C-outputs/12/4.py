
def find_best_subsequence(k, answers):
    # Initialize variables
    best_subsequence = []
    current_subsequence = []
    success_rate = 0
    best_success_rate = 0
    f = 0
    l = 0

    # Iterate through the answers
    for i, answer in enumerate(answers):
        # If the answer is correct, add it to the current subsequence
        if answer == "1":
            current_subsequence.append(i)
        # If the answer is incorrect or the subsequence is full
        else:
            # If the subsequence is full and the success rate is higher than the best success rate, update the best subsequence
            if len(current_subsequence) == k and success_rate > best_success_rate:
                best_subsequence = current_subsequence
                best_success_rate = success_rate
                f = current_subsequence[0]
                l = len(current_subsequence)
            # Reset the current subsequence and success rate
            current_subsequence = []
            success_rate = 0

        # Update the success rate
        success_rate += 1 / len(current_subsequence)

    # If the last subsequence is not empty and the success rate is higher than the best success rate, update the best subsequence
    if len(current_subsequence) > 0 and success_rate > best_success_rate:
        best_subsequence = current_subsequence
        best_success_rate = success_rate
        f = current_subsequence[0]
        l = len(current_subsequence)

    return f, l

if __name__ == '__main__':
    k = int(input())
    answers = input()
    f, l = find_best_subsequence(k, answers)
    print(f, l)

