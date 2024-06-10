
def calculate_sodas_drank(empty_bottles, found_bottles, bottles_per_soda):
    total_bottles = empty_bottles + found_bottles
    sodas_drank = total_bottles // bottles_per_soda
    return sodas_drank

def main():
    empty_bottles = int(input("Enter the number of empty soda bottles in Tim's possession at the start of the day: "))
    found_bottles = int(input("Enter the number of empty soda bottles found during the day: "))
    bottles_per_soda = int(input("Enter the number of empty bottles required to buy a new soda: "))
    print(f"Tim drank {calculate_sodas_drank(empty_bottles, found_bottles, bottles_per_soda)} sodas on his extra thirsty day.")

if __name__ == '__main__':
    main()

