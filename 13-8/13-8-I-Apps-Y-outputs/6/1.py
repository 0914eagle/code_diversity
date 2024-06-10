
def construct_binary_string(a, b, x):
    # Initialize the string with a and b zeroes and ones
    s = "".join(["0" for _ in range(a)] + ["1" for _ in range(b)])
    # Find the indices where the characters are not equal to the next character
    indices = [i for i in range(1, len(s)) if s[i] != s[i - 1]]
    # If there are more indices than x, return an empty string
    if len(indices) > x:
        return ""
    # If there are less indices than x, add additional indices
    for i in range(len(indices), x):
        indices.append(i)
    # Shuffle the indices to ensure a random binary string
    import random
    random.shuffle(indices)
    # Replace the characters at the indices with the opposite character
    for i in indices:
        if s[i] == "0":
            s = s[:i] + "1" + s[i + 1:]
        else:
            s = s[:i] + "0" + s[i + 1:]
    return s

def main():
    a, b, x = map(int, input().split())
    s = construct_binary_string(a, b, x)
    print(s)

if __name__ == '__main__':
    main()

