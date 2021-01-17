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
    Uses the extened euclidean algorithm
    The logic is like this
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
def remainder(higher,lower):
    if zero(lower):
        raise ZeroDivisionError
    dHigher = degree(higher)
    dLower = degree(lower)
    if dHigher < dLower:
        return higher
    else:        
        multPoly = [0] * (dHigher - dLower + 1)
        if len(multPoly):
            multPoly[len(multPoly) -1 ] = 1        
        result = multiply(lower,multPoly)
        result = add(higher, result)
        print(f'higher {higher} lower {lower} multpoly {multPoly}, result {result}' )
        return remainder(result, lower)
        
    

    
'''
Finds the inverse polynomial given the coefficents 
of the input polynomial.
The irreducible polynomial used is x^8 + x^4 + x^3 + x + 1
The algorithm used is extended euclidean algorithm for polynomials
The input is an array of 8 ints, each 0 or 1 
The implementation is meant to demonstrate the working 
and is not meant for efficiency
Cinv(x) C(x) = 1 mod P(x)
Divide P(x) + 1 [The irreducible polynomial is added to 1 so that we can get a 
remainder of 1] 
'''
def inverse(c) :
    modulus = [0,1,0,1,1,0,0,0,1]
    result = remainder(modulus,c)
    return result
    

def testDegree():
    src = [0,0,1,0,0]
    d = degree(src)    
    # should print 2
    print(f'The degree of the polynomial is {d}')
    d = degree([0,0,0,0,0,1,0,1])    
    #should print 7
    print(f'The degree of the polynomial is {d}')

def testMultiply():
    p1 = [ 0, 0, 1, 0 ,1]
    p2 = [ 1, 1, 1,0]
    result = multiply(p1,p2)
# we are multiplying (x^2 + x^4 ) and ( 1 + x + x^2)
#Should print [0, 0, 1, 1, 0, 1, 1]
    print (result)


def testAddPolynomials():
    p1 = [ 0, 0, 1, 0, 1, 1, 0, 1,0]
    p2 = [ 1, 0, 1, 1, 1, 0, 0, 1,1]
    result = add(p2,p1)
#should print [1, 0, 0, 1, 0, 1, 0, 0,1]
    print (result)



'''   
x^6 + x^5 + x^4 + x^3 + x^2 + 1 when divided by x^2 + 1 gives x^4 +  x^3 + 1
'''
def testRemainder():
    dividend = [ 1,0,1,1,1,1,1]
    divisor = [1,0,1]
    result = remainder(dividend, divisor)
    ## reusult should be zero
    print (result)

testDegree()
testMultiply()
testAddPolynomials()
testRemainder()
