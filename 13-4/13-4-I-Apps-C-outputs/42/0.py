
def get_max_distinct_ranks(N, K, a, b):
    # Initialize a dictionary to store the ranks
    ranks = {}
    
    # Loop through each assistant and their measurements
    for i in range(N):
        # Check if the assistant is already in the ranks dictionary
        if i not in ranks:
            # If not, add it to the ranks dictionary with a rank of 1
            ranks[i] = 1
        else:
            # If the assistant is already in the ranks dictionary, check if it can be ranked higher
            can_be_ranked_higher = False
            for j in range(N):
                if i != j and (a[i] + K < a[j] or b[i] + K < b[j]):
                    can_be_ranked_higher = True
                    break
            if can_be_ranked_higher:
                # If the assistant can be ranked higher, increment its rank
                ranks[i] += 1
    
    # Return the maximum number of distinct ranks
    return max(ranks.values())

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_max_distinct_ranks(N, K, a, b))

if __name__ == '__main__':
    main()

