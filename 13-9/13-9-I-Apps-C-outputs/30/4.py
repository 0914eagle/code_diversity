
def check_paradox(h, m, s, t1, t2):
    # Calculate the total seconds from h, m, s
    total_seconds = h * 3600 + m * 60 + s
    
    # Calculate the total seconds from t1 and t2
    total_seconds_t1 = t1 * 3600
    total_seconds_t2 = t2 * 3600
    
    # Check if the difference between the total seconds is a multiple of 3600
    if (total_seconds_t2 - total_seconds_t1) % 3600 == 0:
        return "YES"
    else:
        return "NO"

def main():
    h, m, s, t1, t2 = map(int, input().split())
    print(check_paradox(h, m, s, t1, t2))

if __name__ == '__main__':
    main()

