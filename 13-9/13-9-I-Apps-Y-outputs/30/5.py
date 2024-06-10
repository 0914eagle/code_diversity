
import math

def is_aggressive(minute, a, b, c, d):
    # Calculate the number of aggressive minutes before the given minute
    aggressive_minutes = (minute // a) * b
    # Calculate the number of calm minutes before the given minute
    calm_minutes = (minute // c) * d
    # Return True if the minute is within the aggressive period, False otherwise
    return aggressive_minutes > calm_minutes

def solve(a, b, c, d, p, m, g):
    # Calculate the number of aggressive minutes for each dog
    aggressive_minutes_1 = math.ceil(p / a) * b
    aggressive_minutes_2 = math.ceil(m / c) * d
    # Calculate the number of aggressive minutes for both dogs
    aggressive_minutes_both = aggressive_minutes_1 + aggressive_minutes_2
    # Calculate the number of aggressive minutes for one dog
    aggressive_minutes_one = max(aggressive_minutes_1, aggressive_minutes_2)
    # Calculate the number of aggressive minutes for no dog
    aggressive_minutes_none = min(aggressive_minutes_1, aggressive_minutes_2)
    # Return the appropriate string based on the number of aggressive minutes
    if aggressive_minutes_both == g:
        return "both"
    elif aggressive_minutes_one == g:
        return "one"
    else:
        return "none"

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    print(solve(a, b, c, d, p, m, g))

if __name__ == '__main__':
    main()

