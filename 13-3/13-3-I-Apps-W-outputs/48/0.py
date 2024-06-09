
def get_increasing_sequence(b_list):
    n = len(b_list)
    a_list = [0] * n
    a_list[0] = b_list[0]
    for i in range(1, n):
        a_list[i] = a_list[i-1] ^ b_list[i]
    return a_list

def get_valid_permutation(b_list):
    n = len(b_list)
    a_list = get_increasing_sequence(b_list)
    permutation = []
    for i in range(n):
        permutation.append(b_list[a_list.index(i+1)])
    return permutation

def main():
    n = int(input())
    b_list = list(map(int, input().split()))
    permutation = get_valid_permutation(b_list)
    if permutation:
        print("Yes")
        print(" ".join(map(str, permutation)))
    else:
        print("No")

if __name__ == '__main__':
    main()

