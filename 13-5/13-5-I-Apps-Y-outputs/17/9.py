
def get_min_mp(l_list, a, b, c):
    # Sort the list of lengths in non-decreasing order
    l_list.sort()
    # Initialize the minimum magic points needed to achieve the objective
    min_mp = 0
    # Initialize the current length of the bamboos
    curr_len = 0
    # Loop through the list of lengths
    for l in l_list:
        # If the current length is less than the length of the first bamboo, use extension magic
        if curr_len < a:
            min_mp += 1
            curr_len += 1
        # If the current length is less than the length of the second bamboo, use extension magic
        elif curr_len < b:
            min_mp += 1
            curr_len += 1
        # If the current length is less than the length of the third bamboo, use extension magic
        elif curr_len < c:
            min_mp += 1
            curr_len += 1
        # If the current length is equal to the length of the first bamboo, use composition magic
        elif curr_len == a:
            min_mp += 10
            curr_len += l
        # If the current length is equal to the length of the second bamboo, use composition magic
        elif curr_len == b:
            min_mp += 10
            curr_len += l
        # If the current length is equal to the length of the third bamboo, use composition magic
        elif curr_len == c:
            min_mp += 10
            curr_len += l
        # If the current length is greater than the length of the first bamboo, use shortening magic
        elif curr_len > a:
            min_mp += 1
            curr_len -= 1
        # If the current length is greater than the length of the second bamboo, use shortening magic
        elif curr_len > b:
            min_mp += 1
            curr_len -= 1
        # If the current length is greater than the length of the third bamboo, use shortening magic
        elif curr_len > c:
            min_mp += 1
            curr_len -= 1
    return min_mp

def main():
    n, a, b, c = map(int, input().split())
    l_list = list(map(int, input().split()))
    print(get_min_mp(l_list, a, b, c))

if __name__ == '__main__':
    main()

