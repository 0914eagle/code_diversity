
def process_phone_books(n, entries):
    friends_numbers = {}
    
    for entry in entries:
        name, count, *phone_numbers = entry.split()
        if name not in friends_numbers:
            friends_numbers[name] = set()
        
        for number in phone_numbers:
            if not any(number.endswith(existing) for existing in friends_numbers[name]):
                friends_numbers[name].add(number)
    
    return friends_numbers

def print_organized_info(friends_numbers):
    print(len(friends_numbers))
    for name, numbers in friends_numbers.items():
        print(name, len(numbers), *numbers)

if __name__ == "__main__":
    n = int(input())
    entries = [input() for _ in range(n)]
    friends_numbers = process_phone_books(n, entries)
    print_organized_info(friends_numbers)
