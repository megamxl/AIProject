import time
from copy import deepcopy

from tqdm import tqdm

from DataClasses.Puzzle import *
from Solvers import AStar
from Heuristics import Euclidean, Hamming, Manhattan


def benchmark():
    """
    This class creates random solvable puzzles for amount x
    Each Heuristic is passed a function pointer and the grids get deepcopied because python works with reference
    :return: a dict filled with information
    """
    amount = 100
    curMeasures = []
    measures = {'Manhattan': [], 'Euclid': [], 'Hamming': []}

    print(f"solving the same {amount} random puzzles with ")

    puzzles = [Puzzle() for _ in range(amount)]

    print()
    print("Manhattan :")
    tik = time.time()
    for puzz in tqdm(puzzles):
        curMeasures.append(AStar.search(deepcopy(puzz.grid), Manhattan.Manhattan)[1])
    print(f"Manhattan : {time.time() - tik}s")
    measures['Manhattan'] = (deepcopy(curMeasures))
    curMeasures.clear()

    print()
    print("Euclidian :")
    tik = time.time()
    for puzz in tqdm(puzzles):
        curMeasures.append(AStar.search(deepcopy(puzz.grid), Euclidean.Euclidean)[1])
    print(f"Euclid : {time.time() - tik}s")
    measures['Euclid'] = (deepcopy(curMeasures))
    curMeasures.clear()

    print()
    print("Hamming : ")
    tik = time.time()
    for puzz in tqdm(puzzles):
        curMeasures.append(AStar.search(deepcopy(puzz.grid), Hamming.Hamming)[1])
    print(f"Hamming : {time.time() - tik}s")
    measures['Hamming'] = (deepcopy(curMeasures))
    curMeasures.clear()
    return measures
