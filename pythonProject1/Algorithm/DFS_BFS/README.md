# 꼭 필요한 자료구조 기초
### '탐색'이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미한다. 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룬다. 대표적인 탐색 알고리즘으로 DFS와 BFS를 꼽을 수 있는데 이 두 알고리즘의 원리를 제대로 이해해야 코딩 테스트의 탐색유형 문제를 풀 수 있다. 그런데 DFS와 BFS를 제대로 이해하려면 기본 자료구조인 큐와 스택에 대한 이해거 잔제 되어야한다.

<br/>
<hr/>
<br/>

## 자료구조
### 자료구조란 '데이터를 표현하고 관리하고 처리하기 위한 구조'를 의미한다. 그 중 스택과 큐는 자료구조의 기초 개념으로 다음의 두 핵심적인 함수로 구성된다.

* 삽입(PUSH) : 데이터를 삽입한다.
* 삭제(POP) : 데이터를 삭제한다.

### 물론 실제로 스택과 큐를 사용할 때는 삽입과 삭제 외에도 오버플로(overflow)는 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입연산을 수행할 때 발생한다. 즉, 저장 공간을 벗어나 데이터가 넘쳐 흐를 때 발생한다. 반면에 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태이므로 언더플로(underflow)가 발생한다.

<br/>

## 스택
### 스택(Stack)은 박스 쌓기에 비유할 수 있다. 흔히 박스는 아래에서부터 위로 차곡차곡 쌓는다. 그리고 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 내려야 한다. 이러한 구조를 선입후출(FILO)구조 또는 후입선출(LIFO)라고 한다.

![스택](https://blog.kakaocdn.net/dn/dOp4c9/btqEF5n3SqX/kzA6LHzQRdBvs4LKmdD2d0/img.png)

```python
    # Python으로 표현
    stack = []
    stack.append('A')
    stack.append('B')
    stack.append('C')
    stack.pop()
    stack.append('D')

    print(stack) # 최하단 원소부터 출력 ABD
    print(stack[::-1]) # 최상단 원소부터 출력
```

<br/>

## 큐
### 큐(Queue)는 대기 줄에 비유할 수 있다. 우리가 흔히 놀이공원에서 입장하기 위한 줄을 설 때, 먼저 온 사람이 먼저 들어가게 된다. 물론 새치기는 없다고 가정한다. 나중에 온 사람일수록 나중에 들어가기 때문에 흔히 '공정한' 자료구조라고 비유된다. 이러한 구조를 선입선출(FIFO) 구조라고 한다.

![큐](https://t1.daumcdn.net/cfile/tistory/27396E3F50F61F651C)

```python
    queue.append('A')
    queue.append('B')
    queue.append('C')
    queue.append('D')
    queue.append('E')
    queue.append('F')
    queue.popleft()

    print(queue)
    queue.reverse() #다음 출력을 위해 역순으로 바꾸기
    print(queue) # 나중에 들어온 원소부터 출력하기
 
    #
```
```
    deque([3,7,1,4])
    deque([4,1,7,3])
```
### 파이썬으로 큐를 활용할 때에는 collections 모듈에서 제공하는 deque 자료구조를 활용하자. deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며,queue 라이브러리를 이용하는 것보다 더 간단하다. 더불에 대부분의 코딩테스트에서는 collections 모듈과 같은 기본 라이브러리의 사용을 허용한다.

## 재귀 함수
### DFS와 BFS를 구현하려면 재귀 함수도 이해할 수 있어야 한다. 재귀 함수는 자기 자신을 다시 호출하는 함수를  의미한다. 가장 간단한 재귀함수는 다음과 같다.

```python
    def recursice_function():
        print('재귀 함수를 호출합니다.')
        recursice_function()
    
    recursice_function()
```
### 위의 코드를 실행하면 '재귀 함수를 호출합니다' 가 무한으로 출력된다. 여기서 정의한 recursive_function()이 자기 자신을 계속해서 추가로 불러오기 때문이다. 물론 어느 정도 출력하다가 오류 메시지를 출력하고 멈출 것이다.

```
RecursionError : maximum recursion depth exceeded while picking an obejct
위의 에러는 재귀의 최대 깊이를 초과했다는 내용이다.
파이썬 인터프리터의 최대 호출횟수 제한이 있는데 이 한계를 벗어났다는 것이다.
따라서, 무한 재귀는 불가능하다.
```

