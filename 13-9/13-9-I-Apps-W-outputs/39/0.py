
def get_valid_scenarios(n, k, x):
    # Initialize a set to store the valid scenarios
    valid_scenarios = set()
    
    # Iterate over all possible starting positions
    for i in range(1, n+1):
        # Initialize the current position and the number of moves made
        current_position = i
        num_moves = 0
        
        # Iterate over all questions
        for j in range(k):
            # If the current position is not the question, move to the next position
            if current_position != x[j]:
                current_position = current_position + 1 if x[j] > current_position else current_position - 1
                num_moves += 1
            
            # If the current position is the question and the number of moves made is even, add the scenario to the set
            if current_position == x[j] and num_moves % 2 == 0:
                valid_scenarios.add((i, current_position))
                break
    
    return len(valid_scenarios)

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    print(get_valid_scenarios(n, k, x))

if __name__ == '__main__':
    main()

