
def process_phone_books(n, entries):
    friends_numbers = {}
    
    for entry in entries:
        name, count, *numbers = entry.split()
        numbers = set(numbers)
        if name not in friends_numbers:
            friends_numbers[name] = numbers
        else:
            for num in numbers:
                if not any(num.endswith(existing_num) for existing_num in friends_numbers[name]):
                    friends_numbers[name].add(num)
    
    return friends_numbers

def print_phone_books(friends_numbers):
    print(len(friends_numbers))
    for name, numbers in friends_numbers.items():
        print(name, len(numbers), *numbers)

if __name__ == "__main__":
    n = int(input())
    entries = [input() for _ in range(n)]
    friends_numbers = process_phone_books(n, entries)
    print_phone_books(friends_numbers)
