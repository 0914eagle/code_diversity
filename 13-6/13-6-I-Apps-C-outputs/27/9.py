
def get_permutation(n, m, k, a):
    # Initialize the permutation as a list of numbers from 1 to n
    permutation = list(range(1, n+1))
    # Initialize the average score as 0
    avg_score = 0
    # Iterate through the permutation and calculate the average score
    for i in range(n):
        # Calculate the average score for the current permutation
        avg_score = (avg_score * i + a[permutation[i]-1]) / (i+1)
        # If the average score is greater than or equal to k/n, return the permutation
        if avg_score >= k/n:
            return permutation
    # If the average score is never greater than or equal to k/n, return "impossible"
    return "impossible"

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    permutation = get_permutation(n, m, k, a)
    if permutation == "impossible":
        print("impossible")
    else:
        print(*permutation)

if __name__ == '__main__':
    main()

