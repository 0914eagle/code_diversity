
def get_permutation(n, m, k, a):
    # Calculate the average score for each critic
    avg_scores = [0] * n
    for i in range(n):
        avg_scores[i] = (k - a[i]) / (n - i - 1)
    
    # Find the maximum average score
    max_avg = max(avg_scores)
    
    # Check if the maximum average score is greater than or equal to the minimum score
    if max_avg < m:
        return "impossible"
    
    # Find the index of the maximum average score
    max_index = avg_scores.index(max_avg)
    
    # Create a permutation with the maximum average score at the beginning
    permutation = [max_index + 1]
    
    # Fill in the remaining positions with the remaining critics
    for i in range(n - 1):
        permutation.append((max_index + i + 1) % n + 1)
    
    return permutation

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

