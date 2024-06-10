
def get_speedup(n, p, k):
    # Calculate the speedup for each segment
    speedup = [100 + i * p for i in range(n + 1)]
    
    # Calculate the total speedup
    total_speedup = sum(speedup)
    
    # Calculate the original length of the video
    original_length = k / total_speedup
    
    return original_length

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    
    original_length = get_speedup(n, p, k)
    
    print(original_length)

if __name__ == '__main__':
    main()

