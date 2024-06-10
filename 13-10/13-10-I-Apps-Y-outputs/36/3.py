
def get_base_2_representation(N):
    if N == 0:
        return "0"
    result = ""
    while N != 0:
        if N % 2 == 0:
            result += "0"
        else:
            result += "1"
        N = N // 2
    return result[::-1]

def get_base_2_representation_from_input():
    N = int(input())
    return get_base_2_representation(N)

if __name__ == '__main__':
    print(get_base_2_representation_from_input())

