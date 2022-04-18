# BFS
### BFS알고리즘은 '너비 우선 탐색'이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작한다고 했는데, BFS는 그 반대다. 어떻게 구현할 수 있을까? BFS구현에서 선입 선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다. 그림과 함꼐 자세한 동작 방식을 살펴본다.

<br/>

## 알고리즘의 정확한 동작방식
### 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
### 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
### 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

<br/>

## 그림으로 알아보는 동작 방식

<hr/>

### 다음의 그림으로 BFS(너비 우선 탐색을 해보겠다.)
!["BFS-1"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2F2f44a677-9f4e-4352-a916-d37405abcdc7%2Fimage.png)


### 시작 노드 1을 큐에 삽입하고 방문처리(TRUE)를 한다.
!["BFS-2"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2F0325b024-0214-445d-b47b-35074a95802b%2Fimage.png)

### 큐에서 노드 1을 꺼내고 인접 노드 2,3,8을 큐에 넣고 방문처리를 한다.
!["BFS-3"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2Fee112a0c-01bc-48e2-8c17-341e238b8670%2Fimage.png)

### 큐에서 가장 최근에 들어온 노드 2를 꺼내고 2의 인접 노드 7을 큐에 넣고 방문처리를 한다.
!["BFS-4"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2F87919caa-5af3-4ca1-b368-9a38a70fd4c7%2Fimage.png)

### 큐에서 가장 최근에 들어온 노드 3을 꺼내고 3의 인접 노드 4,5를 큐에 삽입하고 방문처리를 한다.
!["BFS-5"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2Fdc39f0fb-de13-4a5d-8ddf-a38713c61ae0%2Fimage.png)

### 큐에서 가장 최근에 들어온 노드 8을 꺼내고 8의 인접 노드 6을 큐에 삽입하고 방문처리를 한다.
!["BFS-6"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2F34cf889c-254f-4cf4-b952-a9ad2101d972%2Fimage.png)

### 더 이상 방문하지 않은 노드가 없으므로 큐에서 먼저 들어온 순서대로 꺼내어 정렬한다.
!["BFS-7"](https://velog.velcdn.com/images%2Fyellowsummer%2Fpost%2F38d9b7d1-c8fc-416c-9911-bfade89c2a52%2Fimage.png)

### BFS 정렬 결과
```
[결과] 1->2->3->8->7->4->5->6
```
