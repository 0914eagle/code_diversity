
def get_probability(N):
    # Calculate the total number of positive integers not greater than N
    total = (N * (N + 1)) // 2
    
    # Calculate the number of odd positive integers not greater than N
    odd = N // 2
    
    # Calculate the probability that a is odd
    probability = odd / total
    
    return probability

def main():
    N = int(input())
    probability = get_probability(N)
    print(probability)

if __name__ == '__main__':
    main()

