#!/usr/bin/python3
"""Method to check for keys amongst boxes"""

# Method errors out on final test
# list ends up being out of range


def canUnlockAll(boxes):
    visited = set()
    visited.add(0)
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in visited:
                if key > len(boxes):
                    continue
                visited.add(key)
                stack.append(key)
    return len(visited) == len(boxes)
