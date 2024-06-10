
def organize_phone_numbers(entries):
    friends_numbers = {}
    
    for entry in entries:
        name, count, *phone_numbers = entry.split()
        phone_numbers = set(phone_numbers)
        
        if name not in friends_numbers:
            friends_numbers[name] = set()
        
        for num in phone_numbers:
            if not any(num.endswith(existing_num) for existing_num in friends_numbers[name]):
                friends_numbers[name].add(num)
    
    return friends_numbers


def print_organized_info(friends_numbers):
    print(len(friends_numbers))
    for name, numbers in friends_numbers.items():
        print(name, len(numbers), *numbers)


if __name__ == "__main__":
    n = int(input())
    entries = [input() for _ in range(n)]
    
    friends_numbers = organize_phone_numbers(entries)
    print_organized_info(friends_numbers)
