
def get_starting_time(current_time, hours_to_add):
    return (current_time + hours_to_add) % 24

def main():
    current_time, hours_to_add = map(int, input().split())
    print(get_starting_time(current_time, hours_to_add))

if __name__ == '__main__':
    main()

