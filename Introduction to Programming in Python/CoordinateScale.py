import stddraw

numOfLines = 100 #change the number.

stddraw.setXscale(0, numOfLines)
stddraw.setYscale(0, numOfLines)
for i in range(numOfLines + 1):
    stddraw.line(0, numOfLines - i, i, 0)
stddraw.show()