
def get_best_friend_pairs(n):
    def is_valid_number(num):
        if len(str(num)) != n:
            return False
        if num < 10 ** (n - 1):
            return False
        if num >= 10 ** n:
            return False
        return True

    def get_friendly_operations(num):
        operations = []
        for i in range(n - 1):
            digit1 = num // (10 ** i) % 10
            digit2 = num // (10 ** (i + 1)) % 10
            if digit1 == 0 or digit2 == 0:
                continue
            if digit1 == 1 and digit2 == 9:
                continue
            if digit1 == 9 and digit2 == 1:
                continue
            operations.append((digit1, digit2))
        return operations

    def get_best_friend_pair(num):
        operations = get_friendly_operations(num)
        for operation in operations:
            digit1, digit2 = operation
            if digit1 + digit2 == 10:
                return num * 10 + digit1 - 1, num * 10 + digit2 - 1
            if digit1 - digit2 == 1:
                return num * 10 + digit1 + 1, num * 10 + digit2 + 1
        return None, None

    def get_all_best_friend_pairs(num):
        pairs = []
        for i in range(10 ** (n - 1), 10 ** n):
            pair = get_best_friend_pair(i)
            if pair[0] is not None and pair[1] is not None:
                pairs.append(pair)
        return pairs

    pairs = get_all_best_friend_pairs(10 ** (n - 1))
    return len(pairs)

if __name__ == '__main__':
    n = int(input())
    print(get_best_friend_pairs(n))

