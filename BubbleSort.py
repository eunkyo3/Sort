import random

sort_num = random.sample(range(50), 10)

print('Before Bubble')
print(sort_num)

for i in range(len(sort_num) -1):
    for j in range(len(sort_num) -i -1):    
        if sort_num[j] > sort_num[j+1]: 
            sort_num[j], sort_num[j+1] = sort_num[j+1], sort_num[j]
        else:   
            pass

print('After Bubble')
print(sort_num
