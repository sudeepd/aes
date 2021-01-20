from polynomials import eea, zero,add
'''
In this file, we do the math required to get to the sbox
For the sbox, the first step is to have a table of multipleicative inverse of 
all elements in the field
'''

'''
Given a hex number in the galois field, we cnovert it to polynomial
Algo : mod2 gives us the lsb, and right shift brings the next higher order bit 
into position
'''
def numberToPolynomial(n):
    polynomial = [0] * 8
    number = n
    for index in range(8):
        polynomial[index] = number % 2
        number = number >> 1
    return polynomial

def polynomialToNumber(p):
    number = 0        
    for index in range(len(p)):
        number += p[index] * 1 << index
    return number
    
def inverse(p):
    if zero(p): return 0
    reducingPolynomial = [1,1,0,1,1,0,0,0,1]
    return eea(reducingPolynomial,p,False)    

'''
    Rotates elements of an array give spaces towards the higher orders (think as circular left shift)
'''
def rotRight(p,n):
    if (n == 0 ): return p
    left = p[-n:]
    right = p[:len(p) - n]
    result = left + right
    return result

'''
Dot product of 2 vectors
'''
def dotProduct(a,b):
    ###Both vectors need to be of the same dimension
    p1 = [0,0,0,0,0,0,0,0]
    p2 = [0,0,0,0,0,0,0,0]
    for i in range(len(a)): p1[i] = a[i]
    for i in range(len(b)): p2[i] = b[i]
    product = 0
    for i in range(len(p1)):
        term = 1 if p1[i] and p2[i] else 0
        product = 1 if product != term else 0        

    return product

            

'''
Computes the sbox value of a given number
'''
def sbox(n):
    basePolynomial = [1,0,0,0,1,1,1,1]    #This is the affine transform matrix's first row 
    additivePolynomial = [1,1,0,0,0,1,1,0] # This is the additive vector that gets added to the inverse multiplied matrix
    ### All subsequent rows can be constructed with a right rotations of the polynomial
    inputPolynomial = numberToPolynomial(n)
    invP = inverse(inputPolynomial)
    inversePolynomial = [0,0,0,0,0,0,0,0]
    for i in range(len(invP)): inversePolynomial[i] = invP[i]

    transformPolynomial = [0] * len(basePolynomial)
    for index in range(len(inversePolynomial)):
        transformPolynomial[index] = dotProduct(inversePolynomial,rotRight(basePolynomial, index))    
    result = add(transformPolynomial, additivePolynomial)
    return polynomialToNumber(result)



# for i in range(256):
#     print(f'{hex(i)} {hex(inverse(i))}')

