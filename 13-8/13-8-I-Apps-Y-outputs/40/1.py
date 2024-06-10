
def get_k_periodic_string(s):
    k = 1
    while k * len(s) % len(s) == 0:
        if all(s[i:] == s[:len(s) - i] for i in range(k)):
            return k
        k += 1
    return 0

def main():
    s = input()
    print(get_k_periodic_string(s))

if __name__ == '__main__':
    main()

