"""
run Sudoku scraper and solver
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from ortools.linear_solver import pywraplp
import numpy as np

from scraper.nyt_sudoku import NYTSudoku
from solver.sudoku_solver import SudokuSolver


if __name__ == '__main__':
    
    # run scraper
    sudoku_scraper = NYTSudoku()
    retreived = sudoku_scraper.nyt_pipeline()

    # run optimization
    sudoku_optimizer = SudokuSolver()
    answer = sudoku_optimizer.integer_solve(sudoku=retreived)
    print('\n')
    for i in range(9):
        print(answer[i])