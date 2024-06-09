
def get_d(e, e_success, e_failure):
    # Initialize variables
    d = 0
    s = 0
    w = 25
    while e > 0:
        # Try to lift the weight
        if s >= w:
            # Successful lift
            e -= e_success
            s -= w
            d = max(d, w)
        else:
            # Failed lift
            e -= e_failure
        # Increase weight by 25 kg
        w += 25
    return d

def main():
    e, e_success, e_failure = map(int, input().split())
    d = get_d(e, e_success, e_failure)
    print(d)

if __name__ == '__main__':
    main()

