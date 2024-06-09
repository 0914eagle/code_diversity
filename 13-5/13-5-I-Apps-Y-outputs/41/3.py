
def is_valid_color_choosing(n, k, b_list, g_list):
    # Check if there are any duplicate pairs
    for i in range(n):
        for j in range(i+1, n):
            if b_list[i] == b_list[j] and g_list[i] == g_list[j]:
                return False
    
    # Check if there are any pairs with the same color
    for i in range(n):
        if b_list[i] == g_list[i]:
            return False
    
    # Check if there are any consecutive pairs with the same color
    for i in range(n-1):
        if b_list[i] == b_list[i+1] or g_list[i] == g_list[i+1]:
            return False
    
    return True

def get_color_choosing(n, k):
    b_list = []
    g_list = []
    for i in range(n):
        b_list.append(i%k+1)
        g_list.append((i+1)%k+1)
    
    if is_valid_color_choosing(n, k, b_list, g_list):
        return "YES\n" + "\n".join([str(b) + " " + str(g) for b, g in zip(b_list, g_list)])
    else:
        return "NO"

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_color_choosing(n, k))

