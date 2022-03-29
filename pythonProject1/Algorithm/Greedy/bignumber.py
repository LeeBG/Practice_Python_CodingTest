def bigNumber():
  #큰 수의 법칙은 일반적으로 통계분야에서 다뤄짐
  #다양한 수들로 이루어진 배열이 있을 때 
  #주어진 수들을 총 M번 더하여 가장 큰 수를 만드는 것이다.
  #배열의 특정한 인덱스에 해다아하는 수가 연속해서 K번을 초과할 수 없다.
  #배열의 크기를 N,숫자가더해지는 횟수M,연속가능최대횟수K를 입력받아
  #큰수의 법칙에 따른 결과를 출력하라
  # 먼저, N,M,K를 입력받는다.
  N,M,K = map(int,input("배열의 크기 N 숫자가 더해지는 횟수M 연속초과제한 k번").split())
  # N개의 수를 입력받는다.(공백으로 구분)
  data = list(map(int,input("배열멤버 N개입력:").split()))

  if len(data) == N:
    data.sort() #입력받은 수를 정렬한다.(파이썬 정렬 알고리즘)
    first = data[N-1] #가장 큰 수
    second = data[N-2] #두번째로 큰 수
  
    result = 0 #큰수의 법치게 따른 결과를 담을 변수
    while True:
      for i in range(K):
        if M == 0 :
          break
        result += first
        M -= 1
      if M == 0:
        break
      result += second
      M -= 1
    print("큰수의법칙 : ",result)      
  else:
    print("갯 수 초과 또는 부족")


def bigNumber2():
  N,M,K = map(int,input().split())
  # N개의 수를 입력받는다.(공백으로 구분)
  data = list(map(int,input("배열멤버 N개입력:").split()))

  if len(data) == N:
    data.sort() #입력받은 수를 정렬한다.(파이썬 정렬 알고리즘)
    first = data[N-1] #가장 큰 수
    second = data[N-2] #두번째로 큰 수
    result = 0 #큰수의 법치게 따른 결과를 담을 변수
    
    count = int(M / (K+1)) * K
    print("count:",count)
    count += M % (K+1)
    print("count:",count)
    
    result += first * count #가장 큰수들의 합
    result += (M-count) * second

  print("result:",result)