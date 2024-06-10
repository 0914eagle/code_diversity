
def process_entries(n, entries):
    friends_numbers = {}
    for entry in entries:
        name, count, *numbers = entry.split()
        if name not in friends_numbers:
            friends_numbers[name] = set()
        for number in numbers:
            if not any(number.endswith(existing) for existing in friends_numbers[name]):
                friends_numbers[name].add(number)
    return friends_numbers

def print_output(friends_numbers):
    print(len(friends_numbers))
    for name, numbers in friends_numbers.items():
        print(name, len(numbers), *numbers)

if __name__ == "__main__":
    n = int(input())
    entries = [input() for _ in range(n)]
    friends_numbers = process_entries(n, entries)
    print_output(friends_numbers)
