#!/usr/bin/python3
"""determine if all boxes can be opened"""


def canUnlockAll(boxes):
    """unlock all boxes"""
    if not boxes:
        return False
    if type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True

    return False
