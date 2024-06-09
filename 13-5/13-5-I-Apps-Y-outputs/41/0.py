
def is_valid_color_choosing(n, k, pairs):
    # Check if there are any two completely identical pairs
    for i in range(n):
        for j in range(i+1, n):
            if pairs[i] == pairs[j]:
                return False
    
    # Check if there is a pair with costumes of the same color
    for i in range(n):
        if pairs[i][0] == pairs[i][1]:
            return False
    
    # Check if for every two consecutive (adjacent) pairs, both man's costume colors and woman's costume colors differ
    for i in range(n-1):
        if pairs[i][0] == pairs[i+1][0] or pairs[i][1] == pairs[i+1][1]:
            return False
    
    return True

def get_color_choosing(n, k):
    pairs = []
    for i in range(n):
        pair = []
        for j in range(2):
            pair.append(j+1)
        pairs.append(pair)
    
    return pairs

def main():
    n, k = map(int, input().split())
    pairs = get_color_choosing(n, k)
    if is_valid_color_choosing(n, k, pairs):
        print("YES")
        for pair in pairs:
            print(pair[0], pair[1])
    else:
        print("NO")

if __name__ == '__main__':
    main()

