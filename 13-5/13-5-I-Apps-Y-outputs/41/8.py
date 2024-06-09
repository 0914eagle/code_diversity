
def is_valid_color_choosing(b_colors, g_colors, n, k):
    # Check if there are any two completely identical pairs
    for i in range(n):
        for j in range(i+1, n):
            if b_colors[i] == b_colors[j] and g_colors[i] == g_colors[j]:
                return False
    
    # Check if there is a pair with costumes of the same color
    for i in range(n):
        if b_colors[i] == g_colors[i]:
            return False
    
    # Check if there are any two consecutive pairs with the same color
    for i in range(n-1):
        if b_colors[i] == b_colors[i+1] or g_colors[i] == g_colors[i+1]:
            return False
    
    return True

def get_color_choosing(n, k):
    b_colors = []
    g_colors = []
    for i in range(n):
        b_colors.append(i%k+1)
        g_colors.append((i+1)%k+1)
    
    if is_valid_color_choosing(b_colors, g_colors, n, k):
        return "YES\n" + "\n".join([str(b) + " " + str(g) for b, g in zip(b_colors, g_colors)])
    else:
        return "NO"

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_color_choosing(n, k))

