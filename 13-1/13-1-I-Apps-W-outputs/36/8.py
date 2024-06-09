
def check_intersection(x1, x2, k_list, b_list):
    for i in range(len(k_list)):
        for j in range(i+1, len(k_list)):
            if k_list[i] != k_list[j]:
                x = (b_list[j] - b_list[i]) / (k_list[i] - k_list[j])
                if x_1 < x < x_2:
                    return True
    return False

def main():
    n = int(input())
    x_1, x_2 = map(int, input().split())
    k_list = []
    b_list = []
    for i in range(n):
        k, b = map(int, input().split())
        k_list.append(k)
        b_list.append(b)
    if check_intersection(x_1, x_2, k_list, b_list):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

