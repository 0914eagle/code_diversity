
def get_bouquets(n, a, b):
    # Calculate the number of bouquets that can be made without the constraint
    num_bouquets = n * (n - 1) // 2
    
    # Subtract the number of bouquets that contain a or b
    num_bouquets -= (n - a + 1) * (n - b + 1) // 2
    
    return num_bouquets % (10**9 + 7)

def main():
    n, a, b = map(int, input().split())
    print(get_bouquets(n, a, b))

if __name__ == '__main__':
    main()

