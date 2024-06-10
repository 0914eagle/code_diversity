
def in_shuffles(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n // 2) + 1

def out_shuffles(n):
    if n % 2 == 0:
        return (n // 2) - 1
    else:
        return n // 2

if __name__ == '__main__':
    n = int(input())
    shuffle_type = input()
    if shuffle_type == "in":
        print(in_shuffles(n))
    else:
        print(out_shuffles(n))

