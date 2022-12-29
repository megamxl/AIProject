from copy import deepcopy

from tqdm import tqdm

from DataClasses.Puzzle import *
from Solvers import AStar
from Heuristics import Euclidean, Hamming, Manhattan


def benchmark():
    amount = 100

    print(f"solving the same {amount} random puzzles with ")

    puzzles = [Puzzle() for _ in range(amount)]
    print()
    print("Manhattan :")
    for puzz in tqdm(puzzles):
        AStar.search(deepcopy(puzz.grid), Manhattan.Manhattan)
    print()
    print("Euclidian :")
    for puzz in tqdm(puzzles):
        AStar.search(deepcopy(puzz.grid), Euclidean.Euclidean)
    print()
    print("Hamming : ")

    for puzz in tqdm(puzzles):
        (AStar.search(deepcopy(puzz.grid), Hamming.Hamming))
