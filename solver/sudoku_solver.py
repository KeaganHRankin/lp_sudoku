"""
Object uses python optimization tools to solve a 2-D sudoku passed in
array format.
"""
# -- Imports --
#!pip install ortools #https://developers.google.com/optimization/introduction/python
from ortools.linear_solver import pywraplp
import numpy as np

class SudokuSolver:

    def __init__(self) -> None:
        pass

    def integer_solve(self, sudoku: np.ndarray, grid_dim = 9, block_dim = 3):
        """
        pass sudoku grid as (i,i) np array,
        optimize using mix int-lin programming,
        returns solved grid or exception if infeasible.
        """
        # -- Setup --
        # create solver using OR tools linear solver
        solver = pywraplp.Solver('Sudoku Solver', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
        if not solver:
            print('Solver error, exiting.')
            return

        # Defining i,j,k variable
        i_r = range(grid_dim)
        j_r = range(grid_dim)
        k_r = range(grid_dim)
        i_0 = range(0,grid_dim,block_dim)
        j_0 = range(0,grid_dim,block_dim)

        # Initialize the variables for the optimization.
        x = {}
        for i in i_r:
            for j in j_r:
                for k in k_r:
                    x[i,j,k] = solver.BoolVar(f'x{i}{j}{k}')


        # -- Constraints --
        # Constraint 1: each cell must contain a number 1 through 9
        for i in i_r:
            for j in j_r: 
                solver.Add(solver.Sum(x[i,j,k] for k in k_r) == 1)

        # Constraint 2: each row must contain a number 1 through 9
        for i in i_r:
            for k in k_r: 
                solver.Add(solver.Sum(x[i,j,k] for j in j_r) == 1)

        # Constraint 3: each column must contain a number 1 through 9
        for j in j_r:
            for k in k_r: 
                solver.Add(solver.Sum(x[i,j,k] for i in i_r) == 1)

        # Constraint 4: each nxn block must contain a number 1 through 9
        for k in k_r:
            for p in i_0:
                for q in j_0:
                    solver.Add(solver.Sum(x[p+i,j,k] for j in range(q,(q+block_dim)) for i in range(block_dim)) == 1)

        # Constraint 5/Known number init: if known numbers i,j,k must be = 1
        for i in i_r:
            for j in j_r:
                if sudoku[i,j] != 0:
                    solver.Add(x[i,j,sudoku[i,j]-1] == 1)



        # -- Solve and Return --
        # init objective function
        solver.Minimize(0)
        status = solver.Solve()

        results = np.zeros((9,9)).astype(np.int32)
        status_d = {0:'OPTIMAL', 1:'FEASIBLE', 2:'INFEASIBLE', 3:'UNBOUNDED', 
            4:'ABNORMAL', 5:'MODEL_INVALID', 6:'NOT_SOLVED'}

        # store results or except
        if status == pywraplp.Solver.OPTIMAL:
            for i in i_r:
                for j in j_r:
                    results[i,j] = sum((k + 1) * int(x[i, j, k].solution_value()) for k in k_r)
        else:
            raise Exception('Unfeasible Sudoku: {}'.format(status_d[status]))

        return results