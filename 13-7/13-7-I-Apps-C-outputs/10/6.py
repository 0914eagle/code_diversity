
def get_candy_distribution(a, b):
    # Initialize the distribution array
    distribution = [""] * len(a)

    # Sort the candy values by their absolute value in descending order
    sorted_candy = sorted(zip(a, b), key=lambda x: abs(x[0]), reverse=True)

    # Iterate through the sorted candy and assign them to Alf or Beata based on their values
    for i, (ai, bi) in enumerate(sorted_candy):
        if ai > 0:
            distribution[i] = "A"
        elif bi > 0:
            distribution[i] = "B"
        else:
            distribution[i] = "A" if ai > bi else "B"

    return "".join(distribution)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_candy_distribution(a, b))

if __name__ == '__main__':
    main()

