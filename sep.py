import numpy as np
def custom1(x,y,frequency):
    j1, j2 = 0, len(y)-1
    j3, j4 = j1, j2
    while frequency[j1] < x-1/24 < frequency [j2] and j2 - j1 > 1:
        if frequency[(j1+j2)//2] < x-1/24:
            j1 = (j1+j2)//2
        else:
            j2 = (j1+j2)//2
    while frequency[j3] < x+1/24 < frequency [j4] and j4 - j3 > 1:
        if frequency[(j3+j4)//2] < x-1/24:
            j3 = (j3+j4)//2
        else:
            j4 = (j3+j4)//2
    return y[j2:j4]

