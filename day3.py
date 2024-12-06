import sys
import fileinput
sys.setrecursionlimit(10000)
x=0
with fileinput.input(files=('aoc-input')) as aocInput:
  do=True
  for line in aocInput:
    # do=True
    for i in range(0,len(line)):
      if line[i:i+4]=="do()":
        print("do")
        do=True
      elif line[i:i+7]=="don't()":
        print("don't")
        do=False
      elif do and line[i:i+4]=="mul(":
        # print("mul( found")
        nums=""
        for j in range(i+4,line.find(")",i+5)+1):
          if line[j].isnumeric() or line[j]==",":
            # print("nfound")
            nums+=line[j]
          elif line[j]==")":
            # print(")found")
            try:
              a,b=list(map(int,nums.split(",")))
              if a>=1000 or b>=1000:
                break
              # print(nums, a, b)
              x+=a*b
              break
            except:
              break
          else:
            break
          
          

print(x)