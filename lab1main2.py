print("задача 2.2")
from itertools import permutations
A = {1, 2, 3,4}
k = 2
permute_k = list(permutations(A, k))
print("Перестановки довжини {} множини {}: {}".format(k,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)))

A = {1, 2, 3,4}
k = 3
permute_k = list(permutations(A, k))
print("Перестановки довжини {} множини {}: {}".format(k,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)))

A = {1, 2, 3,4,5}
k = 2
permute_k = list(permutations(A, k))
print("Перестановки довжини {} множини {}: {}".format(k,A,permute_k))
print("Кількість таких перестановок: {}".format(len(permute_k)))
A = {1, 2, 3,4,5,6}
k = 2
permute_k = list(permutations(A, k))
print("Кількість перестановок n=6 k=2: {}".format(len(permute_k)))
A = {1, 2, 3,4,5,6}
k = 4
permute_k = list(permutations(A, k))
print("Кількість перестановок n=6 k=4: {}".format(len(permute_k)))

A = {1, 2, 3,4,5,6,7,8}
k = 4
permute_k = list(permutations(A, k))
print("Кількість перестановок n=8 k=4: {}".format(len(permute_k)))