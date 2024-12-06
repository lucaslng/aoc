import fileinput
from functools import cmp_to_key

x=0
isPages = False
rules={}
pages=[]
with fileinput.input(files=('aoc-input')) as aocInput:
  for line in aocInput:
    line=line.strip()
    if line=="":
      isPages=True
      continue
    if isPages:
      pages.append(list(map(int,line.split(","))))
    else:
      line = list(map(int,line.split("|")))
      if line[0] in rules:
        print(rules, line[0])
        rules[line[0]].add(line[1])
      else:
        rules[line[0]] = {line[1]}

@cmp_to_key
def cmp_items(a, b):
  if a in rules:
    for rule in rules[a]:
      if rule == b:
        return -1
  elif b in rules:
    for rule in rules[b]:
      if rule == a:
        return 1
  return 0

for updates in pages:
  s = sorted(updates,key=cmp_items)
  if s != updates:
    l=len(s)//2
    x+=int(s[l])

print(x)