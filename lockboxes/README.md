# 🔓 Lockboxes

> Determine if all locked boxes can be opened using keys found inside them — a Python graph traversal algorithm.

---

## 📖 Description & Objectives

You have `n` locked boxes numbered `0` to `n-1`. Each box may contain keys to other boxes. Box `0` is unlocked by default. The challenge: determine if **all boxes can be opened**.

This is essentially a **graph reachability problem**, solved here with an iterative BFS/DFS approach using a set to track unlocked boxes.

**Learning objectives:**
- Model real-world problems as graph traversal
- Use sets for efficient membership tracking
- Implement iterative search algorithms

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
cd holbertonschool-interview/lockboxes
```

---

## 🚀 How to Use

```python
#!/usr/bin/python3
from lockboxes import canUnlockAll

boxes1 = [[1], [2], [3], []]
print(canUnlockAll(boxes1))   # → True

boxes2 = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes2))   # → False
```

**Output:**
```
True
False
```

---

## ✨ Features

- Starts from box `0` (always unlocked)
- Ignores keys that reference out-of-range boxes
- Returns `True` only if **all** boxes are reachable
- O(n + k) time complexity where k = total number of keys

---

## 📁 Project Structure

```
lockboxes/
├── lockboxes.py   # Core function
└── README.md
```

---

## 🧠 Algorithm — How it works

```
Start: box 0 is unlocked → collect its keys
While there are keys to explore:
  → Take a key, open the corresponding box
  → Add new keys found inside to the queue
  → Track all unlocked boxes in a set
Final check: unlocked boxes == total boxes
```

---

## 👤 Author

**Sagal Haider** — [@sagalou](https://github.com/sagalou)  
Holberton School — Cybersecurity track