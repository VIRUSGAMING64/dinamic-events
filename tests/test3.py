
def concat(x):
    s = ""
    for i in range(1,x+1):
        s += str(i)
    return s

def gen(x,A):
    co = 0
    c = 0
    for i in A[:x]:
        c+=1
        if i == '1':
            co += 1
            print(c,co)


n = 100000

gen(len(concat(n)),concat(n))


"""
!SOLUCION RECURSIVA:

f(1) = 1 
f(x) = 10**(log10(x)) + 10f(x/10)

eso me da (habiendo concatenado x elementos, entonces cuantos 1 hay hasta x)
x siempre potencia de 10

"""