#3.2
from itertools import combinations
A = {1, 2, 3,4}
k = 2
choose_k = list(combinations(A,k))

print("задача 3.2")
print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
A = {1, 2, 3,4}
k = 3
choose_k = list(combinations(A,k))
print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5}
k = 2
choose_k = list(combinations(A,k))
print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5,6}
k = 2
choose_k = list(combinations(A,k))
print("Кількість комбінацій n=6 k=2: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5,6}
k = 4
choose_k = list(combinations(A,k))
print("Кількість комбінацій n=6 k=4: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5,6,7,8}
k = 4
choose_k = list(combinations(A,k))
print("Кількість комбінацій n=8 k=4: {}".format(len(choose_k)  ))
#3.3

A = {1, 2, 3,4,5,6,7,8,9,10}
k = 2
choose_k = list(combinations(A,k))
print("Кількість сум(задача 3.3): {}".format(len(choose_k)  ))
