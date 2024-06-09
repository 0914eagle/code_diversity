
def get_carryless_multiplication(num1, num2):
    result = 0
    for i in range(len(num1)):
        for j in range(len(num2)):
            result += (num1[i] * num2[j]) % 10
    return result

def get_smallest_positive_integer(num):
    for i in range(1, num+1):
        if get_carryless_multiplication(i, i) == num:
            return i
    return -1

if __name__ == '__main__':
    num = int(input())
    print(get_smallest_positive_integer(num))

