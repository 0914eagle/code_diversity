
def get_min_moves(a):
    # Find the starting and ending positions of the contiguous segment
    start, end = 0, 0
    for i in range(len(a)):
        if a[i] == 1:
            if start == 0:
                start = i
            end = i
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    
    # Loop until the starting and ending positions are the same
    while start != end:
        # Find the leftmost and rightmost positions of the contiguous segment
        left = start
        right = end
        for i in range(start, end+1):
            if a[i] == 1:
                left = i
                break
        for i in range(end, start-1, -1):
            if a[i] == 1:
                right = i
                break
        
        # Shift the contiguous segment to the right by 1
        if right < len(a) and a[right+1] == 0:
            a[left:right+1] = a[left+1:right+2]
            start += 1
            end += 1
            min_moves += 1
        
        # Shift the contiguous segment to the left by 1
        elif left > 1 and a[left-1] == 0:
            a[left-1:right+1] = a[left-2:right]
            start -= 1
            end -= 1
            min_moves += 1
        
        # If neither of the above conditions are met, then the contiguous segment cannot be shifted any further
        else:
            break
    
    return min_moves

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_min_moves(a))

if __name__ == '__main__':
    main()

