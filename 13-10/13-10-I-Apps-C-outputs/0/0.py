
def get_favorite_sequence(sequence, frequency, colors):
    
    max_freq = 0
    max_seq = []
    for i in range(len(sequence)):
        if sequence[i] in colors:
            freq = frequency[sequence[i] - 1]
            if freq > max_freq:
                max_freq = freq
                max_seq = [sequence[i]]
            elif freq == max_freq:
                max_seq.append(sequence[i])
    return max_seq

def count_arrangements(n, colors, forbidden, favorite):
    
    # Initialize the frequency of each color
    frequency = [0] * n
    for i in range(n):
        frequency[colors[i] - 1] += 1
    
    # Initialize the number of arrangements
    num_arrangements = 1
    
    # Loop through each color and consider each position for that color
    for i in range(n):
        # Get the favorite sequence with the maximum frequency
        max_seq = get_favorite_sequence(favorite, frequency, colors)
        
        # If the current color is not in the favorite sequence, skip it
        if colors[i] not in max_seq:
            continue
        
        # If the current color is in the favorite sequence, consider each position for that color
        for j in range(frequency[colors[i] - 1]):
            # If the current position is not forbidden, add it to the arrangement
            if colors[i] not in forbidden:
                num_arrangements *= frequency[colors[i] - 1]
            else:
                num_arrangements *= (frequency[colors[i] - 1] - 1)
    
    return num_arrangements % 1000000007

def main():
    n, k, l = map(int, input().split())
    colors = list(map(int, input().split()))
    forbidden = list(map(int, input().split()))
    favorite = list(map(int, input().split()))
    print(count_arrangements(n, colors, forbidden, favorite))

if __name__ == '__main__':
    main()

