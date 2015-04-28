def f(x):
        return x**2
		#replace with your function

def CalcIntegral(a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,n/2 + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,n/2):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)
    
def dTh(a, b, n):
        i=0.0
        sum=0.0
        h=(b-a)/(2.0*n)
        return 25*2.6*(h**4)
        
def dR(n):
        q=2
        zqn = CalcIntegral(0.0, 1.0, n*q)
        zn = CalcIntegral(0.0, 1.0, n)
        return (zqn-zn)/(pow(q, 4)-1.0)

def K(n):
        zqn = CalcIntegral(0.0, 1.0, n*2)
        zq2n = CalcIntegral(0.0, 1.0, n*4)
        zn = CalcIntegral(0.0, 1.0, n)
        if (zq2n-zqn) == 0:
                return 'err'
        else:
                return ((zqn - zn)/(zq2n-zqn))

print '  n         K                   dR                 dTh             dReal'
print '  1.0         -                -                 ', round(K(2), 2), '           ',round(1.0-CalcIntegral(0.0, 1.0, 2),16)

for a in range(1, 16):
        print '%5s %10s %18s %18s %18s' % (round(2**a), round(K(2**a),2),round(dR(2**a),16),round(dTh(0.0, 1.0, 2**a),16),round(1.0-CalcIntegral(0.0, 1.0, 2**(a+1)),16))
