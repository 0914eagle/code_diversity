
def get_available_mb(spent_mb, total_mb):
    return total_mb - spent_mb

def get_spent_mb(spent_mb_list, total_mb):
    spent_mb = sum(spent_mb_list)
    return spent_mb if spent_mb < total_mb else total_mb

def get_available_mb_in_next_month(spent_mb_list, total_mb):
    spent_mb = get_spent_mb(spent_mb_list, total_mb)
    return get_available_mb(spent_mb, total_mb)

def main():
    total_mb = int(input())
    num_months = int(input())
    spent_mb_list = []
    for _ in range(num_months):
        spent_mb_list.append(int(input()))
    available_mb = get_available_mb_in_next_month(spent_mb_list, total_mb)
    print(available_mb)

if __name__ == '__main__':
    main()

