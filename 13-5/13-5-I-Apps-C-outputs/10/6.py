
def f1(n, m, r):
    # Function to check if the candles are on the same piece of cake
    def check_candles(candles, cuts):
        pieces = []
        for candle in candles:
            piece = None
            for cut in cuts:
                if cut.intersects(candle):
                    piece = cut
                    break
            if piece is None:
                return False
            pieces.append(piece)
        return len(set(pieces)) == len(pieces)

    # Function to check if the cuts are valid
    def check_cuts(cuts, r):
        for cut in cuts:
            if cut.distance_to_origin() > r:
                return False
        return True

    # Function to check if the cuts successfully divide the cake
    def check_cake(candles, cuts, r):
        if not check_cuts(cuts, r):
            return False
        if not check_candles(candles, cuts):
            return False
        return True

    # Function to read the input
    def read_input():
        n, m, r = map(int, input().split())
        candles = []
        for i in range(n):
            x, y = map(int, input().split())
            candles.append(Candle(x, y))
        cuts = []
        for i in range(m):
            a, b, c = map(int, input().split())
            cuts.append(Cut(a, b, c))
        return n, m, r, candles, cuts

    # Function to write the output
    def write_output(result):
        if result:
            print("yes")
        else:
            print("no")

    # Main function
    n, m, r, candles, cuts = read_input()
    result = check_cake(candles, cuts, r)
    write_output(result)

class Candle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intersects(self, other):
        return self.x == other.x and self.y == other.y

class Cut:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def distance_to_origin(self):
        return abs(self.a * 0 + self.b * 0 + self.c) / math.sqrt(self.a ** 2 + self.b ** 2)

if __name__ == '__main__':
    f1()

