# 아이디어를 코드로 바꾸는 구현
## 피지컬로 승부하기
* 코딩테스트에서 구현(implementation)이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정'이다.
* 프로그래밍 언어의 문법을 정확하게 알고 있어야 하며 문제의 요구사항에 어긋나지 않는 답안 코드를 실수 없이 작성해야 한다.
* 흔히 문제 해결 분야에서 구현 유형의 문제는 '풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제'를 의미한다.
<hr/>

## 어떤 문제가 구현하기 어려운 문제인가? <br/>

* 알고리즘은 간단하지만 코드가 지나치게 길어지는 문제
* 특정 소수점 자리 까지 출력해야하는 문제
* 문자열이 입력으로 주어졌을 때 한 문자 단위로 끊어서 리스트로 처리해야하는 (혹은 파싱해야하는) 문제

<hr/>

### 구현의 유형

* 완전탐색
    * 모든 경우의 수를 주저 없이 다 계산하는 방법

* 시뮬레이션
    * 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제유형을 의미한다.
<hr/>


## 구현 시 고려해야 할 메모리 제약 사항

### C/C++에서 변수의 표현 범위

|정수형 종류|자료형 크기|자료형의 범위|
|:-----:|:-----:|:-------:|
|int|4바이트|-2,147,438,648 ~ 2,147,438,647|
|long long|8바이트|-9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807|
|Big Integer(클래스)|가변적|제한 없음|

<br/>

### 파이썬의 리스트 크기

* 대체로 코딩 테]스트는 128 ~ 512MB로 메모리를 제한하는데 알고리즘 문제 중 때로는 수백만 개 이상의 데이터를 처리해야 하는 문제가 출제되곤 한다. 이럴 때는 메모리 제한을 염두에 두고 코딩해야 한다.

* 
    |데이터의 갯수(리스트의 길이)|메모리 사용량|
    |:------:|:------:|
    |1,000|약 4KB|
    |1,000,000|약 4MB|
    |10,000,000|약 40MB|

* 1000만 이상인 리스트가 있다면 메모리 용량 제한으로 문제를 풀 수 없을 수도 있다.

## 체점 환경

* 파이썬은 C/C++보다 동작 속도가 느리다.

## 구현 문제에 접근 하는 방법

* 보통의 구현 유횽의 문제는 사소한 입력 조건 등을 문제애서 명시해주며 문제의 길이가 꽤 긴 편이다.
* 문제의 길이만을 보고 지레 겁을 먹는데, 고차원적인 사고력을 요구하는 문제는 나오지 않는 편이라 익숙하다면 오히려 쉽게 풀 수 있다.

* 구현 유형의 문제는 C/C++/JAVA로 문제를 풀 때 더 어렵게 느껴진다. 문자열을 처리하거나 파이썬에 비해 까다롭고, 큰 정수를 처리하는 라이브러리를 별도로 사용해야 하기 때문이다.

|             |구현 난이도|프로그램 실행 시간|
|:--------:|:------:|:----------:|
|파이썬|쉬운 편|긴 편|
|PyPy|쉬운 편|다소 짧은 편|
|C/C++|어려운 편|짧은 편|

