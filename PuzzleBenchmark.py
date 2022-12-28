from tqdm import tqdm
from Puzzle import *
from solvers import Manhattan, Hamming, Euclidean
from solvers import AStar

def benchmark():
    amount = 100

    print(f"solving the same {amount} random puzzles with ")

    puzzles = [Puzzle() for puzzle in range(amount)]
    print()
    print("Manhattan :")
    for puzz in tqdm(puzzles):
        AStar.search(deepcopy(puzz.grid), Manhattan)
    print()
    print("Euclidian :")
    for puzz in tqdm(puzzles):
        AStar.search(deepcopy(puzz.grid), Euclidean)
    print()
    print("Hamming : ")

    for puzz in tqdm(puzzles):
        (AStar.search(deepcopy(puzz.grid), Hamming))