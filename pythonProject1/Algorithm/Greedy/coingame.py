def coin():
      # Greedy Algorithm
  # 그리디 알고리즘 예제 1번 (거스름돈예제)

  remains = 1260
  count = 0

  coins = [500,100,50,10]

  #Number of coins used the leaste

  for coin in coins:
    count += (remains // coin)
    remains %= coin

  print(count)
  
