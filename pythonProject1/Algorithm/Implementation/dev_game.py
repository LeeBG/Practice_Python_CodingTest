''' 
게임 개발

게임 캐릭터가 어떤 맵 안에서 움직이는 시스템을 개발중이다. 
- 캐릭터가 있는 장소는 1x1 정사각형으로 이뤄진 N x M 크기의 직사각형
- 각각의 칸은 육지 또는 바다이다. 
- 캐릭터는 동서남북중 한 곳을 바라본다. 
- 맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 갯수, 
  B는 서쪽으로부터 떨어진 칸의 갯수이다. 캐릭터는 상하좌우로 움직일 수 있고, 
  바다로 되어 있는 공간에는 갈 수 없다.
  캐릭터의 움직임을 설정하기 위해 정해놓은 메뉴얼은 이러하다.
  1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반 시계방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
  2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진
  3. 왼쪽 방향으로 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 하고 1단계로 돌아간다.
  4. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는 바라보는 방향을 유지한 채로 한칸 뒤로가고 1단계로 돌아감
     이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.  

    ☆현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트를 하려한다, 메뉴얼에 따라
    캐릭터를 이동시킨 뒤에, 캐릭터가 "방문한 칸의 수를 출력하는 프로그램"을 만드시오☆
'''

#  3 <= N,M <= 50
'''
- 0 : 북
- 1 : 동
- 2 : 남
- 3 : 서
'''

n,m = map(int,input("N,M : ").split())
# 방문한 위치를 저장하기 위한 맵을 초기화
d = [[0] * m for _ in range(n)]
# 현재 플레이어의 위치와 방향(0,1,2,3) 입력
x, y, direction = map(int,input("player x, y, direction : ").split())
d[x][y] = 1 # 현재 플레이어의 위치는 시작과 동시에 방문처리
print("d[",x,"][",y,"] :",d[x][y])
# 전체 맵 정보 지정
array = []
for i in range(n):
    array.append(list(map(int,input(str(i)+": ").split()))) # m개


#방향이동 정의 (북 동 남 서)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전(90도)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

result = 1 # 시작 방문했기 때문에 
turn_time = 0 #4가 되면 모든 방향을 방문한 상태가 된다.


while True:
    #왼쪽으로 회전
    print("d[",x,"][",y,"] :",d[x][y])
    turn_left()# direction변경
    nx = x + dx[direction]
    ny = y + dy[direction]
    print("nx "+str(nx))
    print("ny "+str(ny))
    # 회전이동 이후 정면에 가보지 않은 칸이 존재하는 경우 and 바다가 아닌 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        result +=1
        turn_time =0
        continue
    else: # 이미 가본 적이 있거나 바다인 경우
        turn_time += 1
    # 네 방향 모두 가본 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로갈 수 있는 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    
#print
print(result)