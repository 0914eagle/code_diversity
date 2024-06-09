
def get_lawn_widths(s_widths, g_widths):
    # Initialize variables
    total_lawn_width = 0
    s_prime_widths = []

    # Iterate through each part of the street
    for i in range(len(s_widths)):
        # Calculate the new road width and lawn width
        s_prime = s_widths[i] + g_widths[i]
        g_prime = g_widths[i] - g_widths[i]

        # Add the lawn width to the total
        total_lawn_width += g_widths[i]

        # Add the new road width to the list
        s_prime_widths.append(s_prime)

    return total_lawn_width, s_prime_widths

def solve(n, s_widths, g_widths):
    # Get the lawn widths and the new road widths
    total_lawn_width, s_prime_widths = get_lawn_widths(s_widths, g_widths)

    # Check if the new road widths differ by at most 1
    for i in range(len(s_prime_widths) - 1):
        if abs(s_prime_widths[i] - s_prime_widths[i + 1]) > 1:
            return -1

    # Return the total lawn width and the new road widths
    return total_lawn_width, s_prime_widths

if __name__ == '__main__':
    n = int(input())
    s_widths = list(map(int, input().split()))
    g_widths = list(map(int, input().split()))
    total_lawn_width, s_prime_widths = solve(n, s_widths, g_widths)
    print(total_lawn_width)
    print(*s_prime_widths)

