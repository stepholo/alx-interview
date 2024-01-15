#!/usr/bin/python3
"""Fuction lockboxes"""


def canUnlockAll(boxes):
    """Function to find if boxes have locks"""
    # Set to keep track of visited boxes
    visited = set()

    # Stack to perform DFS
    stack = [0]

    # Mark the first box as visited
    visited.add(0)

    # DFS to explore the boxes
    while stack:
        current_box = stack.pop()

        # Check keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to an unvisited box, mark it as visite
            # and add it to the stack
            if key not in visited and key < len(boxes):
                visited.add(key)
                stack.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
