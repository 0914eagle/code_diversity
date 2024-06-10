
def get_minimum_distinct_people(visitors):
    visitors = visitors.split("+")
    return len(set(visitors))

def main():
    visitors = input()
    print(get_minimum_distinct_people(visitors))

if __name__ == '__main__':
    main()

