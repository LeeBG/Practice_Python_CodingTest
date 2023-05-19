
result = [[0 for j in range(11)]for i in range(11)]

count = 0
for i in range(1,11):
    if count==0:
        result[i].append(1)
        count += 1
    else:
        result[i].append(int(input().split()))
        count = 0;
    
    