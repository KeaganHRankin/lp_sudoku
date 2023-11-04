"""
run Sudoku scraper and solver in a nice streamlit wrapper,
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

import streamlit as st
