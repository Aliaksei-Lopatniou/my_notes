'''
func:
    len() - O(1)
    min([...]), max([...]) - O(n)
    min(a, b), max(a, b) - O(1)
    sum() - O(n)
    pow(), **, - O(logN)
    sorted() = O(nLogN)



data:
list-
    lst[index]	O(1)

    lst[index] = value O(1)

    del lst[index] O(n)

    lst.append(value) O(1)

    lst.insert(index, value) O(n)

    lst.pop() O(1)

    lst.pop(index) O(n)

    value in lst,	for elem in lst, lst.index(value),
    lst.remove(value),  lst.count(value), lst.reverse(),
    lst.copy(),lst.clear() - O(n)

    lst.sort()	- O(n logN)


tuple-
    like the list
range-
    rng[index] O(1)

    value in rng O(1)

    for elem in rng: O(n)

    rng.index(value) O(1)

    rng.count(value) O(1)

    len(rng) O(1)

    min(rng) O(n)

    max(rng) O(n)

    sum(rng) O(n)

str-
    s.split(value),for char in s:, s.capitalize(),
    s.lower(),s.strip(value),s.isalpha() - O(n)

     s[index] - O(1)


     in ,find(), rfind(), index(), rindex(), count(), replace() - O(n)
'''

def algorithm(n):   #O(n**2)
    result = ''
    for _ in range(n):
        result += 'A'
    return result