'''
This file adds support for the shiftrows steps. The state is represented with an 
array of 16  polynomials or arrays
Each row start with 4i as the start index, and 4i + 4 as the indices of the other items
Each row is shifted left by row number places 
'''
from rot import rotLeft

### We write the algo as gneric in rows and columns
def shiftRows(state, nrows, ncols):
    result = [0] * nrows * ncols
    for i in range(len(state) // nrows):
        row = [0] * ncols
        for j in range(ncols): row[j] = state[i+4*j]            
        # print(f'row generated as {row}')
        shifted = rotLeft(row, i)
        for j in range(ncols): result[i+4*j] = shifted[j]
    return result

state = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(shiftRows(state, 4, 4))