"""
DICT
                           time        data
-----------------------------------------------------
dct[key]                  O(1)       O(1)
dct[key] = value          O(1)       O(1)
del dct[key]              O(1)       O(1)
dct.get(key)              O(1)       O(1)
dct.pop(key)              O(1)       O(1)
key in dct                O(1)       O(1)
value in dct.values()     O(n)       O(1)
for key in dct:           O(n)       O(1)
for key, value in dct.items(): O(n)  O(1)
dct.copy()                O(n)       O(n)
dct.clear()               O(n)       O(1)
dct.update(iterable)      O(k)       O(k)


SET


                                     time        data
---------------------------------------------------------------
s.add(value)                          O(1)         O(1)
s.remove(value)                       O(1)         O(1)
s.discard(value)                      O(1)         O(1)
s.pop()                               O(1)         O(1)
value in s                            O(1)         O(1)
for elem in s:                        O(n)         O(1)
s.copy()                              O(n)         O(n)
s.clear()                             O(n)         O(1)
s.update(iterable)                    O(k)         O(k)

# Операции с двумя множествами (s1, s2):
# n — размер s1, m — размер s2

s1 == s2                              O(n)         O(1)
s1 != s2                              O(n)         O(1)
s1 < s2                               O(n)         O(1)
s1 > s2                               O(m)         O(1)
s1 <= s2, s1.issubset(s2)             O(n)         O(1)
s1 >= s2, s2.issubset(s1)             O(m)         O(1)
s1 | s2, s1.union(s2)                 O(n+m)       O(n+m)
s1 & s2, s1.intersection(s2)          O(min(n,m))  O(min(n,m))
s1 - s2, s1.difference(s2)            O(n)         O(n)
s1 ^ s2, s1.symmetric_difference(s2)  O(n+m)       O(n+m)
"""
