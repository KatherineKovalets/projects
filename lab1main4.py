#4.2
from itertools import combinations_with_replacement
A = {1, 2, 3,4}
k = 2
choose_k = list(combinations_with_replacement(A,k))
print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
A = {1, 2, 3,4}
k = 3
choose_k = list(combinations_with_replacement(A,k))
print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5}
k = 2
choose_k = list(combinations_with_replacement(A,k))
print("Комбінації довжини {} множини {}: {}".format(k,A,choose_k))
print("Кількість таких комбінацій: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5,6}
k = 2
choose_k = list(combinations_with_replacement(A,k))
print("Кількість таких комбінацій n=6,k=2: {}".format(len(choose_k)  ))
A = {1, 2, 3,4,5,6}
k = 4
choose_k = list(combinations_with_replacement(A,k))
print("Кількість таких комбінацій n=6,k=4: {}".format(len(choose_k)  ))

A = {1, 2, 3,4,5,6,7,8}
k = 4
choose_k = list(combinations_with_replacement(A,k))
print("Кількість таких комбінацій n=8,k=4: {}".format(len(choose_k)  ))

from itertools import product
A = {0,1, 2, 3,4,5,6,7,8,9}
k = 6
choose_k = list(product(A,repeat=k))
choose_k1=set()
for i in choose_k:
  if i[0]+i[1]+i[2]==i[3]+i[4]+i[5]:
    choose_k1.add(i)
#print("Такі набори: {}".format(choose_k1))
print("Кількість таких наборів(задача 4.3): {}".format(len(choose_k1)  ))
A = {0,1, 2, 3,4,5,6,7,8,9}
k = 6
choose_k = list(product(A,repeat=k))
choose_k1=set()
for i in choose_k:
  flag=True;
  if i[0]!=0:
    for j in range(1,len(i)):
      if i[j]==i[j-1]:
        flag=False
  else:
    flag=False
  if flag:
    choose_k1.add(i);

#print("Такі набори: {}".format(choose_k1))
print("Кількість таких наборів(задача 4.4): {}".format(len(choose_k1)  ))
