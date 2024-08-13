import numpy as np

def solution(s):
    array_s = np.array(list(map(int, s.split(" "))))
    return( str(min(array_s)) + " " + str(max(array_s)))