
def is_good_arrangement(arrangement):
    # Check if the arrangement is a valid one
    if len(arrangement) != R * C:
        return False
    
    # Check if the arrangement has the correct number of each flavor
    if len([x for x in arrangement if x == 'A']) != a:
        return False
    if len([x for x in arrangement if x == 'B']) != b:
        return False
    if len([x for x in arrangement if x == 'C']) != c:
        return False
    
    # Check if the arrangement has two adjacent bonbons of the same color
    for i in range(R - 1):
        for j in range(C - 1):
            if arrangement[i * C + j] == arrangement[i * C + j + 1] or arrangement[i * C + j] == arrangement[(i + 1) * C + j]:
                return False
    
    return True

def find_good_arrangement():
    # Generate all possible arrangements
    arrangements = []
    for i in range(R * C):
        arrangements.append(list(range(R * C)))
    
    # Shuffle the arrangements
    import random
    random.shuffle(arrangements)
    
    # Check if any arrangement is good
    for arrangement in arrangements:
        if is_good_arrangement(arrangement):
            return arrangement
    
    # If no good arrangement is found, return impossible
    return "impossible"

def main():
    global R, C, a, b, c
    R, C = map(int, input().split())
    a, b, c = map(int, input().split())
    print(*find_good_arrangement(), sep='\n')

if __name__ == '__main__':
    main()

