
def get_input():
    N = int(input())
    cheetahs = []
    for _ in range(N):
        t, v = map(int, input().split())
        cheetahs.append((t, v))
    return N, cheetahs

def solve(N, cheetahs):
    # Sort the cheetahs by their start time
    cheetahs.sort(key=lambda x: x[0])
    
    # Initialize the minimum length of the pack to infinity
    min_length = float('inf')
    
    # Iterate over the cheetahs and calculate the minimum length of the pack
    for i in range(N):
        # Calculate the time at which the cheetah will reach the finish line
        t_end = cheetahs[i][0] + cheetahs[i][1]
        
        # Calculate the length of the pack between the current cheetah and the last cheetah in the pack
        length = cheetahs[i][1] * (t_end - cheetahs[i][0])
        
        # Update the minimum length of the pack
        min_length = min(min_length, length)
    
    return min_length

def main():
    N, cheetahs = get_input()
    print(solve(N, cheetahs))

if __name__ == '__main__':
    main()

