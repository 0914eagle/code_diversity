
def get_number_of_arrangements(n, colors, forbidden_colors, favorite_sequence):
    # Implement your solution here
    return 0

def main():
    n = int(input())
    colors = list(map(int, input().split()))
    forbidden_colors = set(map(int, input().split()))
    favorite_sequence = list(map(int, input().split()))
    print(get_number_of_arrangements(n, colors, forbidden_colors, favorite_sequence))

if __name__ == '__main__':
    main()

