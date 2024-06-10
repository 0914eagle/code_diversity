
def get_party_estimation(n, photographs):
    # Initialize an array to store the estimation of the parties
    party_estimation = [" "] * n

    # Iterate through the photographs
    for photograph in photographs:
        # Split the pairs into individual MPs
        mp_pairs = photograph.split()

        # Iterate through the MPs in the photograph
        for mp_pair in mp_pairs:
            # Split the MPs into their indices
            mp1, mp2 = mp_pair.split(" ")

            # Check if the MPs have the same party label
            if party_estimation[int(mp1)] == party_estimation[int(mp2)]:
                # If they have the same label, change it to the other party label
                if party_estimation[int(mp1)] == "A":
                    party_estimation[int(mp1)] = "B"
                    party_estimation[int(mp2)] = "B"
                else:
                    party_estimation[int(mp1)] = "A"
                    party_estimation[int(mp2)] = "A"
            else:
                # If they have different labels, change the label of the MP that argued with the other MP to the other party label
                if party_estimation[int(mp1)] == "A":
                    party_estimation[int(mp2)] = "B"
                else:
                    party_estimation[int(mp1)] = "A"

    return "".join(party_estimation)

def main():
    n = int(input())
    photographs = []
    for i in range(5):
        photographs.append(input())
    print(get_party_estimation(n, photographs))

if __name__ == '__main__':
    main()

