
def get_base_2_repr(n):
    
    if n == 0:
        return "0"
    repr_list = []
    while n != 0:
        if n % 2 == 0:
            repr_list.append("0")
        else:
            repr_list.append("1")
        n //= -2
    return "".join(reversed(repr_list))

def main():
    n = int(input())
    print(get_base_2_repr(n))

if __name__ == "__main__":
    main()

