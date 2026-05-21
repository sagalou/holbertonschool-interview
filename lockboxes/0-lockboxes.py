#!/usr/bin/python3
"""Module that determinate if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Determinate if al boxes can be opened"""
    unlocked = {0}
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key not in unlocked and new_key < len(boxes):
                unlocked.add(new_key)
                keys.append(new_key)

    return len(unlocked) == len(boxes)
