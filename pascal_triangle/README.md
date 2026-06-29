# 🔺 Pascal's Triangle

> Generate Pascal's Triangle up to n rows using Python — a classic algorithm project built at Holberton School.

---

## 📖 Description & Objectives

Pascal's Triangle is a triangular array where each number is the sum of the two numbers directly above it. This project implements a Python function that returns the triangle as a list of lists, handling edge cases and building each row iteratively from the previous one.

**Learning objectives:**
- Manipulate nested lists in Python
- Implement iterative algorithms with index-based logic
- Handle edge cases (n ≤ 0)

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
cd holbertonschool-interview/pascal_triangle
```

---

## 🚀 How to Use

```python
#!/usr/bin/python3
from pascal_triangle import pascal_triangle

result = pascal_triangle(5)
for row in result:
    print(row)
```

**Output:**
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

---

## ✨ Features

- Returns `[]` if `n <= 0`
- Builds each row iteratively from the previous one
- No external libraries required
- Fully documented with docstrings (Google style)

---

## 📁 Project Structure

```
pascal_triangle/
├── pascal_triangle.py   # Core function
└── README.md
```

---

## 👤 Author

**Sagal Haider** — [@sagalou](https://github.com/sagalou)  
Holberton School — Cybersecurity track