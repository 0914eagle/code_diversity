
def get_broadcasting_rights(N, K, C, A):
    # Initialize variables
    media_companies = 0
    current_range = []
    current_colors = set()
    
    # Iterate through the sectors
    for i in range(N):
        # If the current sector has a different color than the previous sector,
        # and the current range is not empty,
        # and the current range is at least K sectors long,
        # and the current range has at least C distinct colors,
        # then we can sell broadcasting rights to a media company
        if A[i] != A[i-1] and current_range and len(current_range) >= K and len(current_colors) >= C:
            media_companies += 1
            current_range = []
            current_colors = set()
        
        # Add the current sector to the current range
        current_range.append(i)
        current_colors.add(A[i])
    
    # If the last range is not empty, and it is at least K sectors long, and it has at least C distinct colors,
    # then we can sell broadcasting rights to a media company
    if current_range and len(current_range) >= K and len(current_colors) >= C:
        media_companies += 1
    
    return media_companies

def main():
    N, K, C = map(int, input().split())
    A = list(map(int, input().split()))
    print(get_broadcasting_rights(N, K, C, A))

if __name__ == '__main__':
    main()

