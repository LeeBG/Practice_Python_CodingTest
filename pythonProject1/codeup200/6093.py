a = int(input())
b = input().split()

for i in range(len(b)):
  b[i] = int(b[i])
  
b.reverse()

for i in range(len(b)):
  print(b[i], end=" ")
