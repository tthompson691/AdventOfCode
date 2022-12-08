from utils.utils import pull_input_directly
import numpy as np


# def view_check(direction):
#     score = 0
#     if direction == "left":
#         x = j-1
#         y = i
#         while forest[x, y] < forest[i, j] and x >= 0 and y >= 0:
#             score += 1
#             x -= 1


if __name__ == "__main__":
    forest = np.array([list(map(int, i)) for i in pull_input_directly(2022, 8)[:-1]])
    
    part1 = sum(
        any(
            [
                all(forest[i, :j] < forest[i, j]), 
                all(forest[i, (j+1):] < forest[i, j]),           
                all(forest[:i, j] < forest[i, j]),
                all(forest[(i+1):, j] < forest[i, j]),
            ]
        ) for i in range(forest.shape[1]) for j in range(forest.shape[0])
    )
    
    print(part1)
    maxscore = 0
    
    for i in range(1, forest.shape[1]-1):
        for j in range(1, forest.shape[0]-1):
            # check left
            try:
                left = list((list(reversed(forest[i, :j])) < forest[i, j])).index(False) + 1
            except ValueError:
                left = len(forest[i, :j])
            
            try:
                right = list((list(forest[i, (j+1):]) < forest[i, j])).index(False) + 1
            except ValueError:
                right = len(forest[i, (j+1):])
                
            try:
                up = list((list(reversed(forest[:i, j])) < forest[i, j])).index(False) + 1
            except ValueError:
                up = len(forest[:i, j])
            
            try:
                down = list((list(forest[(i+1):, j]) < forest[i, j])).index(False) + 1
            except ValueError:
                down = len(forest[(i+1):, j])
            
            score = left * right * up * down
            
            if score > maxscore:
                maxscore = score
                
                
    print(maxscore)
            
    
    