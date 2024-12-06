import sys
import fileinput
sys.setrecursionlimit(10000)
x=0
grid=[]
with fileinput.input(files=('aoc-input')) as aocInput:
  for line in aocInput:
    grid.append(line.strip())

length = len(grid[0])

for i in range(0, len(grid)-2):
  for j in range(0, length-2):
    if (grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]=="MAS" or grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]=="SAM") and (grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]=="MAS" or grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]=="SAM"):
      x+=1

print(x)