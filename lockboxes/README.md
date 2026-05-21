# Lockboxes

## Description
This project contains a method to determine if all locked boxes can be opened.

## Requirements
- Python 3.4.3
- Ubuntu 14.04 LTS

## File
| File | Description |
|------|-------------|
| `0-lockboxes.py` | Method `canUnlockAll(boxes)` |

## Usage
```bash
./main_0.py
```

## Algorithm
Uses a set to track unlocked boxes and a list of keys to explore.
Starting from box 0, it collects all reachable keys until no new boxes can be opened.