
import itertools

def get_smallest_string(s, t):
    # Generate all possible strings that satisfy Condition 1
    possible_strings = ["".join(p) for p in itertools.product(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], repeat=len(t))]
    
    # Filter out strings that do not contain T as a contiguous substring
    possible_strings = [s for s in possible_strings if t in s]
    
    # Find the lexicographically smallest string that satisfies Condition 1 and Condition 2
    smallest_string = None
    for s in possible_strings:
        if smallest_string is None or s < smallest_string:
            smallest_string = s
    
    return smallest_string

def main():
    s, t = input().split()
    smallest_string = get_smallest_string(s, t)
    if smallest_string is None:
        print("UNRESTORABLE")
    else:
        print(smallest_string)

if __name__ == "__main__":
    main()

