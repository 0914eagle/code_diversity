
def max_tables(n, k, s):
    # Count the number of occupied tables
    occupied_tables = s.count("1")

    # If there are no occupied tables, then we can occupy all the tables
    if occupied_tables == 0:
        return n

    # Initialize the maximum number of tables that can be occupied
    max_tables = 0

    # Iterate over the string and check if we can occupy a table
    for i in range(n):
        # If the table is already occupied, then skip it
        if s[i] == "1":
            continue

        # If the table is free, then check if we can occupy it
        # without violating the rules of the restaurant
        if can_occupy_table(i, k, s):
            max_tables += 1

    return max_tables

def can_occupy_table(i, k, s):
    # Check if the table is within the range of the string
    if i < 0 or i >= len(s):
        return False

    # If the table is already occupied, then we cannot occupy it
    if s[i] == "1":
        return False

    # Iterate over the string and check if there is a table that is
    # closer than k to the current table
    for j in range(i-k, i+k+1):
        # If the table is within the range of the string and is occupied,
        # then we cannot occupy the current table
        if j >= 0 and j < len(s) and s[j] == "1":
            return False

    # If we reach this point, then we can occupy the table
    return True

print(max_tables(6, 1, "100010"))
print(max_tables(6, 2, "000000"))
print(max_tables(5, 1, "10101"))
print(max_tables(3, 1, "001"))
print(max_tables(2, 2, "00"))
print(max_tables(1, 1, "0"))

