
def get_max_squares(n, a):
    # Initialize variables
    max_squares = 0
    current_color = 1
    remaining_liters = a

    # Iterate through the jars
    for i in range(n):
        # If there is enough paint in the current jar, paint the current square
        if remaining_liters[i] >= current_color:
            max_squares += 1
            remaining_liters[i] -= current_color
            current_color += 1

        # If the current color is greater than the number of jars, start from the first jar
        if current_color > n:
            current_color = 1

    return max_squares

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_squares(n, a))

if __name__ == '__main__':
    main()

