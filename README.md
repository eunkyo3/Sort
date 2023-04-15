# Sort

## Bubble Sort(버블 정렬)
```python
import random

# 무작위 정렬 숫자 선택
sort_num = random.sample(range(50), 10)

# 정렬하기 전
print(sort_num)

# 버블 정렬 과정
for i in range(len(sort_num) -1):
    for j in range(len(sort_num) -i -1):
        if sort_num[j] > sort_num[j+1]:
            sort_num[j], sort_num[j+1] = sort_num[j+1], sort_num[j]
        else:
            pass

# 정렬한 후
print(sort_num)
```
