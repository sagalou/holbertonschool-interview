# ⚙️ Minimum Operations

> Find the fewest number of "Copy All" and "Paste" operations needed to reach exactly n characters in a text file — a Python algorithm using prime factorization.

---

## 📖 Description & Objectives

Starting with a single character `H` in a text file, the only available operations are **Copy All** and **Paste**. This project computes the minimum number of operations required to reach exactly `n` characters.

The key insight: the answer is the **sum of prime factors** of `n`. Each prime factor `p` represents a copy + (p-1) pastes.

**Learning objectives:**
- Apply prime factorization to an optimization problem
- Implement greedy iterative algorithms
- Think in terms of mathematical reductions

---

## 🛠 Technologies Used

| Tool | Version |
|------|---------|
| Python | 3.8+ |
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
cd holbertonschool-interview/minimum_operations
```

---

## 🚀 How to Use

```python
#!/usr/bin/python3
from minimum_operations import minOperations

print(minOperations(9))   # → 6
print(minOperations(12))  # → 7
print(minOperations(1))   # → 0
```

**Output:**
```
6
7
0
```

**Why 9 → 6?** `9 = 3 × 3` → Copy+Paste+Paste (3) + Copy+Paste+Paste (3) = 6 operations.

---

## ✨ Features

- Returns `0` if `n <= 1`
- Uses prime factorization for optimal result
- O(√n) time complexity
- No external libraries

---

## 📁 Project Structure

```
minimum_operations/
├── minimum_operations.py   # Core function
└── README.md
```

---

## 👤 Author

**Sagal Haider** — [@sagalou](https://github.com/sagalou)  
Holberton School — Cybersecurity track