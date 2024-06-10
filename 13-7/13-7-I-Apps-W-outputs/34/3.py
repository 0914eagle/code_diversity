
def read_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def is_perfect_matching(R, B, rebels, bases):
    # Create a dictionary to map each rebel to its assigned base
    rebel_base_map = {}
    for i in range(R):
        rebel_base_map[i] = -1
    
    # Create a dictionary to map each base to its assigned rebel
    base_rebel_map = {}
    for i in range(B):
        base_rebel_map[i] = -1
    
    # Iterate through the rebels and bases and try to find a matching
    for i in range(R):
        for j in range(B):
            if rebels[i][0] != bases[j][0] and rebels[i][1] != bases[j][1]:
                if rebel_base_map[i] == -1 and base_rebel_map[j] == -1:
                    rebel_base_map[i] = j
                    base_rebel_map[j] = i
                    break
    
    # Check if all rebels have been assigned to a base
    for i in range(R):
        if rebel_base_map[i] == -1:
            return False
    
    # Check if all bases have been assigned to a rebel
    for i in range(B):
        if base_rebel_map[i] == -1:
            return False
    
    return True

def main():
    R, B, rebels, bases = read_input()
    if is_perfect_matching(R, B, rebels, bases):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

