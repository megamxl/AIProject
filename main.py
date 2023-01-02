import PuzzleBenchmark
import numpy as np
from DataClasses.Puzzle import Puzzle
from Solvers import AStar
from Heuristics import Manhattan


def loop():
    inP = -1
    while not 0 < inP < 4:
        print(
            "Welcome to the 8 Puzzle Paradise \nYou have 2 Options Benchmarking and Solving a single Puzzle\n1) Benchmarking\n2) Solveing\n3) Exit")
        try:
            inP = int(input())
        except:
            print("Enter a numeric value between 1 an 2")
    action(inP)
    if inP != 3: loop()


def statisticDingsis(m):

    for key in m.keys():
        sumOfAll = sum(m[key])
        avg = sumOfAll / len(m[key])
        deviation = np.std(np.asarray(m[key]))
        print(f'{key}: \n#Sum: {sumOfAll:,} \n#Avg: {avg:,} \n#Standard deviation: {deviation:,}'.replace(',', '_'))



def action(inP):
    if inP == 1:
        statisticDingsis(PuzzleBenchmark.benchmark())
    elif inP == 2:
        p = Puzzle()
        print("The random selected Puzzle is")
        node = AStar.search(p.grid, Manhattan.Manhattan)
        for indx, x in enumerate(node.getPath()):
            if indx == 0:
                print("Start State")
            print("m->" + str(AStar.REVERSE.get(str(x.move))))
            print(x)


if __name__ == '__main__':
    loop()
