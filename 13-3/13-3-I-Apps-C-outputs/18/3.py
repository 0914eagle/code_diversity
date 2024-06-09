
def is_possible(w, s, c, k):
    # Initialize the number of each item on the bank and in the boat to 0
    bank_w, bank_s, bank_c = 0, 0, 0
    boat_w, boat_s, boat_c = 0, 0, 0

    # Loop through each item and check if it can be transferred to the boat
    while w > 0 or s > 0 or c > 0:
        # Check if the boat is full
        if boat_w + boat_s + boat_c == k:
            # If the boat is full, transfer the items from the boat to the bank
            bank_w += boat_w
            bank_s += boat_s
            bank_c += boat_c
            # Empty the boat
            boat_w, boat_s, boat_c = 0, 0, 0

        # Check if there are still items left to transfer
        if w > 0:
            # If there are still wolves left, transfer them to the boat
            boat_w += 1
            w -= 1
        if s > 0:
            # If there are still sheep left, transfer them to the boat
            boat_s += 1
            s -= 1
        if c > 0:
            # If there are still cabbages left, transfer them to the boat
            boat_c += 1
            c -= 1

    # Check if all the items have been transferred to the bank
    if bank_w == w and bank_s == s and bank_c == c:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    w, s, c, k = map(int, input().split())
    print(is_possible(w, s, c, k))

