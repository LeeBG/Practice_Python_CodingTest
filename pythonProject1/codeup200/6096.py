a = [[0 for j in range(20)] for i in range(20)]

for i in range(1,20):
    a[i]= input().split()
    a[i].append(0)
    
for i in range(1,20):
    for j in range(18,-1,-1):
        a[i][j+1] = int(a[i][j])

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    for j in range(1,20):
        if a[j][y] == 0:
            a[j][y] = 1
        else:
            a[j][y] = 0
        if a[x][j] == 0:
            a[x][j] = 1
        else:
            a[x][j] = 0

for i in range(1,20):
    for j in range(1,20):
        print(a[i][j],end=" ")
    print()
