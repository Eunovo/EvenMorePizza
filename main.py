import argparse
import os
from pathlib import Path
from Problem import Problem
from ga.Solver import GASolver


def main():
    parser = argparse.ArgumentParser(
        description='Solve the Even More Pizza Challenge.')
    parser.add_argument(
        'input_dir', metavar='input_dir',
        type=str, nargs=1, help='input dir')
    args = parser.parse_args()
    
    input_dir = args.input_dir[0]

    files = os.listdir(input_dir)
    for file in files:
        problem = Problem.from_file(Path(input_dir, file))
        solver = GASolver(problem)
        solver.run()

if __name__ == '__main__':
    main()
