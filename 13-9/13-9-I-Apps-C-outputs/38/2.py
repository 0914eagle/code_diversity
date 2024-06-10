
def get_min_people(record):
    # Initialize variables
    people = set()
    current_people = set()

    # Iterate through the record
    for event in record:
        if event == "+":
            current_people.add(event)
        else:
            current_people.remove(event)
        people = people.union(current_people)

    return len(people)

def main():
    record = input()
    print(get_min_people(record))

if __name__ == '__main__':
    main()

