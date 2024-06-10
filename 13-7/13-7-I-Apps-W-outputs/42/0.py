
def get_attendee_numbers_and_heights(n):
    attendee_numbers = list(range(1, n+1))
    heights = list(map(int, input().split()))
    return attendee_numbers, heights

def get_pairs_satisfying_condition(attendee_numbers, heights):
    pairs_satisfying_condition = 0
    for i in range(len(attendee_numbers)):
        for j in range(i+1, len(attendee_numbers)):
            if abs(attendee_numbers[i] - attendee_numbers[j]) == heights[i] + heights[j]:
                pairs_satisfying_condition += 1
    return pairs_satisfying_condition

def main():
    n = int(input())
    attendee_numbers, heights = get_attendee_numbers_and_heights(n)
    pairs_satisfying_condition = get_pairs_satisfying_condition(attendee_numbers, heights)
    print(pairs_satisfying_condition)

if __name__ == '__main__':
    main()

