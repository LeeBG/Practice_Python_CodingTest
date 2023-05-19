h,w = map(int,input().split())

result = [[0 for j in range(h+1)]for i in range(w+1)]

n = int(input())

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for j in range(y,y+l):
            result[j][x]=1
    else:
        for k in range(x,x+l):
            result[y][k]=1
            
            
            
for j in range(1,h+1):
    for i in range(1,w+1):
        print(result[i][j],end=" ")
    print()
