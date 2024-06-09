
def get_best_friend_pairs(n):
    def is_valid_number(num):
        if num == 0:
            return False
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10
        return True

    def get_friendly_operation(num):
        operations = []
        while num > 0:
            digit1 = num % 10
            num //= 10
            digit2 = num % 10
            num //= 10
            if digit1 == digit2:
                operations.append((digit1, digit2))
            elif digit1 + 1 == digit2:
                operations.append((digit1, digit2))
            elif digit1 - 1 == digit2:
                operations.append((digit1, digit2))
            else:
                return None
        return operations

    def get_best_friend_pair(num):
        operations = get_friendly_operation(num)
        if not operations:
            return None
        num2 = num
        for operation in operations:
            num2 = num2 // 10
            num2 = num2 * 10 + operation[1]
        return num2

    def count_best_friend_pairs(n):
        count = 0
        for i in range(10 ** n):
            num = i
            while num > 0:
                num2 = get_best_friend_pair(num)
                if num2 and is_valid_number(num2):
                    count += 1
                    break
                num //= 10
        return count

    return count_best_friend_pairs(n)

if __name__ == '__main__':
    n = int(input())
    print(get_best_friend_pairs(n))

