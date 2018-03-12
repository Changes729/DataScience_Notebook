#-----------------------------------------------------------------------
# ifs.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stdrandom
import stddraw

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Read a
# 1-by-m vector (probabilities) and two m-by-3 matrices (coefficients
# for updating x and y, respectively) from standard input. Plot the
# results as a set of n points to standard draw.

def main():
    n = int(sys.argv[1])
    dist = stdarray.readFloat1D()
    cx = stdarray.readFloat2D()
    cy = stdarray.readFloat2D()
    x = 0.0
    y = 0.0
    stddraw.setPenRadius(0.0)
    for i in range(n):
        r = stdrandom.discrete(dist)
        x0 = cx[r][0]*x + cx[r][1]*y + cx[r][2]
        y0 = cy[r][0]*x + cy[r][1]*y + cy[r][2]
        x = x0
        y = y0
        stddraw.show(1.0)
        stddraw.point(x, y)
    stddraw.show()

if __name__ == '__main__':
    main()