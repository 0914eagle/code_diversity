
def get_num_ways(num_colors, ball_freqs, bad_colors, fav_seq):
    # Initialize a variable to store the total number of ways
    num_ways = 0
    
    # Loop through each possible combination of balls
    for combination in itertools.product(*[range(1, freq+1) for freq in ball_freqs]):
        # Check if the current combination meets the conditions
        if all(comb[i-1] != comb[i] for i in range(1, len(comb))) and all(comb[i-1] != comb[i+1] for i in range(1, len(comb)-1)):
            num_ways += 1
    
    return num_ways % 1000000007

def main():
    num_colors, num_bad_colors = map(int, input().split())
    ball_freqs = list(map(int, input().split()))
    bad_colors = set(map(int, input().split()))
    fav_seq = list(map(int, input().split()))
    
    print(get_num_ways(num_colors, ball_freqs, bad_colors, fav_seq))

if __name__ == '__main__':
    main()

