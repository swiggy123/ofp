# %%
from itertools import count


with open("game_of_life.txt") as read:
    grid = [list(map(lambda y: 1 if y=="#" else 0,x.strip("\n"))) for x in read.readlines()]
    print(grid)
 # %%
def rule(grid,x:int,y:int):
    count_of_neighbours = grid[y][x]

    for x_diff in range(-1,2):
        for y_diff in range(-1,2):
            if -1 not in [y+y_diff,x+x_diff] and len(grid) != y+y_diff and len(grid[0]) != x+x_diff:
                count_of_neighbours += grid[y+y_diff][x+x_diff]

    return count_of_neighbours
# %%

    
rule = lambda grid ,y,x:sum([sum([grid[y+y_diff][x + x_diff] for x_diff in range(-1,2) if x+x_diff not in [len(grid[0]),-1]]) for y_diff in range(-1,2) if y+y_diff not in [len(grid),-1] ])- grid[y][x]
# %%

