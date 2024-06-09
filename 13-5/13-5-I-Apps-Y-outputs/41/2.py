
def is_valid_color_choosing(n, k, b_colors, g_colors):
    # Check if there are no two completely identical pairs
    for i in range(n):
        for j in range(i+1, n):
            if b_colors[i] == b_colors[j] and g_colors[i] == g_colors[j]:
                return False
    
    # Check if there is no pair such that the color of the man's costume is the same as the color of the woman's costume
    for i in range(n):
        if b_colors[i] == g_colors[i]:
            return False
    
    # Check if for each two consecutive (adjacent) pairs, both man's costume colors and woman's costume colors differ
    for i in range(n-1):
        if b_colors[i] == b_colors[i+1] or g_colors[i] == g_colors[i+1]:
            return False
    
    return True

def get_color_choosing(n, k):
    # Initialize the colors of the costumes of pairs
    b_colors = [0] * n
    g_colors = [0] * n
    
    # Loop through each pair and assign a color to the man and woman
    for i in range(n):
        b_colors[i] = i % k + 1
        g_colors[i] = (i + 1) % k + 1
    
    # Check if the color choosing is valid
    if is_valid_color_choosing(n, k, b_colors, g_colors):
        return b_colors, g_colors
    else:
        return None

def main():
    n, k = map(int, input().split())
    b_colors, g_colors = get_color_choosing(n, k)
    if b_colors is None:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            print(b_colors[i], g_colors[i])

if __name__ == '__main__':
    main()

