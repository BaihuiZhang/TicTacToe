###problem 1
def los(n):
    if '' == n:
        return('')
    longest = n[0]
    current = n[0]
    for c in n[1:]:
        if current[-1] < c:
            current += c
            if len(longest) < len(current):
                longest = current
        else:
            current = c
    return(longest)
    
###problem 2
def c2f(a):
    x = a*9/5 + 32
    return x
def f2c(a):
    x = a*5/9 - 32*5/9
    return x
    
class Constraint:
    
    def __init__(self,varnames,value,total):
        self.varnames = varnames
        self.value = value
        self.total = total
    
    def __equation__(self):
        self.d = {}
        for n in range(len(self.varnames)):
            self.d[self.varnames[n]]=self.value[n]
    
    def __cal__(self):
        for n in self.d:
            self.d[n][1]*self.d[n][2]
    
    def setvar(self,var,val):
        if var in self.d:
            self.d[var].append(val)
    
    
###problem 3
import itertools 

def dot(a,b):
    dotproduct = 0
    for n in range(len(a)):
        dotproduct += a[n]*b[n]
    return dotproduct

def mindot(a,b):
    n = list(itertools.permutations(b))
    m = []
    for x in n:
        m.append(dot(a,x))
    return min(m)
    
###problem 4
import itertools

def pickitems(prices,cash):
    lowprices = []
    for n in prices:
        if n <= cash:
            lowprices.append(n)
    print
    k = []
    # for the prices >= 5, the permutations function would use too much memory
    # so i limited the n of permutations as 2.
    if len(lowprices) >= 5:
        k = itertools.permutations(lowprices,2)
    else:
        for n in range(1,int(cash/min(lowprices))+1):
            k += itertools.permutations(lowprices,n)
    d = {}    
    for n in k:
        d[n] = sum(n)
    for n in d:
        if d[n] == cash:
            return n

###problem 5
# the user/password 'database'
up = {}
up['jack'] = 'jackpw'
up['jill'] = 'jillpw'


class secure(object):
    def __init__(self,a):
        self.a = a
    def __call__(self, user, pw, *pos, **kw):
        if not user in up:
            raise Exception('User %s not registered'% user)
        if pw != up[user]:
            raise Exception('Bad password')
        else:
            return self.a(*pos,**kw)
                
@secure
def foo(a,b):
    return (a+b)

@secure
def bar(a, b=34):
    return(a+b)
