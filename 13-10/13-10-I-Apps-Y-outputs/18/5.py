
def get_target_score(n):
    if n % 3 == 0 and n // 3 in range(1, 21):
        return "triple " + str(n // 3)
    elif n % 2 == 0 and n // 2 in range(1, 21):
        return "double " + str(n // 2)
    elif n in range(1, 21):
        return "single " + str(n)
    else:
        return "impossible"

def main():
    n = int(input())
    print(get_target_score(n))

if __name__ == '__main__':
    main()

