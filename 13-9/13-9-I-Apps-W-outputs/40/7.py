
def get_min_time(a, b, c):
    # Sort the sticks by length in descending order
    sticks = sorted([a, b, c], reverse=True)
    
    # Initialize the minimum time needed to form a triangle
    min_time = 0
    
    # Loop through the sticks and check if they can form a triangle
    for i in range(len(sticks)):
        if sticks[i] + sticks[i-1] > sticks[i-2]:
            # If the two shorter sticks can form a triangle, return the current minimum time
            return min_time
        else:
            # If the two shorter sticks cannot form a triangle, increase the length of the longest stick by one centimeter and add it to the minimum time
            min_time += 1
            sticks[i] += 1
    
    # If no triangle can be formed, return -1
    return -1

def main():
    a, b, c = map(int, input().split())
    print(get_min_time(a, b, c))

if __name__ == '__main__':
    main()

