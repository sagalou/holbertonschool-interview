# Island Perimeter

## Description

This project implements a function that calculates the perimeter of an island described by a grid of `0`s (water) and `1`s (land).

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code follows the `PEP 8` style guide (version 1.7)
- No modules may be imported
- All modules and functions are documented
- All files are executable

## Task

### 0. Island Perimeter

**File:** `0-island_perimeter.py`
**Function:** `island_perimeter(grid)`

Given a rectangular grid of integers (`0` = water, `1` = land), returns the perimeter of the island described in `grid`.

**Assumptions:**
- Cells are connected horizontally/vertically, not diagonally
- The grid is completely surrounded by water
- There is only one island (or none)
- The island has no internal lakes

**Approach:**
Each land cell contributes 4 to the perimeter. For every pair of adjacent land cells (horizontally or vertically), 2 is subtracted from the total (1 for each cell, since that shared edge no longer touches water). The algorithm only checks the top and left neighbors of each cell while iterating top-to-bottom, left-to-right, which is enough to detect every adjacent pair exactly once without double-counting.

## Author

Sagalou