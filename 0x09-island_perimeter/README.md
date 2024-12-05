#Project: 0x09. Island Perimeter

This project focuses on determining the perimeter of an "island" within a grid. The "island" is represented by 1s (land) in a 2D grid of 0s (water). The task involves understanding and implementing an algorithm to compute the perimeter efficiently.
---

#Overview

The problem requires analyzing a grid where:

0 represents water.

1 represents land.

The grid is fully surrounded by water.

Each cell is square and connects either to another square horizontally or vertically.

The goal is to calculate the total perimeter of the island(s) formed by 1s. The perimeter is computed based on the number of edges of the land cells that are adjacent to water or at the boundary of the grid.

---

#Learning Objectives

Understand grid-based traversal and neighbor checking.

Analyze edge cases like:

Islands with lakes.

Islands at the boundary of the grid.

No islands present.

Optimize algorithms for computational efficiency.
---

##Tasks
File

0. Island Perimeter

0-island_perimeter.py

Task 0: Island Perimeter

#Description:
Write a function def island_perimeter(grid): that calculates the perimeter of the island described in the grid.
---

##Requirements:

The grid is rectangular, with dimensions not exceeding 100x100.

The grid is surrounded by water, and there is only one island (or none).

The function must run efficiently in terms of time complexity.

##Example:

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 16
---

#Development Notes
Algorithm:

Iterate through the grid.

For each cell that is 1:

Add 4 to the perimeter.

Subtract 2 for each adjacent land cell (to avoid double counting shared edges).

Edge Cases:

Grid with no 1s.

Large grids with complex shapes.

Minimal islands (e.g., single-cell islands).

