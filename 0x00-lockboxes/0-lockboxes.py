#!/usr/bin/python3
def canUnlockAll(boxes):
    visited = set()
    visited.add(0)
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in visited:  # or if visited
                visited.add(key)
                stack.append(key)
    return len(visited) == len(boxes)
