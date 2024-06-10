
def solve(n, k):
    # Find the minimum number of candies that each kid can receive
    min_candies = n // k
    # Find the maximum number of candies that each kid can receive
    max_candies = n // (k - 1) if k > 1 else 0
    # Initialize the maximum number of candies that Santa can give to kids
    max_candies_santa = 0
    # Loop through each possible number of candies that each kid can receive
    for c in range(min_candies, max_candies + 1):
        # Find the number of kids who will receive c + 1 candies
        num_kids_c_plus_1 = 0
        # Loop through each kid and count the number of kids who will receive c + 1 candies
        for i in range(k):
            if (n - i * c) >= (c + 1):
                num_kids_c_plus_1 += 1
        # If the number of kids who will receive c + 1 candies is less than or equal to the maximum number of kids who can receive c + 1 candies,
        # and the difference between the maximum and minimum number of candies is less than or equal to 1,
        # then update the maximum number of candies that Santa can give to kids
        if num_kids_c_plus_1 <= k // 2 and max_candies - min_candies <= 1:
            max_candies_santa = c
    # Return the maximum number of candies that Santa can give to kids
    return max_candies_santa

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))

if __name__ == '__main__':
    main()

