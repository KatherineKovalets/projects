#1.3
from itertools import permutations
A = {1, 3, 5}
permute_all = set(permutations(A))
print("задача 1.3"))
print("Перестановки множини {}: {}".format(A,permute_all))
print("Кількість перестановок: ", len(permute_all))
A = {1, 2, 3, 4}
permute_all = set(permutations(A))
print("Перестановки множини {}: {}".format(A,permute_all))
print("Кількість перестановок: ", len(permute_all))
A = {1, 2, 2, 1}
permute_all = set(permutations(A))
print("Перестановки множини {}: {}".format(A,permute_all))
print("Кількість перестановок: ", len(permute_all))
A = [1, 2, 2, 1]
permute_all = set(permutations(A))
print("Перестановки множини {}: {}".format(A,permute_all))
print("Кількість перестановок: ", len(permute_all))
#1.4
A = [1, 2, 3]
permute_all= permutations(A)
permute_all1=set()

for i in permute_all:
  count=0
  for j in range(len(i)):
    if A[j]!=i[j]:
      count+=1
    if count==len(i):
     permute_all1.add(i)


print("Перестановки множини без нерухомих точок  (задача 1.4) {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))

#1.4
A = [1, 2, 3, 4]
permute_all= permutations(A)
permute_all1=set()
for i in permute_all:
  count=0
  for j in range(len(i)):
    if A[j]!=i[j]:
      count+=1
    if count==len(i):
     permute_all1.add(i)
print("Перестановки множини без нерухомих точок  (задача 1.4) {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))

A = [1, 3, 5, 7]
permute_all= permutations(A)
permute_all1=set()
for i in permute_all:
  count=0
  for j in range(len(i)):
    if A[j]!=i[j]:
      count+=1
    if count==len(i):
     permute_all1.add(i)
print("Перестановки множини без нерухомих точок (задача 1.4)  {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))
A = [1, 2, 2, 1]
permute_all= permutations(A)
permute_all1=set()
for i in permute_all:
  count=0
  for j in range(len(i)):
    if A[j]!=i[j]:
      count+=1
    if count==len(i):
     permute_all1.add(i)
print("Перестановки множини без нерухомих точок (задача 1.4) {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))
A = [1, 2, 3, 4, 5, 6, 7, 8]
permute_all= permutations(A)
permute_all1=set()
for i in permute_all:
  flag=True
  for j in range(len(i)):
    if j<3:
      if i[j]>i[j+1]:
        flag=False
        break
    else: 
      if j>3:
        if i[j]>i[j-1]:
          flag=False
          break
  if flag:
    permute_all1.add(i)
print("Перестановки задачі 1.5  {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
permute_all= permutations(A)
permute_all1=set()
for i in permute_all:
  flag=True
  for j in range(len(i)):
    if j<3:
      if i[j]>i[j+1]:
        flag=False
        break
    else: 
      if j>3:
        if i[j]>i[j-1]:
          flag=False
          break
  if flag:
    permute_all1.add(i)
print("Перестановки задачі 1.5 {}: {}".format(A,permute_all1))
print("Кількість перестановок: ", len(permute_all1))