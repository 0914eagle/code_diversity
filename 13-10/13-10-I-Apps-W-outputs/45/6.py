
def get_tandem_kayaks(weights):
    # sort the weights in descending order
    sorted_weights = sorted(weights, reverse=True)
    # initialize the tandem kayaks with the first two weights
    tandem_kayaks = [(sorted_weights[0], sorted_weights[1])]
    # iterate through the remaining weights
    for i in range(2, len(sorted_weights)):
        # find the pair of weights that results in the minimum instability
        min_instability = float('inf')
        for j in range(i):
            instability = abs(sorted_weights[i] - sorted_weights[j])
            if instability < min_instability:
                min_instability = instability
                pair = (sorted_weights[i], sorted_weights[j])
        # add the pair to the tandem kayaks
        tandem_kayaks.append(pair)
    return tandem_kayaks

def get_single_kayaks(weights, tandem_kayaks):
    # get the weights that are not used in tandem kayaks
    single_weights = [w for w in weights if w not in tandem_kayaks]
    # sort the single weights in descending order
    sorted_single_weights = sorted(single_weights, reverse=True)
    # create a list of single kayaks with the first single weight
    single_kayaks = [sorted_single_weights[0]]
    # iterate through the remaining single weights
    for i in range(1, len(sorted_single_weights)):
        # find the weight that results in the minimum instability
        min_instability = float('inf')
        for j in range(i):
            instability = abs(sorted_single_weights[i] - sorted_single_weights[j])
            if instability < min_instability:
                min_instability = instability
                pair = (sorted_single_weights[i], sorted_single_weights[j])
        # add the pair to the single kayaks
        single_kayaks.append(pair)
    return single_kayaks

def get_total_instability(tandem_kayaks, single_kayaks):
    # calculate the total instability of the tandem kayaks
    total_instability = sum([abs(w1 - w2) for (w1, w2) in tandem_kayaks])
    # calculate the total instability of the single kayaks
    total_instability += sum([abs(w1 - w2) for (w1, w2) in single_kayaks])
    return total_instability

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    assert len(weights) == 2 * n
    tandem_kayaks = get_tandem_kayaks(weights)
    single_kayaks = get_single_kayaks(weights, tandem_kayaks)
    total_instability = get_total_instability(tandem_kayaks, single_kayaks)
    print(total_instability)

if __name__ == '__main__':
    main()

