a,b,c = map(int,input().split())
result = a*b*c
for i in range(max(a,b,c),a*b*c):
  if i%a==0 and i%b==0 and i%c==0:
    result = i
    break

print(result)