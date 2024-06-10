
def get_probability(g, k, p):
    # Initialize variables
    win_prob = 0
    draw_prob = 0
    lose_prob = 0

    # Loop through all possible combinations of g and k
    for i in range(len(g) + len(k)):
        # Get the substring of g and k with length i
        g_substring = g[:i]
        k_substring = k[:i]

        # Get the probability of g and k being a substring of s
        g_prob = get_substring_probability(g_substring, p)
        k_prob = get_substring_probability(k_substring, p)

        # Get the probability of Gon winning, drawing, or losing
        win_probability = g_prob - k_prob
        draw_probability = 2 * (g_prob * k_prob)
        lose_probability = 1 - g_prob - k_prob

        # Add the probabilities to the total probability
        win_prob += win_probability
        draw_prob += draw_probability
        lose_prob += lose_probability

    # Return the probability of Gon winning
    return win_prob

def get_substring_probability(substring, p):
    # Get the length of the substring
    length = len(substring)

    # Base case: if the substring is empty, return 1
    if length == 0:
        return 1

    # Recursive case: calculate the probability of the substring being a substring of s
    return p * get_substring_probability(substring[1:], p) + (1 - p) * get_substring_probability(substring[1:], p)

def main():
    # Read input
    g = input()
    k = input()
    p = float(input())

    # Calculate the probability of Gon winning
    probability = get_probability(g, k, p)

    # Print the result
    print(probability)

if __name__ == '__main__':
    main()

