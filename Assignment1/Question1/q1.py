from pysat.formula import CNF
from pysat.solvers import Solver
from typing import List

def solve_sudoku(grid: List[List[int]]) -> List[List[int]]:
    """Solves a Sudoku puzzle using a SAT solver (PySAT)."""
    n = 9
    cnf = CNF()

    # Helper function to map (row, col, val) to a unique integer ID (1-based)
    def v(r, c, val):
        return r * 81 + c * 9 + val

    # 1. Each cell must contain at least one value (1-9)
    for r in range(n):
        for c in range(n):
            cnf.append([v(r, c, val) for val in range(1, n + 1)])

    # 2. Each cell must contain at most one value (pairwise negation)
    for r in range(n):
        for c in range(n):
            for v1 in range(1, n + 1):
                for v2 in range(v1 + 1, n + 1):
                    cnf.append([-v(r, c, v1), -v(r, c, v2)])

    # 3. Each row must contain every value exactly once
    for r in range(n):
        for val in range(1, n + 1):
            cnf.append([v(r, c, val) for c in range(n)])

    # 4. Each column must contain every value exactly once
    for c in range(n):
        for val in range(1, n + 1):
            cnf.append([v(r, c, val) for r in range(n)])

    # 5. Each 3x3 block must contain every value exactly once
    for br in range(0, n, 3):
        for bc in range(0, n, 3):
            for val in range(1, n + 1):
                cnf.append([v(br + r, bc + c, val) for r in range(3) for c in range(3)])

    # 6. Pre-filled values (Unit Clauses)
    for r in range(n):
        for c in range(n):
            if grid[r][c] != 0:
                cnf.append([v(r, c, grid[r][c])])

    # Solve using Glucose3 (a CDCL-based solver)
    with Solver(name='glucose3') as solver:
        solver.append_formula(cnf.clauses)
        if solver.solve():
            model = solver.get_model()
            # Convert the True literals back into the 9x9 grid
            res = [[0 for _ in range(n)] for _ in range(n)]
            for lit in model:
                if lit > 0:
                    # Reverse the mapping to get r, c, val
                    val = (lit - 1) % 9 + 1
                    c = ((lit - 1) // 9) % 9
                    r = (lit - 1) // 81
                    res[r][c] = val
            return res
        else:
            return None # UNSAT
