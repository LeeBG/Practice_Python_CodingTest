c = ord(input())
# 유니코드로 변환
start = ord('a')
while start<=c:
  print(chr(start), end=" ")
  start+=1
