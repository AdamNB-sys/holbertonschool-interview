#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Pass
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

# Pass
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

# Pass
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

# Pass
boxes = [[1], [2], [3], [4], [], [5], [7]]
print(canUnlockAll(boxes))

# Pass
boxes = [[1, 4, 5, 6], [], [], [], [3, 2], [], [], [], []]
print(canUnlockAll(boxes))

# Pass
boxes = [[1, 4, 1], [1, 4, 3], [1, 4, 6], [1, 4, 4], [1, 4, 4]]
print(canUnlockAll(boxes))

# Pass
boxes = [[1, 4, 6], [1, 2, 6], [1, 3, 6], [1, 4, 6], [1, 4, 6], [], []]
print(canUnlockAll(boxes))

# Error out index out of range
# integers within boxes are greater than the amount of boxes
# if two more boxes are present, no error occurs
boxes = [[1, 4, 6], [1, 4, 6], [1, 4, 8], [1, 4, 6], [1, 4, 6]]
print(canUnlockAll(boxes))
