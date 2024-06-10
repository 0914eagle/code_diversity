
def get_diverse_garland(n, s):
    # Initialize variables
    recolors = 0
    garland = s
    visited = [False] * n
    visited[0] = True
    
    # Iterate through the garland
    for i in range(1, n):
        # If the current lamp is not visited and the previous lamp has the same color, recolor it
        if not visited[i] and garland[i] == garland[i-1]:
            recolors += 1
            garland = garland[:i] + "R" + garland[i+1:]
            visited[i] = True
    
    return recolors, garland

def main():
    n = int(input())
    s = input()
    recolors, garland = get_diverse_garland(n, s)
    print(recolors)
    print(garland)

if __name__ == '__main__':
    main()

