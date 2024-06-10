
def get_available_megabytes(spent_megabytes, monthly_limit):
    return monthly_limit - spent_megabytes

def get_available_megabytes_after_N_months(spent_megabytes_list, monthly_limit, N):
    available_megabytes = monthly_limit
    for i in range(N):
        available_megabytes = get_available_megabytes(spent_megabytes_list[i], available_megabytes)
    return available_megabytes

if __name__ == '__main__':
    monthly_limit = int(input())
    N = int(input())
    spent_megabytes_list = []
    for i in range(N):
        spent_megabytes_list.append(int(input()))
    print(get_available_megabytes_after_N_months(spent_megabytes_list, monthly_limit, N))

