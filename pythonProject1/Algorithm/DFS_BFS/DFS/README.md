# DFS
### DFS는 Depth-First Search, 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. DFS를 설명하기 전에 먼저 그래프(Graph)의 기본 구조를 알아야 한다. 그래프는 노드(Node)와 간선(Edge)으로 표현되며 이 때 노드를 정점(Vertex)이라고도 말한다. 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다. 또한 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다'라고 표현한다.

<br/>

### 일반적으로 그래프를 표현하는데 사용하는 단어들이다. 노드를 도시, 간선을 도로라고 비유해보자 A라는 도시(노드)에서 B라는 도시(노드)로 이동하기 위해서 A와B를 연결하는 도로(간선)를 거친다고 생각하면 이해하기 쉽다.

### 프로그래밍에서 그래프는 크게 두 가지 방식으로 표현할 수 있는데 코딩 테스트에서는 이 두 가지 방식 모두가 필요하니 두 개념에 대해 바르게 알고 있도록 하자

<br/>

* 인접 행렬 (Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
* 인접 리스트 (Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식

</br>

### 먼저, 인접 해열 방식은 2차원 배열에서 각 노드가 연결된 형태를 기록하는 방식이다. 위와 같이 연결된 그래프를 인접 행렬로 표현할 때 파이썬에서는 2차원 리스트로 구현할 수 있다. 연결이 되어 있지 않은 노드끼리는 '무한'의 비용이라고 작성을 한다. 실제 코드에서는 논리적으로 정답이 될 수 없는 큰 값중에서 999999999, 987654321등의 값으로 초기화 하는 경우가 많다. 이렇게 그래프를 인접 행렬 방식으로 처리할 때는 다음과 같이 데이터를 초기화한다.

<hr/>

![인접행렬](https://images.velog.io/images/alsgk721/post/17a5671a-40c3-436e-999f-830827cdf76e/image.png)

```python
    # 인접 행렬 방식 예제

    INF = 999999999 #무한의 비용 선언(연결x)

    # 2차원 배열 인접 행렬 표현
    graph = [
        [0,7,5],
        [7,0,INF],
        [5,INF,0]
    ]

    print(graph)
```

<hr/>
<br/>

```python
    [[0, 7, 5], [7,0,999999999],[5,999999999,0]]
```


### 인접리스트 방식에서 데이터를 표현하는 방식을 알아본다. 인접 리스트 방식에서는 다음 그림처럼 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하며 저장한다. 연결리스트는 'Linked List'라는 자료구조를 이용해 구현하는데, C++이나 JAVA와 같은 프로그래밍 언어에서는 별도로 'LinkedList'기능을 위한 표준 라이브러리를 제공한다. 
### 반면에 파이썬에서는 기본 자료형인 리스트 자료형이 append()와 메소드를 제공하므로 전통적인 프로그래밍 언어에서의 배열과 연결 리스트의 기능을 모두 기본으로 제공한다. 파이썬으로 인접 리스트를 이용해 그래프를 표현하고자 할 때에도 단순히 2차원 리스트를 이용하면 된다.

</br>

![](https://images.velog.io/images/alsgk721/post/261d4d49-3d81-4539-83b3-9d9a42b382c2/image.png)

```python
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)] # 2차원 리스트 표현

# 노드 0에 연결된 노드 정보 저장(노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드 거리)
graph[2].append((0,5))

print(graph)

```

<br/>

```python
    [[(1,7),(2,5)],[(0,7)],[(0,5)]]
```

<hr/>

## 위의 두 방식의 차이

+ 메모리의 속도
    - 인접 행렬 방식 : 모든 관계를 저장(노드 갯수가 많아 메모리 비 효율적)
    - 인접 리스트 방식 : 연결된 정보만 저장 (메모리 효율적)

+ 정보를 얻는 속도
    - 인접 행렬 방식 : 빠름
    - 인접 리스트 방식 : 연결된 정보만을 저장하기 때문에 느림

<br/>
<hr/>
<br/>

## DFS 예시
### 한 그래프에서 노드 1과 노드 7이 연결되어 있는 상황을 생각해보자. 인접 행렬 방식에서는 graph[1][7]만 확인하면 된다. 반면에 인접 리스트 방식에서는 노드 1에 대한 인접 리스트를 앞에서부터 차례대로 확인해야 한다. 그러므로 특정한 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다.

<br/>

### DFS는  스택 자료구조를 이용하여 구체적인 동작 과정은 다음과 같다.

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2.번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


## DFS 동작 예시
* [step 0] 그래프를 준비한다. 시작노드는 1이다. 방문기준은 번호가 낮은 인접 노드 부터
![](https://blog.kakaocdn.net/dn/Rpk1U/btqSEKqhtGM/jfSwJl4aeP0zQfHTrb7Ia1/img.png)


<br/>

* [step 1] 시작노드인 '1'을 스택에 PUSH하고 방문처리 한다.
<br/>

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbDEE6U%2FbtqSEKKynR8%2Fly6bkQecX5FtxBoHilwufK%2Fimg.png)

<br/>

* [step 2] 스택의 최상단 노드인 '1'에 방문하지 않은 인접 노드들 중 우선순위가 높은 가장 작은 노드 '2'를 스택에 넣고 방문처리한다. 
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fuo2da%2FbtqSpGQjd6a%2FUulFHBRkDTkZ7ERbcl7YQ0%2Fimg.png)

<br/>

* [step 3] 스택의 최상단 노드인 '2'에 방문하지 않은 인접 노드는 '7'하나
이기 때문에 '7'을 스택에 넣고 방문처리한다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbBdav4%2FbtqSELCGmj5%2FfgUWCsahpOQkyj4873iEz1%2Fimg.png)

<br/>

* [step 4] 스택의 최상단 노드인 '7'에 방문하지 않은 인접노드는 '6','8'인데
이 중 가장 작은 노드인 '6'을 스택에 넣고 방문 처리한다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbevxIg%2FbtqSDunEvte%2FeGnhkU8uSGGuvzKJSLThf1%2Fimg.png)

<br/>

* [step 5] 스택의 최상단 노드인 '6'에 방문하지 않은 인접노드가 없기 때문에 
스택에서 '6'번 노드를 꺼낸다.(POP)
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbskX80%2FbtqSjAiNnVI%2FIneXiX7pKMXp4ALakfrGmk%2Fimg.png)

<br/>

* [step 6] 스택의 최상단 노드인 '7'에 방문하지 않은 인접 노드가 '8'이 남아있기 때문에 '8'을 스택에 넣고 방문처리한다.
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FpulBx%2FbtqSEL3Nwiy%2FpzaNlfEcoVOHozkTh0sOBk%2Fimg.png)

<br/>

* [step 7] 스택의 최상단 노드인 '8'에 방문하지 않은 인접노드가 없기 때문에 
스택에서 '8'번 노드를 꺼낸다. 이후 이 과정들을 반복해서 '3','4','5'번 노드를 스택에 담으면
<div  style="text-align: center;">
    <b>결과적으로 노드의 탐색 순서는 1 → 2 → 7 → 6 → 8 → 3 → 4 → 5</b>
</div>

