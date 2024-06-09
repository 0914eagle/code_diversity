
def count_good_phone_numbers(n, k, a, b):
    def is_good_block(block):
        if block[0] != b:
            return False
        for i in range(1, k):
            if block[i] != 0:
                return False
        return True

    def get_blocks(phone_number):
        blocks = []
        for i in range(0, n, k):
            blocks.append(phone_number[i:i+k])
        return blocks

    def get_integer_representation(blocks):
        result = 0
        for block in blocks:
            result = result * 10**k - 1 + int(block)
        return result

    def count_good_phone_numbers_helper(phone_number, a, b):
        if len(phone_number) == 0:
            return 1
        count = 0
        for i in range(0, 10):
            if i != b[0]:
                count += count_good_phone_numbers_helper(phone_number[1:], a[1:], b[1:])
        return count

    blocks = get_blocks(phone_number)
    integer_representation = get_integer_representation(blocks)
    if integer_representation % a == 0:
        return 1
    else:
        return 0

def count_good_phone_numbers(n, k, a, b):
    return count_good_phone_numbers_helper(phone_number, a, b)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(count_good_phone_numbers(n, k, a, b))

