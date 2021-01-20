'''
The regular euclidean algorithm to get the gcd
'''
def quotient(x,y):
    return x//y

def mod(x,y):
    return x%y

def zero(x):
    return x == 0

def multiply(x,y):
    return x*y

def subtract(x,y):
    return x - y


'''
Run the extended eea algorithm to get the inverse of numbers
'''
def eea(r0,r1):
    r = [ r0, r1 ]
    t = [ 0,1]
    s = [ 1,0]
    q = [ 0 ]
    index = 2
    while True:
        r.append(mod(r[index-2],r[index-1]))
        q.append(quotient(r[index-2], r[index-1]))
        t.append(subtract(t[index - 2] ,multiply(q[index - 1],t[index-1])))
        s.append(subtract(s[index - 2] ,multiply(q[index - 1],s[index-1])))
        if zero(r[index]):
            break
        index = index + 1
        print(f'--------')
        print(f'r {r}')
        print(f'q {q}')
        print(f's {s}')
        print(f't {t}')
    return t[index - 1 ]


print(eea(42, 12))