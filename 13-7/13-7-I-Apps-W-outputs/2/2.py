
def count_showable_cows(statuses):
    # Initialize variables
    allin_count = 0
    folded_count = 0
    showable_count = 0

    # Iterate through the statuses
    for status in statuses:
        if status == "A":
            allin_count += 1
        elif status == "F":
            folded_count += 1
        elif status == "I":
            if allin_count == len(statuses) or folded_count == len(statuses):
                showable_count += 1

    return showable_count

def main():
    n = int(input())
    statuses = input()
    print(count_showable_cows(statuses))

if __name__ == '__main__':
    main()

