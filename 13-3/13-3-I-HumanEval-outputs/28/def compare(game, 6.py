
from typing import List

def compare(game: List[int], guess: List[int]) -> List[int]:
    
    return [abs(guess[i] - game[i]) for i in range(len(game))]

