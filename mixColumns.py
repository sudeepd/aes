from rot import rotRight
from polynomials import multiply, degree, mod,add

'''
v1 and v2 are both plynomials
'''
def vectorMultiply( v):
    outputVector = [0] * len(v)
    mixVector = [ [0,1], [1,1],[1,0],[1,0]]  
    result = [0] * len(v)
    for index in range(len(v)): 
        mutiplier = rotRight(mixVector,index)
        reducingPolynomial = [1,1,0,1,1,0,0,0,1]
        s = []
        for i in range(len(v)):
            s = add(s,multiply(v[i],mutiplier[i]))
        if (degree(s) >= degree(reducingPolynomial)):
            s = mod(s, reducingPolynomial)
        outputVector[index] = s
    return outputVector

'''
This file adds suport for the mix columsn steps
In mix columns, the row array is simply a row of GF polynomials
And each subsequent row is a left shift by row number of positions

The literature (Par and Pelzl) provide the mix columns multiplicative array as
    02 03 01 01
    01 02 03 01
    01 01 02 03
    03 01 01 02

Only the first row is relevant here, the other ones can be obtained by right rotating the row 
'''
def mixColumns(state, nrows, ncols):
    result = [0] * nrows * ncols
    for i in range (ncols):
        vector = state[ i*nrows:i*nrows+4]
        newColumn = vectorMultiply(vector)
        print (f'newColumn {newColumn}')
        for j in range (ncols):
            result[i * nrows + j] = newColumn[j] 
    return result


def testMixColumns():
    input = [
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1]
    ]
    print(mixColumns(input, 4, 4))

# testMixColumns()