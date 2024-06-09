
def get_best_friend_pairs(n):
    def is_valid_number(num):
        if num == 0:
            return False
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10
        return True

    def get_friendly_operations(num):
        operations = []
        while num > 0:
            digit1 = num % 10
            num //= 10
            digit2 = num % 10
            num //= 10
            if digit1 == 0 or digit2 == 0:
                break
            if digit1 == 1 or digit2 == 9:
                break
            if digit1 == digit2:
                break
            operations.append((digit1, digit2))
        return operations

    def get_friendly_numbers(num):
        numbers = set()
        operations = get_friendly_operations(num)
        for operation in operations:
            digit1, digit2 = operation
            if digit1 == 1:
                numbers.add(num - 10**(n-1))
            else:
                numbers.add(num + 10**(n-1))
            if digit2 == 9:
                numbers.add(num + 10**(n-1))
            else:
                numbers.add(num - 10**(n-1))
        return numbers

    def get_best_friend_pairs_helper(num, pairs):
        if num == 0:
            return pairs
        friendly_numbers = get_friendly_numbers(num)
        for friendly_number in friendly_numbers:
            if friendly_number not in pairs:
                pairs.add((num, friendly_number))
                pairs = get_best_friend_pairs_helper(friendly_number, pairs)
        return pairs

    pairs = set()
    for i in range(10**n):
        if is_valid_number(i):
            pairs = get_best_friend_pairs_helper(i, pairs)
    return len(pairs)

if __name__ == '__main__':
    n = int(input())
    print(get_best_friend_pairs(n))

