
def get_permutation(n, m, k, a):
    # Initialize the permutation with the first critic
    permutation = [1]
    # Initialize the average score with the initial opinion of the first critic
    avg_score = a[0]
    # Iterate over the remaining critics
    for i in range(1, n):
        # Calculate the average score of the previous critics
        prev_avg_score = avg_score
        # Update the average score with the current critic's opinion
        avg_score = (avg_score * i + a[i]) / (i + 1)
        # If the current critic's opinion is greater than the average score, add them to the permutation
        if a[i] > avg_score:
            permutation.append(i + 1)
    # If the average score is equal to the target score, return the permutation
    if avg_score == k / n:
        return permutation
    # Otherwise, return "impossible"
    return "impossible"

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_permutation(n, m, k, a))

if __name__ == '__main__':
    main()

