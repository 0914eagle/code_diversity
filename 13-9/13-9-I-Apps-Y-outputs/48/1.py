
def min_snacks(A, B):
    # Calculate the minimum number of snacks needed for A guests
    min_A = A
    while min_A % B != 0:
        min_A += 1

    # Calculate the minimum number of snacks needed for B guests
    min_B = B
    while min_B % A != 0:
        min_B += 1

    # Return the minimum of the two calculations
    return min(min_A, min_B)

def main():
    A, B = map(int, input().split())
    print(min_snacks(A, B))

if __name__ == '__main__':
    main()

