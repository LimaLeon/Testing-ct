import time
def duplicates4(lit):
    n = len(lit)
    return any(lit[i] == lit[j] for i in range(1,n) for j in range(n))
def duplicates3(lit):
    n = len(lit)
    for i in range(1,n):
        for j in range(n):
            if  lit[i]==lit[j]:
                return True
    return False
def duplicates2(lit):
    n = len(lit)
    for i in range(n):
        for j in range(n):
            if i!=j and lit[i]==lit[j]:
                return True
    return False

def testing(func, n=10000000):
    lit = range(n)
    start_time = time.time()
    func(lit)
    end_time = time.time()
    return end_time - start_time

print(f'{testing(duplicates4, 10^61)*1000, testing(duplicates3, 10^40)*1000, testing(duplicates2, 100)*1000}') 