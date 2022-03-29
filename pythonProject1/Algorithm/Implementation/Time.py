'''
시각
정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함 되는
모든 경우의 수를 구하는 프로그램을 작성하시오 예를 들어, 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다.

'''

three_count = 0 #이 들어가는 시각의 횟수
hours = 0
while True:
    hours = int(input("0에서 24미만의 수를 입력하시오"))
    if hours < 0 or hours >= 24:
        print("정수를 다시 입력하세요")
    else:
        break

for i in range(hours+1):    # 00시 00분 00초 부터 시작 ~ N시 59분 59초 까지
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                three_count+=1

print(three_count)