
import math

def get_flaws_diameter(flaws):
    # Calculate the diameter of the largest flaw
    largest_flaw_diameter = 0
    for flaw in flaws:
        flaw_diameter = math.sqrt(sum(x**2 for x in flaw))
        if flaw_diameter > largest_flaw_diameter:
            largest_flaw_diameter = flaw_diameter

    # Return the diameter of the smallest drill bit that would remove all the flaws
    return largest_flaw_diameter * 2

def main():
    num_flaws = int(input())
    flaws = []
    for _ in range(num_flaws):
        flaw = tuple(float(x) for x in input().split())
        flaws.append(flaw)
    print(get_flaws_diameter(flaws))

if __name__ == '__main__':
    main()

