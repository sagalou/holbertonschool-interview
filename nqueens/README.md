# ♛ N Queens

> Solve the N Queens puzzle using backtracking in Python — place N non-attacking queens on an N×N chessboard.

---

## 📖 Description & Objectives

The N Queens problem is a classic combinatorics challenge: place N queens on an N×N chessboard so that no two queens threaten each other (no shared row, column, or diagonal). This project implements a recursive backtracking solution that finds and prints **all valid solutions**.

**Learning objectives:**
- Implement recursive backtracking algorithms
- Manage constraint propagation (row, column, diagonal conflicts)
- Handle command-line arguments and input validation

---

## 🛠 Technologies Used

| Tool | Version |
|------|---------|
| Python | 3.8+ |
| Module | `sys` (stdlib only) |
| Style | PEP 8 / pycodestyle |

---

## ✅ Prerequisites

- OS: Linux / macOS / Windows (WSL)
- Python 3.8 or higher
- No external dependencies

---

## ⚙️ Installation

```bash
git clone https://github.com/sagalou/holbertonschool-interview.git
cd holbertonschool-interview/nqueens
chmod +x nqueens.py
```

---

## 🚀 How to Use

```bash
./nqueens.py N
```

**Example — N=4:**
```bash
./nqueens.py 4
```

**Output:**
```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each solution is a list of `[row, column]` pairs representing queen positions.

**Example — N=6:**
```bash
./nqueens.py 6
# → 4 solutions printed
```

---

## ✨ Features

- Finds **all** solutions via recursive backtracking
- Validates input: N must be an integer ≥ 4
- Output format: `[[row, col], ...]` per solution
- No external libraries — pure Python stdlib

---

## 📁 Project Structure

```
nqueens/
├── nqueens.py   # Backtracking solver
└── README.md
```

---

## 🧠 Algorithm — How it works

```
For each column (left to right):
  Try placing a queen in each row
  → Check: no conflict with previously placed queens
      (same row, same diagonal)
  → If safe: place and recurse to next column
  → If all N columns filled: record solution
  → Backtrack and try next row
```

Time complexity: O(N!) in the worst case — pruned significantly by constraint checks.

---

## 👤 Author

**Sagal Haider** — [@sagalou](https://github.com/sagalou)  
Holberton School — Cybersecurity track