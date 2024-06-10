
def solve(received_string, remembered_substring):
    # find all possible numbers that can be formed with the given substring
    possible_numbers = []
    for i in range(len(remembered_substring)):
        possible_numbers.append(int(remembered_substring[:i] + "0" + remembered_substring[i:]))
    
    # find the smallest possible number that is also in the list of possible numbers
    smallest_number = float("inf")
    for number in possible_numbers:
        if number <= smallest_number and str(number) in received_string:
            smallest_number = number
    
    return smallest_number

def main():
    received_string = input()
    remembered_substring = input()
    print(solve(received_string, remembered_substring))

if __name__ == '__main__':
    main()

