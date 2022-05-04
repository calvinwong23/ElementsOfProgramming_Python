A = [1,2,3,4,5,6,67,8,13]

print(len(A))

A.append(42)
print(A)

A.remove(2)
print(A)

A.insert(3,28)
print(A)

print(min(A))
print(max(A))
print(A.reverse())
print(reversed(A))
print(A.sort())
print(sorted(A))

del A[2]
print(A)

del A[1:3]
print(A)

#reverse list
A[::-1]
print(A)

#create copy
B = A[:]