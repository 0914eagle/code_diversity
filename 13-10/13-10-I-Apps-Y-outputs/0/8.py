
def check_pairwise_distinct(my_list):
    return len(set(my_list)) == len(my_list)

def get_input():
    n = int(input())
    my_list = list(map(int, input().split()))
    return n, my_list

def main():
    n, my_list = get_input()
    if check_pairwise_distinct(my_list):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

