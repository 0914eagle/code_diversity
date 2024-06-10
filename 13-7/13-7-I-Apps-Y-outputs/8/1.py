
def get_original_length(n, p, k, timestamps):
    
    original_length = k
    for i in range(n):
        original_length -= (timestamps[i] * (100 + (i * p)) / 100)
    return original_length

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    print(get_original_length(n, p, k, timestamps))

if __name__ == '__main__':
    main()

