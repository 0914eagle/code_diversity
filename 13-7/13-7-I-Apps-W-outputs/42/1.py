
def read_input():
    n = int(input())
    attendee_heights = list(map(int, input().split()))
    return n, attendee_heights

def get_pairs_satisfying_condition(n, attendee_heights):
    pairs_satisfying_condition = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i - j) == attendee_heights[i] + attendee_heights[j]:
                pairs_satisfying_condition += 1
    return pairs_satisfying_condition

def main():
    n, attendee_heights = read_input()
    print(get_pairs_satisfying_condition(n, attendee_heights))

if __name__ == '__main__':
    main()

