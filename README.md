# Sort
컴퓨터 과학과 수학에서 정렬 알고리즘이란 원소들을 번호순이나 사전 순서와 같이 일정한 순서대로 열거하는 알고리즘이다
## Bubble Sort(버블 정렬)
버블 정렬이란 서로 인접한 두 원소의 값의 크기를 비교하고, 조건에 맞지 않는다면 자리를 교환하며 정렬하는 알고리즘이다.
### GIF로 이해하는 Bubble Sort
![bubble](https://user-images.githubusercontent.com/112944851/232243712-2bd099c0-f642-40e9-b1b4-2ca8db1b2775.gif)
### CODE로 이해하는 Bubble Sort
```python
import random

# 무작위 정렬 숫자 선택
sort_num = random.sample(range(50), 10)

# 정렬하기 전
print('Before Bubble')
print(sort_num)

# 버블 정렬 과정
for i in range(len(sort_num) -1):   # 버블 할 범위
    for j in range(len(sort_num) -i -1):    # 버블 정렬은 뒤부터 채우기 때문에 한칸씩 앞으로 당김
        if sort_num[j] > sort_num[j+1]: # 값 비교
            sort_num[j], sort_num[j+1] = sort_num[j+1], sort_num[j] # if문 조건에 충족하면 순서를 바꿈
        else:   # if에 해당하지 않으면 넘어감
            pass

# 정렬한 후
print('After Bubble')
print(sort_num)
```
### 시간복잡도
시간복잡도를 계산하면, (n-1) + (n-2) + (n-3) + .... + 2 + 1 => n(n-1)/2이므로, O(n^2) 이다. 또한, Bubble Sort는 정렬이 돼있던 안돼있던, 2개의 원소를 비교하기 때문에 최선, 평균, 최악의 경우 모두 시간복잡도가 O(n^2) 으로 동일하다.
### 공간복잡도
주어진 배열 안에서 교환(swap)을 통해, 정렬이 수행되므로 O(n) 이다.
### 장점
* 구현이 매우 간단하고, 소스코드가 직관적이다.

* 정렬하고자 하는 배열 안에서 교환하는 방식이므로, 다른 메모리 공간을 필요로 하지 않다. => 제자리 정렬(in-place sorting)

* 안정 정렬(Stable Sort) 이다.
### 단점
* 시간복잡도가 최악, 최선, 평균 모두 O(n^2)으로, 굉장히 비효율적이다.
 
* 정렬 돼있지 않은 원소가 정렬 됐을때의 자리로 가기 위해서, 교환 연산(swap)이 많이 일어나게 된다.

## Selection Sort(선택 정렬)
선택 정렬이란 버블 정렬과 유사한 알고리즘으로, 해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘이다. 쉽게 말해서 데이터들에 대해 가장 작은 데이터를 찾아 가장 앞의 데이터와 교환해 나가는 알고리즘이다.
### GIF로 이해하는 Selection Sort
![selection](https://user-images.githubusercontent.com/112944851/232245480-5037eff2-87f4-40d5-9348-5086820da7d5.gif)
### CODE로 이해하는 Selection Sort
```python
import random

# 무작위 정렬 숫자 선택
sort_num = random.sample(range(50), 10)

# 정렬하기 전
print('Before Selection')
print(sort_num)

# 선택 정렬 과정
for i in range(len(sort_num) - 1):  # N개의 데이터가 있는 리스트는 최대 N - 1번의 정렬이면 된다.
    min_index = i   # 가장 작은 값을 갖는 데이터의 index
    for j in range(i + 1, len(sort_num)):   # 현재 인덱스부터 마지막 인덱스까지 최소값의 인덱스를 찾음
        if sort_num[min_index] > sort_num[j]:   #  가작 작은 값의 변수가 다음 인덱스의 값보다 클 경우
            min_index = j   # 값을 변경
    sort_num[i], sort_num[min_index] = sort_num[min_index], sort_num[i] # 값 바꾸기

# 정렬한 후
print('After Selection')
print(sort_num)
```
### 시간복잡도
데이터의 개수가 n개라고 했을 때

* 첫 번째 회전에서의 비교횟수 : 1 ~ (n-1) => n-1

* 두 번째 회전에서의 비교횟수 : 2 ~ (n-1) => n-2

* (n-1) + (n-2) + .... + 2 + 1 => n(n-1)/2

비교하는 것이 상수 시간에 이루어진다는 가정 아래, n개의 주어진 배열을 정렬하는데 O(n^2) 만큼의 시간이 걸린다. 최선, 평균, 최악의 경우 시간복잡도는 O(n^2) 으로 동일하다.
### 공간복잡도
주어진 배열 안에서 교환(swap)을 통해, 정렬이 수행되므로 O(n) 이다.
### 장점
* Bubble sort와 마찬가지로 알고리즘이 단순하다.

* 정렬을 위한 비교 횟수는 많지만, Bubble Sort에 비해 실제로 교환하는 횟수는 적기 때문에 많은 교환이 일어나야 하는 자료상태에서 비교적 효율적이다.

* Bubble Sort와 마찬가지로 정렬하고자 하는 배열 안에서 교환하는 방식이므로, 다른 메모리 공간을 필요로 하지 않는다. => 제자리 정렬(in-place sorting)
### 단점
* 시간복잡도가 O(n^2)으로, 비효율적이다.

* 불안정 정렬(Unstable Sort) 이다.
## Insertion Sort(삽입 정렬)
삽입 정렬은 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘이다.
### GIF로 이해하는 Insertion Sort
![Insertion](https://user-images.githubusercontent.com/112944851/232316391-08625527-9a29-4bbe-baf0-f8ecad35f726.gif)
### CODE로 이해라는 Insertion Sort
```python
print('wait')
```
### 시간복잡도
### 공간복잡도
### 장점
### 단점
