
def get_leader(n, m, log_records):
    leaders = set()
    for record in log_records:
        if record[0] == "+":
            leaders.add(record[1])
        else:
            leaders.remove(record[1])
    return leaders

def main():
    n, m = map(int, input().split())
    log_records = []
    for _ in range(m):
        log_records.append(input())
    leaders = get_leader(n, m, log_records)
    print(len(leaders))
    print(*sorted(leaders), sep=" ")

if __name__ == '__main__':
    main()

