
def is_pairwise_distinct(my_list):
    return len(set(my_list)) == len(my_list)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    if is_pairwise_distinct(arr):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

