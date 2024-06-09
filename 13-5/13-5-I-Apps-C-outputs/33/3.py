
def get_side_length(n, k):
    # Find the minimum side length for each square map
    side_length = (n * 2) / k
    
    # Return the minimum side length for each square map
    return side_length

def main():
    n, k = map(int, input().split())
    print(f"{get_side_length(n, k):.2f}")

if __name__ == '__main__':
    main()

