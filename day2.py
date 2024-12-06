import sys
import fileinput
sys.setrecursionlimit(10000)
x=0
with fileinput.input(files=('aoc-input')) as aocInput:
  for line in aocInput:
    originalarr=list(map(int,line.split(" ")))
    for j in range(len(originalarr)):
      arr=originalarr[:j] + originalarr[j+1:]
      sorted=arr.copy()
      reversed=arr.copy()
      sorted.sort()
      reversed.sort(reverse=True)
      isSafe=True
      
      if arr==sorted:
        for i in range(0, len(arr)-1):
          if not (arr[i+1]-arr[i]<=3 and arr[i+1]-arr[i]>=1):
            isSafe=False
      elif arr==reversed:
        for i in range(0, len(arr)-1):
          if not (arr[i]-arr[i+1]<=3 and arr[i]-arr[i+1]>=1):
            isSafe=False
      else:
        isSafe=False
      if isSafe: x+=1;break

print(x)