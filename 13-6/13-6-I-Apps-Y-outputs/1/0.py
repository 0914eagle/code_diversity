
def get_diagonal_intersections(N):
    # Find the number of intersections between pairs of diagonals
    intersections = 0
    
    for i in range(N):
        for j in range(i+1, N):
            if i != j and i != j-1 and i != j+1:
                intersections += 1
    
    return intersections

def main():
    N = int(input())
    print(get_diagonal_intersections(N))

if __name__ == '__main__':
    main()

