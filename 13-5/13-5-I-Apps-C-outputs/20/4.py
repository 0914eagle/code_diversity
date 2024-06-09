
def get_best_friend_pairs(n):
    def is_valid_number(num):
        if num < 10 ** (n - 1):
            return False
        if num % 10 == 0:
            return False
        if num % 100 == 0:
            return False
        return True
    
    def get_friendly_operations(num):
        operations = []
        while num > 0:
            if num % 10 == 9:
                operations.append(1)
            elif num % 10 == 0:
                operations.append(2)
            else:
                operations.append(0)
            num //= 10
        return operations
    
    def get_friendly_pair(num):
        operations = get_friendly_operations(num)
        new_num = 0
        for i in range(n):
            if operations[i] == 0:
                new_num += (num % 10) * 10 ** i
            elif operations[i] == 1:
                new_num += ((num % 10) + 1) * 10 ** i
            else:
                new_num += ((num % 10) - 1) * 10 ** i
        return new_num
    
    def get_best_friend_pairs_helper(num, pairs):
        if num == 0:
            return pairs
        new_num = get_friendly_pair(num)
        if is_valid_number(new_num) and new_num not in pairs:
            pairs.add(new_num)
            return get_best_friend_pairs_helper(new_num, pairs)
        return pairs
    
    return len(get_best_friend_pairs_helper(10 ** n - 1, set()))

if __name__ == '__main__':
    n = int(input())
    print(get_best_friend_pairs(n))

