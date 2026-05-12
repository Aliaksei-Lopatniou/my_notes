'''in order of increasing time
O(1)
O(logN)
O(n)
O(n**2)
O(n**3)
O(n**a)
O(n**a)
O(a**n)
O(n!)


'''

#examples
def algorithm(n):  #O(1) is T(5)
    return 14*n + 27

def algorithm(data):  #O(n) is T(n*7)
    total = 0
    for elem in data:
        if elem % 2 == 1:
            total = total + elem
    return total

def algorithm(n):  #O(log n)
    i = 1
    while i < n:
        i = i * 11
    return i == n