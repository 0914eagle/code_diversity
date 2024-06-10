
import itertools

def get_possible_suspects(n_coders, min_agreed, coder_pairs):
    # Initialize a set to store the possible suspects
    possible_suspects = set()
    
    # Iterate over the coder pairs and check if at least one of the two coders is in the possible suspects set
    for coder1, coder2 in coder_pairs:
        if coder1 in possible_suspects or coder2 in possible_suspects:
            possible_suspects.add(coder1)
            possible_suspects.add(coder2)
    
    # Return the number of possible suspects that are also in the possible suspects set
    return len([suspect for suspect in range(1, n_coders + 1) if suspect in possible_suspects])

def count_possible_suspect_pairs(n_coders, min_agreed, coder_pairs):
    # Get the possible suspects for each coder pair
    possible_suspects = [get_possible_suspects(n_coders, min_agreed, coder_pairs) for _ in range(n_coders)]
    
    # Count the number of possible suspect pairs
    return sum(itertools.combinations(possible_suspects, 2))

def main():
    n_coders, min_agreed = map(int, input().split())
    coder_pairs = [tuple(map(int, input().split())) for _ in range(n_coders)]
    print(count_possible_suspect_pairs(n_coders, min_agreed, coder_pairs))

if __name__ == '__main__':
    main()

