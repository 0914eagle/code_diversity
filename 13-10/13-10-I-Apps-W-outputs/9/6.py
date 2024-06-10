
def get_all_possible_numbers(substring):
    all_possible_numbers = []
    for i in range(len(substring)):
        number = int(substring[:i+1])
        all_possible_numbers.append(number)
    return all_possible_numbers

def get_smallest_number(all_possible_numbers):
    return min(all_possible_numbers)

def main():
    substring = input()
    all_possible_numbers = get_all_possible_numbers(substring)
    smallest_number = get_smallest_number(all_possible_numbers)
    print(smallest_number)

if __name__ == '__main__':
    main()

