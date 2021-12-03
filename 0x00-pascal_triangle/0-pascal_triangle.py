#!/usr/bin/python3
"""
founction returns a list of lists of integers repesent \
the pascal's triangle of n
"""
def pascal_triangle(n):
    """
    pascal triangle that out put with any value
    """
    x=[[]for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if (j<i):
                if(j==0):
                    x[i].append(1)
                else:
                    x[i].append(x[i-1][j]+x[i-1][j-1])
            elif(j==i):
                x[i].append(1)
    return x
