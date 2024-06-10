
def get_megabytes_spent(plan_megabytes, months_used):
    return sum(months_used)

def get_megabytes_available(plan_megabytes, months_used):
    return plan_megabytes - get_megabytes_spent(plan_megabytes, months_used)

def get_megabytes_available_next_month(plan_megabytes, months_used):
    return get_megabytes_available(plan_megabytes, months_used) + months_used[-1]

def main():
    plan_megabytes = int(input())
    months_used = [int(input()) for _ in range(int(input()))]
    print(get_megabytes_available_next_month(plan_megabytes, months_used))

if __name__ == '__main__':
    main()

