#!/bin/python
# Head ends here
def displayPathtoPrincess(n,grid):
  #print all the moves here
  for y in xrange(0, n):
    for x in xrange(0, n):
      if grid[y][x] == "p":
        yppos = y
        xppos = x
      if grid[y][x] == "m":
        ympos = y
        xmpos = x

  while ympos != yppos:
    if ympos < yppos:
      print "DOWN"
      ympos += 1
    else:
      print "UP"
      ympos -= 1

  while xmpos != xppos:
    if xmpos < xppos:
      print "RIGHT"
      xmpos += 1
    else:
      print "LEFT"
      xmpos -= 1
    
# Tail starts here
m = input()

grid = []
for i in xrange(0, m):
  grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)