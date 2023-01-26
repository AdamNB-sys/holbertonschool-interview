#!/usr/bin/python3
"""Method to check for keys amongst boxes"""


def canUnlockAll(boxes):
    """Return true if all boxes have keys, else return false"""
    availableKeys = [0]
    # Iterate available keys and add new keys not already found
    for x in availableKeys:
        for key in boxes[x]:
            # Add a key if it's within range of boxes,
            # and it has not already been found
            if key not in availableKeys and key < len(boxes):
                availableKeys.append(key)
    # If any numbers are missing from available keys
    # and not all boxes are open, return false
    return len(availableKeys) == len(boxes)
    '''x = 0
    while x < len(boxes):
        if x not in availableKeys:
            return False
        x += 1
    return True'''
