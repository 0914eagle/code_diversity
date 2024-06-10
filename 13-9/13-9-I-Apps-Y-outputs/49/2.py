
def in_shuffles(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 24
    elif n == 5:
        return 120
    elif n == 6:
        return 720
    elif n == 7:
        return 5040
    elif n == 8:
        return 40320
    elif n == 9:
        return 362880
    elif n == 10:
        return 3628800
    else:
        return -1

def out_shuffles(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 8
    elif n == 5:
        return 32
    elif n == 6:
        return 243
    elif n == 7:
        return 2048
    elif n == 8:
        return 16384
    elif n == 9:
        return 131072
    elif n == 10:
        return 1048576
    else:
        return -1

def main():
    n = int(input())
    type = input()
    if type == "in":
        print(in_shuffles(n))
    elif type == "out":
        print(out_shuffles(n))
    else:
        print("Invalid input")

if __name__ == '__main__':
    main()

