# lp_sudoku
## Solving the New York Times daily sudoku puzzle using mixed linear-integer programming
This repo contains a simple python application that uses a webdriver to scrape
the New York Time's daily sudoku puzzle and then solves it using a linear programming
formulation.

## Formulation
The relaxed LP/IP formulation of sudoku is explained here: [https://vanderbei.princeton.edu/tex/talks/INFORMS_19/Sudoku.pdf]

There is no objective function as traditional Sudokus have a single feasible solution. The optimizer will search the
problem space and find this solution.


- $argmin -> 0$

- $x_{ijk} = 1$ if there is a number in the sudoku cell else $0$.
- each cell must contain a number at the end: $\sum_{k}{x_{ijk}}=1$ for $i = 1,...,9$ ; $j = 1,...,9$
- each row must contain each number k: $\sum_{j}{x_{ijk}}=1$ for $i = 1,...,9$ ; $k = 1,...,9$
- each column must contain each number k: $\sum_{i}{x_{ijk}}=1$ for $j = 1,...,9$ ; $k = 1,...,9$
- each nxn block in the sudoku contains each number k: $\sum_{i=3i_0-2}^{3i_0}\sum_{j=3j_0-2}^{3j_0}{x_{ijk}}=1$ for $i_0 = 1,...,3$ ; $j_0 = 1,...,3$
- each known cell must have a value with k equal to the number in the cell: $x_{i,j,k} = 1  \; \forall \:i,j,k \in known$


## Usage
The scraper and solver can be called by running `run_sudoku.py` in a terminal or by using the `example.ipynb` notebook.

Streamlit app currently under development.


## Contributions
Suggestions and referencing welcome.