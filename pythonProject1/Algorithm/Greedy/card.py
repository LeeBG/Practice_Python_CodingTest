from unittest import result


def cardgame():
  """숫자가 쓰인 카드 N x M의 형태로 놓여있따. 이때 N은 행의 갯수 M은 열의 갯수
  먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
  그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
  따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해다 행에서 가장 숫자가 낮은 
  카드를 뽑을 것을 고려해서 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 
  전략을 세워야 한다."""

  n,m = map(int,input().split())
  result = 0
  #카드 입력받기
  for i in range(n):
    data = list(map(int,input().split()[:m]))
    min_value=min(data)
    result = max(result,min_value)
  
  print("result : ",result)

cardgame()