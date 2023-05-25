# 잘라서 배열로 저장하기

def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
      if(i+n<len(my_str)):
        answer.append(my_str[i:i+n])
      else:
        answer.append(my_str[i:])
    return answer
    
print(solution("abc1Addfggg4556b",6))
