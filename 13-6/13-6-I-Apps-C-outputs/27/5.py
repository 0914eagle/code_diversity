
def get_permutation(n, m, k, a):
    # Initialize the permutation as the identity permutation
    permutation = list(range(1, n+1))
    
    # Calculate the average score for each critic
    average_scores = [0] * n
    for i in range(n):
        average_scores[i] = (k - a[i]) / (n-i-1)
    
    # Sort the permutation based on the average scores
    permutation = sorted(permutation, key=lambda x: average_scores[x-1])
    
    return permutation

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    permutation = get_permutation(n, m, k, a)
    if permutation == []:
        print("impossible")
    else:
        print(*permutation)

if __name__ == '__main__':
    main()

