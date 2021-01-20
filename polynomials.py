'''
This file builds polynomial mathematics in binary polynomials, 
and exposes basic polynomial functions that can operate on any Galois field
The high point of this is to get to the extended euclidean algorithm for polynomials
so that we can compute the inverses that are used for sbox
The next step from this is the xbox
'''


'''
Gets the degree of the polynomial. 
'''
def degree(a):
    for index in reversed(range(len(a))):
        if a[index] == 1:
            return index
    return 0

'''
remove leading zero terms (leading terms that are zero)
'''
def removeLeadingZeros(c):
    for index in reversed(range(len(c))):
        if c[index] == 1:
            break
        else:
            del c[index]
    


'''
Checks if the polynomial is zero
'''
def zero(a):
    removeLeadingZeros(a)
    return len(a) == 0

'''
Add two polynomials represented by the coeffcient array 
'''
def add(a,b):
    removeLeadingZeros(a)
    removeLeadingZeros(b)
    diff = len(a) - len(b)
    if diff > 0 : ### a is bigger
        b.extend([0] * abs(diff))
    if diff < 0 : ### b is bigger
        a.extend([0] * abs(diff))

    result = [0] * max(len(a), len(b))
    for i in range(len(a)):
        if a[i] == b[i]:    ### Same values of coefficient means coeff goes to zero, is an xor
            result[i] = 0
        else:
            result[i] = 1
    removeLeadingZeros(result)
    return result


def subtract(a,b):
    return add(a,b)

'''
multiple one term with a specific power 
'''
def multiplyOneTerm(p,count):
    result = [0] * (len(p) + count)    
    for index in reversed(range(len(p))):
        result[index + count] = p[index]    
    return result


'''
Multiplies two polynomials together
'''
def multiply(p1,p2):
    result = []
    for index in range(len(p1)):
        if (p1[index] == 1):            
            addendum = multiplyOneTerm(p2,index)            
            result = add(result,addendum)            
    return result


''' 
    Returns the remainder polynomial coefficients given 
    divisor coefficient (c) , and the dividend (p)
    dividend = x^6 + x^4 + 1 will have the coeffs array as [0,1,0,1,0,0,0,1] 
    divisor = x^3 + x + 1 willl have coeffs array as [0,0,0,0,1,0,1,1]
    The algo is 
    a. If the divisor is zero, bail with zerodiv error
    b. Get diff of the degrees. 
        b.1 If dividend is less degree than divisor, then we cannot divide. Return the dividend as the answer
        b.2 Else multiply divisor by x^(diff degree), and subtract from the dividend. The resulting poly is the remainder
        b.3 Recursively keep diving the remainder by the divisor
    Worked example :
        x^6 + x^5 + x^4 + x^3 + x^2 + 1 when divided by x^2 + 1 gives 0 as remainder
        Degree difference is 4, multiple x^2 + 1 by x^(diffDegree), ie, x^4, to get x^6 + x^4
        Diff this with the dividend to get x^5 + x^3 + x^2 + 1 (Subtraction is xor of same-position coefficients, 
        causing the the power 6 and 4 to zero out)
        New dividend is x^5 + x^3 + x^2 + 1. degree diff with x^2 + 1 is 3, so mult x^2 + 1 with x^3 to get 
        x^5 + x^3
        Diff with dividend to get x^2 + 1
        New dividend is  x^2 + 1. degree diff with x^2 + 1 is 0, so mult x^2 + 1 with 1 and sub with dividend to 
        get 0
'''
def mod(dividend, divisor): ## The remainder polynomial must have a degree lower than the divisor
    if zero(divisor):
        raise ZeroDivisionError
    degreeDividend = degree(dividend)
    degreeDivisor = degree(divisor)
    while ((degreeDividend >= degreeDivisor) and not zero(dividend)):
        factor = [0] * (degreeDividend - degreeDivisor + 1)
        factor[len(factor) -1 ] = 1        
        result = add(dividend, multiply(divisor,factor))
        dividend = result
        degreeDividend = degree(dividend)
        degreeDivisor = degree(divisor)
    return dividend

def quotient(dividend, divisor): ## The remainder polynomial must have a degree lower than the divisor
    if zero(divisor):
        raise ZeroDivisionError
    degreeDividend = degree(dividend)
    degreeDivisor = degree(divisor)
    quotient = []
    while ((degreeDividend >= degreeDivisor) and not zero(dividend)):
        factor = [0] * (degreeDividend - degreeDivisor + 1)
        factor[len(factor) -1 ] = 1        
        result = add(dividend, multiply(divisor,factor))
        dividend = result
        degreeDividend = degree(dividend)
        degreeDivisor = degree(divisor)
        quotient = add(quotient, factor)
    return quotient

'''
Run the extended eea algorithm to get the inverse
r0 is the irreducible polynomial, r1 is the field element who inverse we are seeking
'''
def eea(r0,r1,debug):
    r = [ r0, r1 ]
    t = [ [],[1]]
    s = [ [1],[0]]
    q = [ [] ]
    index = 2
    while True:
        r.append(mod(r[index-2],r[index-1]))
        q.append(quotient(r[index-2], r[index-1]))
        t.append(subtract(t[index - 2],multiply(q[index - 1],t[index-1])))
        s.append(subtract(s[index - 2], multiply(q[index - 1],s[index-1])))
        if zero(r[index]):
            break
        index = index + 1
        if (debug):
            print(f'--------')
            print(f'r {r}')
            print(f'q {q}')
            print(f's {s}')
            print(f't {t}')
    return t[index - 1 ]

# print(eea([1,1,0,1],[0,0,1], True))