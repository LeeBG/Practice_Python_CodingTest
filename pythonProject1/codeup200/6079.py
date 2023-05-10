max = int(input())
sum = 0
i = 1
while sum <= max:
  sum += i   
  if sum >= max:
    break
  i += 1

print(i)

