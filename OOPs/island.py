import matplotlib.pyplot as plt
import numpy as np
import time
from IPython.display import clear_output


class Solution(object):
    def __init__(self):
        self.grid = None
        self.perimeter = 0

    def plot_grid(self, current_cell=None):
        grid = np.array(self.grid)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.matshow(grid, cmap='Blues')

        if current_cell:
            i, j = current_cell
            ax.text(j, i, 'X', va='center', ha='center', color='red', fontsize=20)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ax.text(j, i, str(grid[i][j]), va='center', ha='center', color='black')

        plt.xticks([])
        plt.yticks([])
        plt.show()

    def islandPerimeter(self, grid):
        self.grid = grid
        r = len(grid)
        c = len(grid[0])
        self.perimeter = 0

        print("Initial Grid:")
        self.plot_grid()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.perimeter += 4
                    print(f"Land cell found at ({i}, {j}), adding 4, perimeter now: {self.perimeter}")
                    if i > 0 and grid[i - 1][j] == 1:
                        self.perimeter -= 2
                        print(
                            f"  Shared edge with cell above at ({i - 1}, {j}), subtracting 2, perimeter now: {self.perimeter}")
                    if j > 0 and grid[i][j - 1] == 1:
                        self.perimeter -= 2
                        print(
                            f"  Shared edge with cell to the left at ({i}, {j - 1}), subtracting 2, perimeter now: {self.perimeter}")

                    # Visualize each step
                    clear_output(wait=True)
                    self.plot_grid(current_cell=(i, j))
                    time.sleep(1)  # Pause to visualize the step

        print("Final Grid:")
        self.plot_grid()
        print(f"Total Perimeter: {self.perimeter}")
        return self.perimeter


# Example Usage
solution = Solution()
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
perimeter = solution.islandPerimeter(grid)
print(f"Total Perimeter: {perimeter}")
