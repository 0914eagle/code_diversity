
def get_attendee_heights():
    return list(map(int, input().split()))

def get_number_of_pairs(attendee_heights):
    number_of_pairs = 0
    for i in range(len(attendee_heights)):
        for j in range(i+1, len(attendee_heights)):
            if abs(i-j) == sum(attendee_heights[i:j+1]):
                number_of_pairs += 1
    return number_of_pairs

def main():
    attendee_heights = get_attendee_heights()
    print(get_number_of_pairs(attendee_heights))

if __name__ == '__main__':
    main()

