
def get_min_people(records):
    # Initialize variables
    people = set()
    current_person = 0

    # Iterate through the records
    for record in records:
        if record == "+":
            people.add(current_person)
            current_person += 1
        else:
            people.remove(current_person - 1)
            current_person -= 1

    # Return the minimum number of people
    return len(people)

def main():
    records = input()
    print(get_min_people(records))

if __name__ == '__main__':
    main()

