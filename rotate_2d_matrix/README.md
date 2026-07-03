# Holberton School - Interview Preparation

This repository contains solutions to technical interview practice projects, covering common algorithmic challenges in Python.

## Projects

### rotate_2d_matrix

Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise, in-place.

**File:** `0-rotate_2d_matrix.py`

**Approach:**
The matrix is rotated in two steps:
1. **Transpose** the matrix (swap `matrix[i][j]` with `matrix[j][i]` for all `j > i`).
2. **Reverse** each row of the transposed matrix.

**Example:**
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Author

Sagalou