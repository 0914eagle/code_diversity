
def f1(a, b):
    # Calculate the maximum number of shovels that can be crafted with a given number of sticks and diamonds
    max_shovels = a // 2

    # Calculate the maximum number of swords that can be crafted with a given number of sticks and diamonds
    max_swords = b // 2

    # Calculate the maximum number of emeralds that can be earned by crafting shovels and swords
    max_emeralds = max_shovels + max_swords

    return max_emeralds

def f2(a, b):
    # Calculate the maximum number of emeralds that can be earned by crafting shovels and swords
    max_emeralds = f1(a, b)

    # Calculate the maximum number of emeralds that can be earned by selling tools
    max_emeralds_sold = max_emeralds * 1

    return max_emeralds_sold

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(f2(a, b))

